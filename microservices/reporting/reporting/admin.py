from django.contrib import admin
from .models import Report, ReportTemplate, ReportAccessLog
import requests

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'get_created_by', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('patient_id',)

    def get_created_by(self, obj):
        user_info = obj.get_created_by_user_info()
        return f"{user_info.get('first_name', '')} {user_info.get('last_name', '')}" if user_info else 'Unknown'
    
    get_created_by.short_description = 'Created By'

class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

class ReportAccessLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'report', 'get_accessed_by', 'accessed_at')
    list_filter = ('accessed_at',)
    search_fields = ('report__patient_id',)

    def get_accessed_by(self, obj):
        user_info = obj.get_created_by_user_info()
        return f"{user_info.get('first_name', '')} {user_info.get('last_name', '')}" if user_info else 'Unknown'

    get_accessed_by.short_description = 'Accessed By'

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportTemplate, ReportTemplateAdmin)
admin.site.register(ReportAccessLog, ReportAccessLogAdmin)
