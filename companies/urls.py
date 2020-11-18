from django.contrib import admin
from django.urls import path
from companies.views import start_page, companies_page, partnerships_page, add_company, add_partnership, delete_company, delete_partnerships
 
urlpatterns = [
    path('', start_page, name="start_page"),
    path('all/companies', companies_page, name="companies_page"),
    path('all/partnerships', partnerships_page, name="partnerships_page"),
    path('all/companies/add', add_company, name="add_company"),
    path('all/partnerships/add', add_partnership, name="add_partnership"),
    path('all/companies/delete/<int:pk>', delete_company, name="delete_company"),
    path('all/partnerships/delete/<int:pk>', delete_partnerships, name="delete_partnership"),
]