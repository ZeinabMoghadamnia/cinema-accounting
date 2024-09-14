from rest_framework import serializers
from .models import Ticket, Revenue, Cinema, Movie, Expense, Inventory
from financial_report.models import Tax
from financial_report.serializers import TaxSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source='movie', write_only=True
    )

    class Meta:
        model = Ticket
        fields = [
            'id', 'customers_phone_number', 'seat_number', 'price',
            'start_time', 'end_time', 'movie', 'movie_id', 'date'
        ]



class InventorySerializer(serializers.ModelSerializer):
    tax = TaxSerializer(read_only=True)
    tax_id = serializers.PrimaryKeyRelatedField(
        queryset=Tax.objects.all(), source='tax', write_only=True
    )

    class Meta:
        model = Inventory
        fields = ['id', 'date', 'item_name', 'quantity', 'tax', 'tax_id', 'cost']

class RevenueSerializer(serializers.ModelSerializer):
    tax = TaxSerializer(read_only=True)
    tax_id = serializers.PrimaryKeyRelatedField(
        queryset=Tax.objects.all(), source='tax', write_only=True
    )

    class Meta:
        model = Revenue
        fields = ['id', 'ticket_sale', 'concession_sale', 'other_income', 'tax', 'tax_id', 'date']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'



class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id', 'name']



