from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum
from django.urls import path
from .models import DailyReport
from employee_management.models import Payroll
from rest_framework import status
from django.utils.dateparse import parse_date
from .serializers import DailyReportSerializer

class FinancialReportView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'reports.html'
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({'error': 'Both start_date and end_date are required.'}, status=status.HTTP_400_BAD_REQUEST)

        start_date = parse_date(start_date)
        end_date = parse_date(end_date)

        if not start_date or not end_date:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            daily_reports = DailyReport.objects.filter(date__range=[start_date, end_date]).values(
                'date', 'total_revenue', 'total_expense', 'total_taxes', 'profit'
            )

            payrolls = Payroll.objects.filter(date__range=[start_date, end_date]).values('date').annotate(
                total_salary=Sum('net_salary')
            )

            payroll_dict = {item['date']: item['total_salary'] for item in payrolls}

            totals = DailyReport.objects.filter(date__range=[start_date, end_date]).aggregate(
                total_revenue=Sum('total_revenue'),
                total_expense=Sum('total_expense'),
                total_taxes=Sum('total_taxes'),
                total_profit=Sum('profit')
            )

            total_payroll = sum(payroll_dict.values())
            net_profit_after_payroll = (totals['total_profit'] or 0) - total_payroll

            daily_reports_list = []
            for report in daily_reports:
                payroll_for_day = payroll_dict.get(report['date'], 0)
                net_profit_for_day = report['profit'] - payroll_for_day
                report['total_salary'] = payroll_for_day
                report['net_profit_after_salary'] = net_profit_for_day
                daily_reports_list.append(report)

            daily_reports_list.append({
                'date': 'Total',
                'total_revenue': totals['total_revenue'],
                'total_expense': totals['total_expense'],
                'total_taxes': totals['total_taxes'],
                'profit': totals['total_profit'],
                'total_salary': total_payroll,
                'net_profit_after_salary': net_profit_after_payroll
            })

            return Response({'reports': daily_reports_list}, template_name=self.template_name)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class ChartAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        reports = DailyReport.objects.all()

        if start_date and end_date:
            reports = reports.filter(date__range=[parse_date(start_date), parse_date(end_date)])

        serializer = DailyReportSerializer(reports, many=True)
        return Response(serializer.data)

def chart_view(request):
    return render(request, 'charts.html')