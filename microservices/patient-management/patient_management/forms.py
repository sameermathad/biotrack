from django import forms
from .models import Patient, MedicalHistory, Appointment, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_address', 'city', 'state', 'postal_code', 'country']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['user', 'first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'address']

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['patient', 'condition', 'description', 'date_diagnosed']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'date', 'reason', 'notes']
