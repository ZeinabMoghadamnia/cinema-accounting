from rest_framework import serializers
from .models import Ticket, Revenue, Cinema, Movie
from financial_report.models import Tax


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


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ['tax_type', 'tax_percentage']


class RevenueSerializer(serializers.ModelSerializer):
    tax = TaxSerializer()

    class Meta:
        model = Revenue
        fields = ['id', 'ticket_sale', 'concession_sale', 'other_income', 'tax', 'date']


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id', 'name']



