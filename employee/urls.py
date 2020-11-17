from django.contrib import admin
from django.urls import path
from employee.views import employee_page, add_employee
 
urlpatterns = [
    path('all/employee', employee_page, name="employee_page"),
    path('all/employee/add', add_employee, name="add_employee"),
]