from  django.db import models

class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    def get_deleted(self):
        return super().get_queryset().filter(is_deleted=True)
    def get_archived(self):
        return super().get_queryset()