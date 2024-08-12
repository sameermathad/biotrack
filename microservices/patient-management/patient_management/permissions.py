import requests
from rest_framework.permissions import BasePermission

class IsValidUser(BasePermission):
    def has_permission(self, request, view):
        print("Executing IsValidUser permission check")  # Add this line to indicate execution
        auth_header = request.headers.get('Authorization')
        print("Authorization header:", auth_header)  # Add this line for debugging
        if auth_header:
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                print("Token extracted:", token)  # Add this line for debugging
                response = requests.get(
                    'http://127.0.0.1:8002/api/validate-user/',
                    headers={'Authorization': f'Bearer {token}'}
                )
                print("Token validation response status:", response.status_code)  # Add this line for debugging
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
