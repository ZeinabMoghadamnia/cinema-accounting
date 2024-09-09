from django.contrib import admin
from .models import Cinema, Revenue, Expense, Inventory, Ticket, Movie
# Register your models here.

admin.site.register([Cinema, Revenue, Expense, Inventory, Ticket, Movie])