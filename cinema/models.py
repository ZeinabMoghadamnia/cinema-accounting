from django.db import models
from django.utils import timezone

from core.models import BaseModel
from vendor.models import Vendor
from financial_report.models import Tax


# Create your models here.

class Cinema(BaseModel):
    name = models.CharField(max_length=50, verbose_name="cinema name")
    location = models.CharField(max_length=100, verbose_name="cinema location")

    def __str__(self):
        return self.name


class Movie(BaseModel):
    title = models.CharField(max_length=50, verbose_name="title")
    image = models.ImageField(upload_to='movies', verbose_name="image")

    def __str__(self):
        return self.title


class Ticket(BaseModel):
    customers_phone_number = models.CharField(max_length=50, null=True, blank=True,
                                              verbose_name="Customers phone number")
    seat_number = models.IntegerField(verbose_name="seat number")
    price = models.IntegerField(verbose_name="price")
    start_time = models.DateTimeField(verbose_name="start time")
    end_time = models.DateTimeField(verbose_name="end time")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_ticket", verbose_name="movie")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name="cinema_ticket", verbose_name="cinema")
    is_sold = models.BooleanField(default=False, verbose_name="is sold")
    date = models.DateField(verbose_name="date", default=timezone.now)

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"


class Expense(BaseModel):
    EXPENSE_TYPES = (
        ('marketing & advertising', 'Marketing & Advertising'),
        ('utilities', 'Utilities'),
        ('rent & insurance', 'Rent & Insurance'),
        ('other', 'Other'),
    )
    expense_type = models.CharField(max_length=50, verbose_name="expense type")
    amount = models.IntegerField(verbose_name="expense amount")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name="expense", verbose_name="cinema")
    description = models.TextField(verbose_name="expense description", blank=True, null=True)
    date = models.DateField(verbose_name="date", default=timezone.now)

    def __str__(self):
        return self.expense_type


class Inventory(BaseModel):
    item_name = models.CharField(max_length=50, verbose_name="item name")
    quantity = models.IntegerField(verbose_name="quantity")
    cost = models.IntegerField(verbose_name="cost")
    final_amount = models.IntegerField(verbose_name="final amount")
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, related_name="inventory", verbose_name="tax")
    date = models.DateField(verbose_name="date", default=timezone.now)

    def __str__(self):
        return self.item_name


class Revenue(BaseModel):
    ticket_sale = models.IntegerField(verbose_name="ticket sale")
    concession_sale = models.IntegerField(verbose_name="concession sale")
    other_income = models.IntegerField(verbose_name="other income")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name="revenue", verbose_name="cinema")
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, related_name="revenue", verbose_name="tax")
    date = models.DateField(verbose_name='date', default=timezone.now)

    def __str__(self):
        return f"{self.ticket_sale}"
