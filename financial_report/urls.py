from django.urls import path

from .views import FinancialReportView, ChartAPIView, chart_view

app_name = 'financial-report'
urlpatterns = [
    path('report/', FinancialReportView.as_view(), name='financial-report'),
    path('api/daily-report-data/', ChartAPIView.as_view(), name='daily-report-data'),
    path('chart/', chart_view, name='chart-view'),
]
