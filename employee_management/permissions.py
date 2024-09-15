
from rest_framework.permissions import BasePermission

class CinemaPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.user_type == 'manager' or request.user.user_type == 'employee')

class VendorPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.user_type == 'vendor' or request.user.user_type == 'manager')
