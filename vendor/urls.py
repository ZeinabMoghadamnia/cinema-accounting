from django.urls import path, include
from .views import PurchaseListView, PurchaseCreateView, PurchaseDeleteView, PurchaseEditAPIView, \
    PurchaseEditTemplateView

app_name = 'vendor'

urlpatterns = [
    path('purchase/', PurchaseListView.as_view(), name='purchase-list'),
    path('purchase/create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('purchase/delete/<int:purchase_id>/', PurchaseDeleteView.as_view(), name='purchase-delete'),
    path('purchase/edit/<int:purchase_id>/', PurchaseEditTemplateView.as_view(), name='purchase-edit-template'),
    path('purchase/edit/api/<int:purchase_id>/', PurchaseEditAPIView.as_view(), name='purchase-edit-api'),

]
