import os
import requests
from django.db import models
from django.utils import timezone

class Report(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Reviewed', 'Reviewed'),
    ]

    patient_id = models.CharField(max_length=100)  # Fetched from Patient Microservice
    test_result = models.ForeignKey('TestResult', on_delete=models.CASCADE)  # Fetched from Test Management Microservice
    created_by_user_id = models.CharField(max_length=100)  # Store the user_id instead of a ForeignKey
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Report for {self.patient_id} on {self.test_result.date} - Status: {self.status}"

    def get_patient_info(self):
        try:
            patient_url = f'https://patient-management-biotrack.herokuapp.com/api/patients/{self.patient_id}/' if os.getenv('DJANGO_ENV') == 'production' else f'http://127.0.0.1:8001/api/patients/{self.patient_id}/'
            response = requests.get(patient_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching patient data: {e}")
            return None

    def get_test_info(self):
        try:
            test_url = f'https://test-management-biotrack.herokuapp.com/api/test_results/{self.test_result.test_id}/' if os.getenv('DJANGO_ENV') == 'production' else f'http://localhost:8002/api/test_results/{self.test_result.test_id}/'
            response = requests.get(test_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching test data: {e}")
            return None

    def get_created_by_user_info(self):
        try:
            user_url = f'https://user-management-biotrack.herokuapp.com/api/users/{self.created_by_user_id}/' if os.getenv('DJANGO_ENV') == 'production' else f'http://127.0.0.1:8000/api/users/{self.created_by_user_id}/'
            response = requests.get(user_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching user data: {e}")
            return None

class ReportTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    template_content = models.JSONField()  # Assuming the template content is stored as JSON
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ReportAccessLog(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    accessed_by_user_id = models.CharField(max_length=100)  # Store the user_id instead of a ForeignKey
    accessed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report accessed by User {self.accessed_by_user_id} on {self.accessed_at}"

class TestResult(models.Model):
    test = models.CharField(max_length=100)  # Reference to the test name
    patient_id = models.CharField(max_length=100)  # Reference to patient ID
    date = models.DateTimeField(auto_now_add=True)
    details = models.JSONField()  # To store test result details as JSON

    def __str__(self):
        return f"Test Result for {self.patient_id} - {self.test} on {self.date}"
