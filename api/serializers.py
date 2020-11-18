from rest_framework import serializers
from employee.models import Employee
from companies.models import Company, Partnership

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class PartnershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'