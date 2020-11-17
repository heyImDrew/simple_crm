from django.shortcuts import render
from employee.models import Employee

def employee_page(request):
    employees = Employee.objects.all()
    return render(request, "employee.html", {'employees':employees})

def add_employee(request):
    return render(request, "add_employee.html")