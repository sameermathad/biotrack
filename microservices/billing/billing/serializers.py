from decimal import Decimal
from rest_framework import serializers
from .models import Invoice, Payment, InsuranceClaim, InvoiceItem

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
        extra_kwargs = {
            'invoice': {'required': False},  # Make the invoice field not required here
        }

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = '__all__'
        extra_kwargs = {
            'grand_total': {'read_only': True},  # Mark grand_total as read-only
        }

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)

        for item_data in items_data:
            # The invoice field is not required in the request, so we add it manually here
            InvoiceItem.objects.create(invoice=invoice, **item_data)

        # Recalculate grand_total after items have been created
        invoice.cgst_total = sum(item.cgst_amount for item in invoice.items.all())
        invoice.sgst_total = sum(item.sgst_amount for item in invoice.items.all())
        invoice.igst_total = sum(item.igst_amount for item in invoice.items.all())
        invoice.grand_total = invoice.total_amount + invoice.cgst_total + invoice.sgst_total + invoice.igst_total
        invoice.save(update_fields=['cgst_total', 'sgst_total', 'igst_total', 'grand_total'])

        return invoice


    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class InsuranceClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceClaim
        fields = '__all__'
