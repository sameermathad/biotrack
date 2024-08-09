from django.contrib import admin
from .models import Address, Patient, MedicalHistory, Appointment

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'city', 'state', 'postal_code', 'country')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date_of_birth', 'email', 'registration_date')
    search_fields = ('first_name', 'last_name', 'email')

class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'condition', 'date_diagnosed')
    search_fields = ('condition',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'reason')
    search_fields = ('patient', 'reason')

admin.site.register(Address, AddressAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(MedicalHistory, MedicalHistoryAdmin)
admin.site.register(Appointment, AppointmentAdmin)
