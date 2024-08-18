# authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import requests
import os

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

        # Determine the correct URL based on environment
        if os.getenv('DJANGO_ENV') == 'production':
            validate_url = 'https://user-management-biotrack-b1763a64aa28.herokuapp.com/api/validate-user/'
        else:
            validate_url = 'http://127.0.0.1:8000/api/validate-user/'

        # Validate the token with the user-management service
        response = requests.get(
            validate_url,
            headers={'Authorization': f'Bearer {token}'}
        )

        print("Token validation response status:", response.status_code)  # Debugging

        if response.status_code != 200:
            raise exceptions.AuthenticationFailed('Invalid token.')

        user_data = response.json()
        user_id = user_data.get('id')
        if not user_id:
            raise exceptions.AuthenticationFailed('User not found.')

        return (user_data, None)
