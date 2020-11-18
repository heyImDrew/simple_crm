from django.shortcuts import render
from employee.models import Employee
from companies.models import Company
from .forms import EmployeeForm

def employee_page(request):
    employees = Employee.objects.all()
    return render(request, "employee.html", {'employees':employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.full_name = request.POST['full_name']
            employee.age = request.POST['age']
            employee.company = Company.objects.get(pk = int(request.POST['company']))
            employee.position = request.POST['position']
            employee.salary = request.POST['salary']
            employee.save()
        else:
            form = EmployeeForm()
        return render(request, "employee.html", {'employees':Employee.objects.all()})
    else:
        form = EmployeeForm()
        return render(request, "add_employee.html", {'form':form})

def delete_employee(request, pk):
    employee = Employee.objects.get(id = pk)
    employee.delete()
    return render(request, "employee.html", {'employees':Employee.objects.all()})