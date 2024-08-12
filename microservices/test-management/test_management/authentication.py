# patient_management/authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import requests

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        print("Authorization header:", auth_header)  # Debugging

        if not auth_header:
            return None  # No authentication header means DRF will move to the next authentication class or return 401

        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            raise exceptions.AuthenticationFailed('Invalid token header. No credentials provided.')

        token = parts[1]
        print("Token extracted:", token)  # Debugging

        # Validate the token with the user-management service
        response = requests.get(
            'http://127.0.0.1:8002/api/validate-user/',
            headers={'Authorization': f'Bearer {token}'}
        )

        print("Token validation response status:", response.status_code)  # Debugging

        if response.status_code != 200:
            raise exceptions.AuthenticationFailed('Invalid token.')

        user_data = response.json()
        user_id = user_data.get('id')
        if not user_id:
            raise exceptions.AuthenticationFailed('User not found.')

        # Here we don't need to fetch the User model, just return the user data
        return (user_data, None)
