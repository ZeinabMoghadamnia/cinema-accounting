from .models import Purchase
from .serializers import PurchaseSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .serializers import TaxSerializer
from financial_report.models import Tax
from employee_management.permissions import IsManager

# Create your views here.

class PurchaseListView(APIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated, IsManager]
    template_name = 'purchase.html'

    def get_queryset(self):
        return Purchase.objects.all()

    def get(self, request, *args, **kwargs):
        purchases = self.get_queryset()
        taxes = Tax.objects.all()
        purchase_data = []
        for purchase in purchases:
            tax_percentage = purchase.tax.tax_percentage
            total_cost_with_tax = purchase.quantity * purchase.cost + (
                        tax_percentage * purchase.cost * purchase.quantity / 100)
            serialized_purchase = self.serializer_class(purchase).data
            serialized_purchase['total_cost_with_tax'] = total_cost_with_tax
            purchase_data.append(serialized_purchase)

        # serialized_data = self.serializer_class(purchases, many=True).data
        return Response({'purchases': purchase_data, 'taxes': taxes, 'date': timezone.now().date()})

class PurchaseCreateView(APIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('vendor:purchase-list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, template_name='purchase.html')


class PurchaseDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, purchase_id, format=None):
        purchase = get_object_or_404(Purchase, id=purchase_id)
        purchase.delete()
        return Response({'message': 'Purchase deleted successfully'}, status=status.HTTP_204_NO_CONTENT, template_name='purchase.html')


class PurchaseEditAPIView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, purchase_id, format=None):
        purchase = get_object_or_404(Purchase, id=purchase_id)
        serializer = PurchaseSerializer(purchase)

        taxes = Tax.objects.all()
        tax_serializer = TaxSerializer(taxes, many=True)

        return Response({
            'purchase': serializer.data,
            'taxes': tax_serializer.data
        })

    def put(self, request, purchase_id, format=None):
        purchase = get_object_or_404(Purchase, id=purchase_id)
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class PurchaseEditTemplateView(LoginRequiredMixin, View):
    def get(self, request, purchase_id):
        return render(request, 'purchase.html', {'purchase_id': purchase_id})