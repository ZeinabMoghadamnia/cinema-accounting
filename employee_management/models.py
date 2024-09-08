from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from core.models import BaseModel


# Create your models here.

class CustomUser(AbstractUser, BaseModel):
    USER_TYPES = (
        ('manager', 'Manager'),
        ('vendor', 'Vendor'),
        ('employee', 'Employee'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, verbose_name='user type', null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, verbose_name='email address')
    mobile_regex = RegexValidator(regex='^(\+98|0)?9\d{9}$',
                                  message="Please enter the phone number in this format: '09999999999'")
    phone_number = models.CharField(validators=[mobile_regex], max_length=11, unique=True, verbose_name='phone')
    first_name = models.CharField(max_length=40, verbose_name='first name')
    last_name = models.CharField(max_length=40, verbose_name='last name')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']

    class Meta:
        verbose_name_plural = 'user'

    def __str__(self):
        return self.email


class EmployeePerformance(BaseModel):
    kpi_type = models.CharField(max_length=20, verbose_name='kpi type')
    kpi_value = models.IntegerField(verbose_name='kpi value')

    def __str__(self):
        return self.kpi_type


class PayRoll(BaseModel):
    salary = models.IntegerField(verbose_name='salary')
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="pay_roll", verbose_name='employee')
