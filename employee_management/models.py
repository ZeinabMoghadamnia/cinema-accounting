from django.contrib.auth.models import AbstractUser, Permission, Group
from django.core.validators import RegexValidator
from django.db import models
from core.models import BaseModel
from .managers import CostumeUserManager
from financial_report.models import Tax
from django.db.models import Q, UniqueConstraint
from django.utils import timezone
from django.apps import apps


# Create your models here.

class CustomUser(AbstractUser, BaseModel):
    USER_TYPES = (
        ('manager', 'Manager'),
        ('vendor', 'Vendor'),
        ('employee', 'Employee'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, verbose_name='user type', null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, verbose_name='email address')
    mobile_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$',
                                  message="Please enter the phone number in this format: '09999999999'")
    phone_number = models.CharField(validators=[mobile_regex], max_length=11, unique=True, verbose_name='phone')
    first_name = models.CharField(max_length=40, verbose_name='first name')
    last_name = models.CharField(max_length=40, verbose_name='last name')
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permission_set', blank=True)
    is_active = models.BooleanField(default=False, verbose_name='active')
    objects = CostumeUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']

    class Meta:
        verbose_name_plural = 'user'

    def __str__(self):
        return self.email


class EmployeePerformance(BaseModel):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='employee_performance_set')
    PERFORMANCE_TYPES = (
        ('overtime', 'Overtime'),
        ('absence', 'Absence'),
    )
    performance_type = models.CharField(max_length=20, choices=PERFORMANCE_TYPES, verbose_name='performance type')
    number_of_hours = models.IntegerField(verbose_name='performance value')
    date = models.DateField(verbose_name='date', default=timezone.now)

    def __str__(self):
        return self.performance_type


class Payroll(BaseModel):
    salary = models.IntegerField(verbose_name='salary')
    net_salary = models.IntegerField(verbose_name='net salary', null=True, blank=True)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="pay_roll", verbose_name='employee')
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, related_name="pay_roll", verbose_name='tax')
    date = models.DateField(verbose_name='date', default=timezone.now)

    def __str__(self):
        return self.employee.last_name

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['employee'],
                condition=Q(created_at__year=timezone.now().year, created_at__month=timezone.now().month),
                name='unique_payroll_per_employee_per_month'
            )
        ]
