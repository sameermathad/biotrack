#!/bin/bash

# Setup script for initial setup
echo "Setting up the project..."

# Install dependencies
pip install -r microservices/patient-management/requirements.txt

# Run migrations
python microservices/patient-management/manage.py migrate

# Collect static files
python microservices/patient-management/manage.py collectstatic --noinput
