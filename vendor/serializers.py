from rest_framework import serializers
from financial_report.serializers import TaxSerializer
from financial_report.models import Tax
from vendor.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    tax = TaxSerializer(read_only=True)
    tax_id = serializers.PrimaryKeyRelatedField(
        queryset=Tax.objects.all(), source='tax', write_only=True
    )

    class Meta:
        model = Purchase
        fields = ['id', 'date', 'item_name', 'quantity', 'tax', 'tax_id', 'cost']