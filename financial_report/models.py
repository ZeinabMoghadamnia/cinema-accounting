from django.db import models
from core.models import BaseModel


# Create your models here.

class Tax(BaseModel):
    tax_percentage = models.IntegerField(verbose_name='Tax Percentage')
    tax_type = models.CharField(max_length=50, verbose_name='Tax Type')

    def __str__(self):
        return f"{self.tax_type} - {self.tax_percentage}"


class DailyReport(BaseModel):
    profit = models.IntegerField(verbose_name='Profit')
    total_revenue = models.IntegerField(verbose_name='Total Revenue')
    total_expense = models.IntegerField(verbose_name='Total Expense')
    total_taxes = models.IntegerField(verbose_name='Total Taxes')

    def __str__(self):
        return f"{self.created_at}"
