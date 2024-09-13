from rest_framework import serializers
from .models import Ticket, Revenue, Cinema
from financial_report.models import Tax

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'customers_phone_number', 'seat_number', 'price', 'start_time', 'end_time', 'movie', 'cinema', 'is_sold']

class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = ['id', 'ticket_sale', 'concession_sale', 'other_income', 'cinema', 'tax', 'date']

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id', 'name']

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ['id', 'tax_type', 'tax_percentage']