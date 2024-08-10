from rest_framework.test import APITestCase
from rest_framework import status
from .models import Test, TestResult

class TestManagementTests(APITestCase):
    
    def test_create_test(self):
        data = {'name': 'Blood Test', 'description': 'A test for blood analysis', 'price': '50.00'}
        response = self.client.post('/api/tests/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_test_result(self):
        test = Test.objects.create(name='Blood Test', description='A test for blood analysis', price='50.00')
        patient = Patient.objects.create(first_name='John', last_name='Doe', date_of_birth='1990-01-01', gender='Male', phone_number='1234567890', email='john.doe@example.com')
        data = {'test': test.id, 'patient': patient.id, 'result': 'Normal', 'date': '2024-08-10T10:00:00Z'}
        response = self.client.post('/api/test_results/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
