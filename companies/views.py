from django.shortcuts import render
from companies.models import Company, Partnership

def start_page(request):
    return render(request, "index.html")

def companies_page(request):
    companies = Company.objects.all()
    return render(request, "companies.html", {'companies':companies})

def partnerships_page(request):
    partnerships = Partnership.objects.all()
    return render(request, "partnerships.html", {'partnerships':partnerships})

def add_company(request):
    return render(request, "add_company.html")

def add_partnership(request):
    return render(request, "add_partnership.html")