from django.apps import AppConfig


class EmployeeManagementConfig(AppConfig):
    name = 'employee_management'

    def ready(self):
        import employee_management.signals
