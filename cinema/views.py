from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from cinema.models import Ticket, Revenue, Cinema
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from cinema.serializers import TicketSerializer, RevenueSerializer
import requests
from django.test import Client
from .serializers import CinemaSerializer, TaxSerializer

from financial_report.models import Tax


# Create your views here.

class TicketAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            ticket = get_object_or_404(Ticket, pk=pk)
            return render(request, 'tickets.html', {'ticket': ticket})
        else:
            tickets = Ticket.objects.all().select_related('movie', 'cinema')
            return render(request, 'tickets.html', {'tickets': tickets})

    def post(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'tickets.html', {'ticket': serializer.instance})
        return render(request, 'tickets.html', {'errors': serializer.errors})


class RevenueListView(APIView):
    serializer_class = RevenueSerializer
    permission_classes = [IsAuthenticated]
    template_name = 'revenue.html'

    def get_queryset(self):
        return Revenue.objects.all()

    def get(self, request, *args, **kwargs):
        revenues = self.get_queryset()
        cinemas = Cinema.objects.all()
        taxes = Tax.objects.all()
        serialized_data = self.serializer_class(revenues, many=True).data
        return Response({'revenues': serialized_data, 'cinemas': cinemas, 'taxes': taxes, 'date': timezone.now().date()})



class RevenueCreateView(APIView):
    serializer_class = RevenueSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cinema:revenue-list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, template_name='revenue.html')


class RevenueDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, revenue_id, format=None):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        revenue.delete()
        return Response({'message': 'Revenue deleted successfully'}, status=status.HTTP_204_NO_CONTENT, template_name='revenue.html')


class RevenueEditAPIView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, revenue_id, format=None):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        serializer = RevenueSerializer(revenue)

        cinemas = Cinema.objects.all()
        taxes = Tax.objects.all()
        cinema_serializer = CinemaSerializer(cinemas, many=True)
        tax_serializer = TaxSerializer(taxes, many=True)

        return Response({
            'revenue': serializer.data,
            'cinemas': cinema_serializer.data,
            'taxes': tax_serializer.data
        })

    def put(self, request, revenue_id, format=None):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        serializer = RevenueSerializer(revenue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class RevenueEditTemplateView(LoginRequiredMixin, View):
    def get(self, request, revenue_id):
        return render(request, 'revenue.html', {'revenue_id': revenue_id})
