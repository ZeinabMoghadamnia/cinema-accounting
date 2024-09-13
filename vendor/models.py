from django.db import models
from django.utils import timezone

from employee_management.models import CustomUser
from core.models import BaseModel


# Create your models here.

class Vendor(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor', verbose_name="user")
    address = models.CharField(max_length=120, verbose_name="address")
    company_name = models.CharField(max_length=50, verbose_name="company name")

    def __str__(self):
        return self.company_name


class Purchase(BaseModel):
    amount = models.IntegerField(verbose_name="amount")
    description = models.CharField(max_length=120, verbose_name="description")
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchases', verbose_name="vendor")
    date = models.DateField(verbose_name="date", default=timezone.now)

    def __str__(self):
        return self.description
