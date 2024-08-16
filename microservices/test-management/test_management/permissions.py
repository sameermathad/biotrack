import requests
from rest_framework.permissions import BasePermission
import os

class IsValidUser(BasePermission):
    def has_permission(self, request, view):
        print("Executing IsValidUser permission check")  # Debugging
        auth_header = request.headers.get('Authorization')
        print("Authorization header:", auth_header)  # Debugging

        if auth_header:
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                print("Token extracted:", token)  # Debugging

                # Determine the correct URL based on environment
                if os.getenv('DJANGO_ENV') == 'production':
                    validate_url = 'https://user-management-biotrack-b1763a64aa28.herokuapp.com/api/validate-user/'
                else:
                    validate_url = 'http://127.0.0.1:8000/api/validate-user/'

                response = requests.get(
                    validate_url,
                    headers={'Authorization': f'Bearer {token}'}
                )
                print("Token validation response status:", response.status_code)  # Debugging

                if response.status_code == 200:
                    print("Token validated successfully")
                    return True
                else:
                    print("Token validation failed with status:", response.status_code)
            else:
                print("Authorization header format is incorrect")
        else:
            print("Authorization header is missing")
        return False
