from django.shortcuts import render

def employee_page(request):
    return render(request, "employee.html")