from django.contrib import admin
from .models import Vendor, Purchase
# Register your models here.

admin.site.register([Vendor, Purchase])