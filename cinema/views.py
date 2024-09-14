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
from cinema.models import Ticket, Revenue, Cinema, Movie
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from cinema.serializers import TicketSerializer, RevenueSerializer, MovieSerializer
import requests
from django.test import Client
from .serializers import CinemaSerializer, TaxSerializer

from financial_report.models import Tax


# Create your views here.


class RevenueListView(APIView):
    serializer_class = RevenueSerializer
    permission_classes = [IsAuthenticated]
    template_name = 'revenue.html'

    def get_queryset(self):
        return Revenue.objects.all()

    def get(self, request, *args, **kwargs):
        revenues = self.get_queryset()
        taxes = Tax.objects.all()
        serialized_data = self.serializer_class(revenues, many=True).data
        return Response({'revenues': serialized_data, 'taxes': taxes, 'date': timezone.now().date()})



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

        taxes = Tax.objects.all()
        tax_serializer = TaxSerializer(taxes, many=True)

        return Response({
            'revenue': serializer.data,
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


#-------------------------------------------------------------------------------------

class TicketListView(APIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    template_name = 'tickets.html'

    def get_queryset(self):
        return Ticket.objects.all()

    def get(self, request, *args, **kwargs):
        tickets = self.get_queryset()
        movies = Movie.objects.all()
        serialized_data = self.serializer_class(tickets, many=True).data
        return Response({'tickets': serialized_data, 'movies': movies, 'date': timezone.now().date()})



class TicketCreateView(APIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cinema:ticket-list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, ticket_id, format=None):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.delete()
        return Response({'message': 'ticket deleted successfully'}, status=status.HTTP_204_NO_CONTENT, template_name='tickets.html')


class TicketEditAPIView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, ticket_id, format=None):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        serializer = TicketSerializer(ticket)
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)

        return Response({
            'tickets': serializer.data,
            'movies': movie_serializer.data
        })

    def put(self, request, ticket_id, format=None):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TicketEditTemplateView(LoginRequiredMixin, View):
    def get(self, request, ticket_id):
        return render(request, 'tickets.html', {'ticket_id': ticket_id})
