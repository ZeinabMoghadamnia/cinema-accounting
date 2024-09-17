from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    name = 'cinema'

    def ready(self):
        import cinema.signals