from django.apps import AppConfig


class FinancialReportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'financial_report'

    def ready(self):
        import financial_report.signals
