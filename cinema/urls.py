from django.urls import path, include
from cinema.views import TicketAPIView, RevenueCreateView, RevenueListView, RevenueDeleteView, RevenueEditAPIView, \
    RevenueEditTemplateView
from rest_framework.routers import DefaultRouter

app_name = 'cinema'

urlpatterns = [
    path('tickets/', TicketAPIView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', TicketAPIView.as_view(), name='ticket-detail'),
    path('revenues/', RevenueListView.as_view(), name='revenue-list'),
    path('revenues/create/', RevenueCreateView.as_view(), name='revenue-create'),
    path('revenues/delete/<int:revenue_id>/', RevenueDeleteView.as_view(), name='revenue-delete'),
    path('revenues/edit/<int:revenue_id>/', RevenueEditTemplateView.as_view(), name='revenue-edit-template'),

    # URL برای ویوی API (که داده‌های JSON را برمی‌گرداند)
    path('revenues/edit/api/<int:revenue_id>/', RevenueEditAPIView.as_view(), name='revenue-edit-api'),

]
