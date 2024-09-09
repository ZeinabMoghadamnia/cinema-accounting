from django.contrib import admin
from  .models import EmployeePerformance, PayRoll, CustomUser
# Register your models here.

admin.site.register([EmployeePerformance, PayRoll, CustomUser])