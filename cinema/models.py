from django.db import models


# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    expense_type = models.CharField(max_length=50)
    amount = models.IntegerField()
    other_income = models.IntegerField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    # vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    def __str__(self):
        return self.expense_type


class Inventory(models.Model):
    item_name = models.CharField(max_length=50, verbose_name="item name")
    quantity = models.IntegerField(verbose_name="quantity")
    cost = models.IntegerField(verbose_name="cost")
    date_time = models.DateTimeField(verbose_name="date time")

    def __str__(self):
        return self.item_name


class Revenue(models.Model):
    ticket_sale = models.IntegerField(verbose_name="ticket sale")
    concession_sale = models.IntegerField(verbose_name="concession sale")
    other_income = models.IntegerField(verbose_name="other income")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name="cinema")
    date_time = models.DateTimeField()

    def __str__(self):
        return self.ticket_sale


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    image = models.ImageField(upload_to='movies', verbose_name="image")

    def __str__(self):
        return self.title


class Ticket(models.Model):
    Customers_phone_number = models.CharField(max_length=50, verbose_name="Customers phone number")
    seat_number = models.IntegerField(verbose_name="seat number")
    price = models.IntegerField(verbose_name="price")
    sale_date_time = models.DateTimeField(verbose_name="sale date time")
    start_time = models.DateTimeField(verbose_name="start time")
    end_time = models.DateTimeField(verbose_name="end time")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name="cinema")

    def __str__(self):
        return self.Customers_phone_number
