from django.db import models
from django.http import JsonResponse
from django.utils import timezone
from django.views import View

from core.models import BaseModel


# Create your models here.

class Tax(BaseModel):
    TAX_TYPES = (
        ('employee tax', 'Employee tax'),
        ('cinema tax', 'Cinema tax'),
    )
    tax_percentage = models.IntegerField(verbose_name='Tax Percentage')
    tax_type = models.CharField(max_length=50, choices=TAX_TYPES, verbose_name='Tax Type')
    date = models.DateField(verbose_name="date", default=timezone.now)

    def __str__(self):
        return f"{self.tax_type} - {self.tax_percentage}"


class DailyReport(BaseModel):
    profit = models.IntegerField(verbose_name='Profit')
    total_revenue = models.IntegerField(verbose_name='Total Revenue')
    total_expense = models.IntegerField(verbose_name='Total Expense')
    total_taxes = models.IntegerField(verbose_name='Total Taxes')
    date = models.DateField(verbose_name="date", default=timezone.now)

    def __str__(self):
        return f"{self.created_at}"

