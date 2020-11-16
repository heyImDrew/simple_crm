from django.contrib import admin
from django.urls import path
from companies.views import start_page, companies_page, partnerships_page
 
urlpatterns = [
    path('', start_page, name="start_page"),
    path('all/companies', companies_page, name="companies_page"),
    path('all/partnerships', partnerships_page, name="partnerships_page"),
]