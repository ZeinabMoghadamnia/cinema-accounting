from django.db import models
from django.utils import timezone

from employee_management.models import CustomUser
from core.models import BaseModel
from financial_report.models import Tax


# Create your models here.

class Vendor(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor', verbose_name="user")
    address = models.CharField(max_length=120, verbose_name="address")
    company_name = models.CharField(max_length=50, verbose_name="company name")

    def __str__(self):
        return self.company_name


class Purchase(BaseModel):
    item_name = models.CharField(max_length=50, verbose_name="item name")
    quantity = models.IntegerField(verbose_name="quantity")
    cost = models.IntegerField(verbose_name="cost")
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, related_name="purchase", verbose_name="tax")
    date = models.DateField(verbose_name="date", default=timezone.now)

    def __str__(self):
        return self.item_name
