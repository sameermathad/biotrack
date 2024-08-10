from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Parameter(models.Model):
    name = models.CharField(max_length=100)
    units = models.CharField(max_length=50, null=True, blank=True)
    reference_interval = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='parameters')

    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    parameters = models.ManyToManyField(Parameter)

    def __str__(self):
        return self.name

class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    patient_id = models.CharField(max_length=100)  # Reference to patient ID
    date = models.DateTimeField(auto_now_add=True)

class ResultDetail(models.Model):
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name='details')
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, null=True, blank=True)
    result = models.CharField(max_length=100)
    units = models.CharField(max_length=50, null=True, blank=True)
    reference_interval = models.CharField(max_length=100, null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
