from django.contrib import admin
from .models import Test, TestResult, ResultDetail, Parameter, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'reference_interval', 'category')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    filter_horizontal = ('parameters',)

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('test', 'patient_id', 'date')

@admin.register(ResultDetail)
class ResultDetailAdmin(admin.ModelAdmin):
    list_display = ('test_result', 'parameter', 'result', 'method')
