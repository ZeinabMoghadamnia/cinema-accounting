from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from  .models import EmployeePerformance, Payroll, CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'phone_number', 'first_name', 'last_name', 'is_active', 'user_type')
    list_filter = ('is_active', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'first_name', 'last_name', 'user_type', 'password1', 'password2', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register([EmployeePerformance, Payroll])