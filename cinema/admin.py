from django.contrib import admin
from .models import Cinema, Revenue, Expense, Inventory, Ticket, Movie
# Register your models here.

# class TicketAdmin(admin.ModelAdmin):
#     list_display = ('id', 'movie', 'cinema', 'seat_number', 'price', 'start_time', 'end_time', 'is_sold', 'created_at')
#
#     readonly_fields = ['updated_at']
#
#     fields = ('movie', 'cinema', 'seat_number', 'price', 'start_time', 'end_time', 'is_sold', 'created_at', 'updated_at')
#
#     search_fields = ('movie__title', 'cinema__name', 'customers_phone_number')
#     list_filter = ('is_sold', 'created_at', 'start_time')
#
# admin.site.register(Ticket, TicketAdmin)

admin.site.register([Revenue, Expense, Cinema, Inventory, Movie, Ticket])