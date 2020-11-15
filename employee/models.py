from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Employee(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    age = models.PositiveIntegerField(blank = False, validators=[MinValueValidator(16), MaxValueValidator(100)])
    company = models.ForeignKey('companies.Company', on_delete = models.CASCADE)
    position = models.CharField(max_length=255, blank=False)
    salary = models.IntegerField(blank=True, null=False, default=0)

    def __str__(self):
        return self.full_name + " at " + self.company.name