# patient_management/serializers.py
from rest_framework import serializers
from .models import Patient, MedicalHistory, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source='patient', write_only=True)
    patient = PatientSerializer(read_only=True)  # Keep this to include patient details in the response

    class Meta:
        model = Appointment
        fields = '__all__'
