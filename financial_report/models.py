from django.db import models
from core.models import BaseModel
from employee_management.models import CustomUser
from cinema.models import Revenue


# Create your models here.

class Tax(BaseModel):
    amount = models.IntegerField(verbose_name='Amount')
    tax_percentage = models.IntegerField(verbose_name='Tax Percentage')
    tax_type = models.CharField(max_length=50, verbose_name='Tax Type')
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="employee_tax", verbose_name='Employee')
    revenue = models.ForeignKey(Revenue, on_delete=models.CASCADE, related_name="revenue_tax", verbose_name='Revenue')

    def __str__(self):
        return f"{self.amount} {self.tax_type}"


class Daily_Report(BaseModel):
    profit = models.IntegerField(verbose_name='Profit')
    total_revenue = models.IntegerField(verbose_name='Total Revenue')
    total_expense = models.IntegerField(verbose_name='Total Expense')
    total_taxes = models.IntegerField(verbose_name='Total Taxes')

    def __str__(self):
        return self.created_at
