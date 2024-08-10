import requests

def get_patient_details(patient_id):
    response = requests.get(f'http://localhost:8001/api/patients/{patient_id}/')  # Update URL accordingly
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()  # Raise an exception if the request failed
