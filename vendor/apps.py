from django.apps import AppConfig


class InventoryAppConfig(AppConfig):
    name = 'vendor'

    def ready(self):
        import vendor.signals
