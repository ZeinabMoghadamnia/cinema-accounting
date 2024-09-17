from django.urls import path
from .views import LoginView, LogoutView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'employee_management'
urlpatterns = [
    path('',LoginView.as_view(),name="login_page"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]