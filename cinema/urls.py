from django.urls import path, include
from cinema.views import RevenueCreateView, RevenueListView, RevenueDeleteView, RevenueEditAPIView, \
    RevenueEditTemplateView, TicketListView, TicketCreateView, TicketEditAPIView, TicketDeleteView, TicketEditTemplateView
from rest_framework.routers import DefaultRouter

app_name = 'cinema'

urlpatterns = [
    path('revenues/', RevenueListView.as_view(), name='revenue-list'),
    path('revenues/create/', RevenueCreateView.as_view(), name='revenue-create'),
    path('revenues/delete/<int:revenue_id>/', RevenueDeleteView.as_view(), name='revenue-delete'),
    path('revenues/edit/<int:revenue_id>/', RevenueEditTemplateView.as_view(), name='revenue-edit-template'),
    path('revenues/edit/api/<int:revenue_id>/', RevenueEditAPIView.as_view(), name='revenue-edit-api'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('tickets/delete/<int:ticket_id>/', TicketDeleteView.as_view(), name='ticket-delete'),
    path('tickets/edit/<int:ticket_id>/', TicketEditTemplateView.as_view(), name='ticket-edit-template'),
    path('tickets/edit/api/<int:ticket_id>/', TicketEditAPIView.as_view(), name='ticket-edit-api'),

]
