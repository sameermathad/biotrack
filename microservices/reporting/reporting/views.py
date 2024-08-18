from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Report, ReportTemplate, ReportAccessLog, TestResult
from .serializers import ReportSerializer, ReportTemplateSerializer, ReportAccessLogSerializer
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer
from django.shortcuts import get_object_or_404

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def retrieve(self, request, *args, **kwargs):
        report = self.get_object()
        report_data = self.get_serializer(report).data
        
        # Fetching additional data
        patient_info = report.get_patient_info()
        test_info = report.get_test_info()
        created_by_user_info = report.get_created_by_user_info()

        if patient_info:
            report_data['patient_info'] = patient_info
        if test_info:
            report_data['test_info'] = test_info
        if created_by_user_info:
            report_data['created_by_user_info'] = created_by_user_info

        return Response(report_data)


class ReportTemplateViewSet(viewsets.ModelViewSet):
    queryset = ReportTemplate.objects.all()
    serializer_class = ReportTemplateSerializer

class ReportAccessLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReportAccessLog.objects.all()
    serializer_class = ReportAccessLogSerializer
