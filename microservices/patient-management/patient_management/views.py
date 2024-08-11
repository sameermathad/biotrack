from rest_framework import viewsets
from .models import Patient, MedicalHistory, Appointment
from .serializers import PatientSerializer, MedicalHistorySerializer, AppointmentSerializer
from datetime import datetime


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient')
        date_str = self.request.query_params.get('date')

        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)

        if date_str:
            try:
                # Convert the date string to a datetime object
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                # Filter queryset by the exact date (without time component)
                queryset = queryset.filter(date__date=date_obj.date())
            except ValueError:
                pass  # Handle the error if the date format is incorrect

        return queryset