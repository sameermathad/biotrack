from django.db import models
import requests
import os
from decimal import Decimal


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    patient_id = models.CharField(max_length=100)  # Storing patient ID as a string
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cgst_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sgst_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    igst_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Default to 0.0 to avoid IntegrityError
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_patient_info(self):
        if os.getenv('DJANGO_ENV') == 'production':
            patient_url = f'https://patient-management-biotrack-370c80e6750a.herokuapp.com/api/patients/{self.patient_id}/'
        else:
            patient_url = f'http://127.0.0.1:8001/api/patients/{self.patient_id}/'
        
        response = requests.get(patient_url)
        if response.status_code == 200:
            return response.json()
        return None

    def save(self, *args, **kwargs):
        # Save the instance first if it hasn't been saved yet
        if not self.pk:
            self.grand_total = 0.0  # Temporary value to avoid IntegrityError
            super().save(*args, **kwargs)

        # Recalculate totals after the initial save
        self.cgst_total = sum(item.cgst_amount for item in self.items.all())
        self.sgst_total = sum(item.sgst_amount for item in self.items.all())
        self.igst_total = sum(item.igst_amount for item in self.items.all())
        self.grand_total = self.total_amount + self.cgst_total + self.sgst_total + self.igst_total

        # Save the instance again with the updated totals
        super().save(update_fields=['cgst_total', 'sgst_total', 'igst_total', 'grand_total'])

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    test_id = models.CharField(max_length=100)  # Storing test ID as a string
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    taxable_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cgst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sgst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    igst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    cgst_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sgst_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    igst_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def get_test_info(self):
        if os.getenv('DJANGO_ENV') == 'production':
            test_url = f'https://test-management-biotrack-d934c9e26f2a.herokuapp.com/api/tests/{self.test_id}/'
        else:
            test_url = f'http://localhost:8000/api/tests/{self.test_id}/'
        
        response = requests.get(test_url)
        if response.status_code == 200:
            return response.json()
        return None

    def save(self, *args, **kwargs):
        if self.taxable_value is None:
            self.taxable_value = self.unit_price
        self.cgst_amount = (self.taxable_value * self.cgst_rate) / 100
        self.sgst_amount = (self.taxable_value * self.sgst_rate) / 100
        self.igst_amount = (self.taxable_value * self.igst_rate) / 100
        super().save(*args, **kwargs)


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('Credit Card', 'Credit Card'), ('Cash', 'Cash'), ('Insurance', 'Insurance')])
    payment_date = models.DateTimeField(auto_now_add=True)

class InsuranceClaim(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    insurance_provider = models.CharField(max_length=100)
    claim_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50, choices=[('Submitted', 'Submitted'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])
    claim_date = models.DateTimeField(auto_now_add=True)
