from django.contrib import admin
from  .models import EmployeePerformance, Payroll, CustomUser
# Register your models here.

admin.site.register([EmployeePerformance, Payroll, CustomUser])