from django.contrib import admin
from .models import Tax, DailyReport
# Register your models here.

admin.site.register([DailyReport, Tax])