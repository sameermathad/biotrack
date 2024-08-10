from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet, TestResultViewSet, ResultDetailViewSet, ParameterViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'parameters', ParameterViewSet)
router.register(r'tests', TestViewSet)
router.register(r'test_results', TestResultViewSet)
router.register(r'result_details', ResultDetailViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
