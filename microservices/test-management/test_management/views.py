from rest_framework import viewsets
from .models import Test, TestResult, ResultDetail, Parameter, Category
from .serializers import TestSerializer, TestResultSerializer, ResultDetailSerializer, ParameterSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

    def get_queryset(self):
        # Get the 'patient_id' from query params
        patient_id = self.request.query_params.get('patient_id', None)
        queryset = TestResult.objects.all()

        # Filter queryset by patient_id if provided
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)

        return queryset

class ResultDetailViewSet(viewsets.ModelViewSet):
    queryset = ResultDetail.objects.all()
    serializer_class = ResultDetailSerializer
