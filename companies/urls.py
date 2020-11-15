from django.contrib import admin
from django.urls import path
from companies.views import start_page
 
urlpatterns = [
    path('', start_page),
]