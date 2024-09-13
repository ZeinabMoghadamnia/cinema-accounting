from rest_framework import serializers
from .models import DailyReport

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ['profit', 'total_revenue', 'total_expense', 'total_taxes', 'date']
