from django.db import migrations, IntegrityError, transaction

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
        Role.objects.get_or_create(name=role['name'], defaults={'description': role['description']})


def create_permissions(apps, schema_editor):
    Permission = apps.get_model('user_management', 'Permission')

    permissions = [
        {"name": "Create/Update Patient Record", "codename": "create_update_patient_record"},
        {"name": "Schedule/Cancel Appointments", "codename": "schedule_cancel_appointments"},
        {"name": "Check-In Patients", "codename": "check_in_patients"},
        {"name": "View Daily Schedule", "codename": "view_daily_schedule"},
        {"name": "View Patient Record", "codename": "view_patient_record"},
        {"name": "Create/Update Test Orders", "codename": "create_update_test_orders"},
        {"name": "Review Test Results", "codename": "review_test_results"},
        {"name": "Generate Test Report", "codename": "generate_test_report"},
        {"name": "Issue Prescriptions", "codename": "issue_prescriptions"},
        {"name": "Manage Appointments", "codename": "manage_appointments"},
        {"name": "View Test Orders", "codename": "view_test_orders"},
        {"name": "Manage Samples", "codename": "manage_samples"},
        {"name": "Input Test Results", "codename": "input_test_results"},
        {"name": "Generate Preliminary Test Data", "codename": "generate_preliminary_test_data"},
        {"name": "Manage Users/Roles", "codename": "manage_users_roles"},
        {"name": "View/Generate Reports", "codename": "view_generate_reports"},
        {"name": "System Management", "codename": "system_management"},
        {"name": "Oversee Billing", "codename": "oversee_billing"},
        {"name": "Generate/Update Invoices", "codename": "generate_update_invoices"},
        {"name": "Process Payments", "codename": "process_payments"},
        {"name": "Insurance Management", "codename": "insurance_management"},
        {"name": "Manage Patient Care", "codename": "manage_patient_care"},
        {"name": "Administer Medications", "codename": "administer_medications"},
        {"name": "Access Test Reports", "codename": "access_test_reports"},
        {"name": "Task Managements", "codename": "task_management"},
        {"name": "Patient Manage Appointments", "codename": "patient_manage_appointments"},
        {"name": "Patient Access Test Reports", "codename": "patient_access_test_reports"},
        {"name": "Patient Health Records", "codename": "patient_health_records"},
        {"name": "Patient Billing and Payments", "codename": "patient_billing_payments"},
        {"name": "Manage Prescriptions", "codename": "manage_prescriptions"},
        {"name": "Manage Inventory", "codename": "manage_inventory"},
        {"name": "Patient Interaction", "codename": "patient_interaction"},
        {"name": "Monitor Clinic Operations", "codename": "monitor_clinic_operations"},
        {"name": "Generate/Review Reports", "codename": "generate_review_reports"},
        {"name": "Staff Scheduling", "codename": "staff_scheduling"},
    ]

    for perm in permissions:
        Permission.objects.get_or_create(
            codename=perm['codename'],
            defaults={'name': perm['name']}
        )


def assign_permissions_to_roles(apps, schema_editor):
    Role = apps.get_model('user_management', 'Role')
    Permission = apps.get_model('user_management', 'Permission')
    RolePermission = apps.get_model('user_management', 'RolePermission')

    role_permissions_map = {
        "Receptionist": ["create_update_patient_record", "schedule_cancel_appointments", "check_in_patients", "view_daily_schedule"],
        "Doctor": ["view_patient_record", "create_update_test_orders", "review_test_results", "generate_test_report", "issue_prescriptions", "manage_appointments"],
        "Lab Technician": ["view_test_orders", "manage_samples", "input_test_results", "generate_preliminary_test_data"],
        "Administrator": ["manage_users_roles", "view_generate_reports", "system_management", "oversee_billing"],
        "Billing Clerk": ["generate_update_invoices", "process_payments", "insurance_management"],
        "Nurse": ["manage_patient_care", "administer_medications", "access_test_reports", "task_management"],
        "Patient": ["patient_manage_appointments", "patient_access_test_reports", "patient_health_records", "patient_billing_payments"],
        "Pharmacist": ["manage_prescriptions", "manage_inventory", "patient_interaction"],
        "Clinic Manager": ["monitor_clinic_operations", "generate_review_reports", "staff_scheduling"],
    }

    for role_name, perm_codenames in role_permissions_map.items():
        role = Role.objects.get(name=role_name)
        for codename in perm_codenames:
            try:
                permission = Permission.objects.get(codename=codename)
                RolePermission.objects.get_or_create(role=role, permission=permission)
            except Permission.DoesNotExist:
                print(f"Permission {codename} does not exist.")


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_roles),
        migrations.RunPython(create_permissions),
        migrations.RunPython(assign_permissions_to_roles),
    ]
