from django.db import models
from .managers import BaseManager
from django.utils import timezone


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='date created')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='date updated')
    is_deleted = models.BooleanField(default=False, verbose_name='delete status')
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name='date deleted')
    restored_at = models.DateTimeField(blank=True, null=True, verbose_name='date restored')
    objects = BaseManager()

    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()
