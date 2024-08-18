from rest_framework import serializers
from .models import Report, ReportTemplate, ReportAccessLog

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ReportTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportTemplate
        fields = '__all__'

class ReportAccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportAccessLog
        fields = '__all__'
