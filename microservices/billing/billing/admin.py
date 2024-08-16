# admin.py
from django.contrib import admin
from .models import Invoice, Payment, InsuranceClaim, InvoiceItem

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'patient_id', 'total_amount', 'status', 'created_at')
    search_fields = ('invoice_number', 'patient_id')

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'test_id', 'unit_price', 'taxable_value', 'cgst_amount', 'sgst_amount', 'igst_amount')
    search_fields = ('invoice__invoice_number', 'test_id')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'payment_method', 'payment_date')
    search_fields = ('invoice__invoice_number',)

@admin.register(InsuranceClaim)
class InsuranceClaimAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'insurance_provider', 'claim_number', 'status', 'claim_date')
    search_fields = ('claim_number', 'insurance_provider')
