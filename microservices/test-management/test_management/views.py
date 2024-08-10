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

class ResultDetailViewSet(viewsets.ModelViewSet):
    queryset = ResultDetail.objects.all()
    serializer_class = ResultDetailSerializer
