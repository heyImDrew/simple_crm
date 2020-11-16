from django.contrib import admin
from django.urls import path
from employee.views import employee_page
 
urlpatterns = [
    path('all/employee', employee_page, name="employee_page"),
]