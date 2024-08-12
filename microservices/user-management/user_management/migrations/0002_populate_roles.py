from django.db import migrations


def populate_roles(apps, schema_editor):
    Role = apps.get_model('user_management', 'Role')
    roles = [
        {"name": "Receptionist", "description": "Manages appointments and patient registrations."},
        {"name": "Doctor", "description": "Accesses patient records and manages treatments."},
        {"name": "Lab Technician", "description": "Handles test management and results processing."},
        {"name": "Administrator", "description": "Manages users, roles, and system settings."},
        {"name": "Billing Clerk", "description": "Handles billing and payment processing."},
        {"name": "Nurse", "description": "Manages patient care and tasks."},
        {"name": "Patient", "description": "Views personal health records and manages appointments."},
        {"name": "Pharmacist", "description": "Manages prescriptions and inventory."},
        {"name": "Clinic Manager", "description": "Oversees clinic operations and staff management."},
    ]
    for role in roles:
        Role.objects.create(**role)


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_roles),
    ]
