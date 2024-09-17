from django.contrib import admin
from .models import Tax, DailyReport
# Register your models here.

# class DailyReportAdmin(admin.ModelAdmin):
#     list_display = ('profit', 'total_revenue', 'total_taxes', 'total_expense')
#
#     readonly_fields = ['updated_at', 'created_at']
#
#     fields = ('profit', 'total_revenue', 'total_taxes', 'total_expense', 'created_at')
#
# admin.site.register(DailyReport, DailyReportAdmin)

admin.site.register([DailyReport, Tax])