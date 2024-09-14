from django.urls import path, include
from cinema.views import RevenueCreateView, RevenueListView, RevenueDeleteView, RevenueEditAPIView, \
    RevenueEditTemplateView, TicketListView, TicketCreateView, TicketEditAPIView, TicketDeleteView, \
    TicketEditTemplateView, ExpenseListView, ExpenseCreateView, ExpenseDeleteView, ExpenseEditAPIView, \
    ExpenseEditTemplateView, InventoryListView, InventoryCreateView, InventoryDeleteView, InventoryEditAPIView, \
    InventoryEditTemplateView
from rest_framework.routers import DefaultRouter

app_name = 'cinema'

urlpatterns = [
    path('revenues/', RevenueListView.as_view(), name='revenue-list'),
    path('revenues/create/', RevenueCreateView.as_view(), name='revenue-create'),
    path('revenues/delete/<int:revenue_id>/', RevenueDeleteView.as_view(), name='revenue-delete'),
    path('revenues/edit/<int:revenue_id>/', RevenueEditTemplateView.as_view(), name='revenue-edit-template'),
    path('revenues/edit/api/<int:revenue_id>/', RevenueEditAPIView.as_view(), name='revenue-edit-api'),
    # ------------------------------tickets-------------------------------------------
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('tickets/delete/<int:ticket_id>/', TicketDeleteView.as_view(), name='ticket-delete'),
    path('tickets/edit/<int:ticket_id>/', TicketEditTemplateView.as_view(), name='ticket-edit-template'),
    path('tickets/edit/api/<int:ticket_id>/', TicketEditAPIView.as_view(), name='ticket-edit-api'),
    # -------------------------------------expense--------------------------------------
    path('expenses/', ExpenseListView.as_view(), name='expense-list'),
    path('expenses/create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('expenses/delete/<int:expense_id>/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('expenses/edit/<int:expense_id>/', ExpenseEditTemplateView.as_view(), name='expense-edit-template'),
    path('expenses/edit/api/<int:expense_id>/', ExpenseEditAPIView.as_view(), name='expense-edit-api'),
    # -------------------------------------inventory--------------------------------------
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/create/', InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/delete/<int:inventory_id>/', InventoryDeleteView.as_view(), name='inventory-delete'),
    path('inventory/edit/<int:inventory_id>/', InventoryEditTemplateView.as_view(), name='inventory-edit-template'),
    path('inventory/edit/api/<int:inventory_id>/', InventoryEditAPIView.as_view(), name='inventory-edit-api'),

]
