from rest_framework import viewsets
from employee.models import Employee
from companies.models import Company, Partnership
from .serializers import EmployeeSerializer, CompanySerializer, PartnershipSerializer
from django_filters import rest_framework as filters

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('full_name', 'company', 'position')

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('name', 'specialization')

class PartnershipViewSet(viewsets.ModelViewSet):
    serializer_class = PartnershipSerializer
    queryset = Partnership.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('type', 'companies')