from django.db import models

class Company(models.Model):
    SPECIALIZATION_CHOICES = tuple([(x,x) for x in (open('companies/choices/specializations.txt').read()).split('\n')])

    name = models.CharField(max_length = 255, unique=True, blank=False)
    description = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length = 255, choices = SPECIALIZATION_CHOICES)
    organization_date = models.DateField(blank=False)
    site = models.CharField(max_length = 255, blank=True, null=True)

    def __str__(self):
        return self.name

class Partnership(models.Model):
    PARTNERSHIP_CHOICES = tuple([(x,x) for x in (open('companies/choices/partnership_types.txt').read()).split('\n')])

    type = models.CharField(max_length = 255, choices=PARTNERSHIP_CHOICES, blank = False)
    companies = models.ManyToManyField('Company', blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return ', '.join([company.name for company in self.companies.all()]) + " partnership"