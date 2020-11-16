from django.shortcuts import render

def start_page(request):
    return render(request, "index.html")

def companies_page(request):
    return render(request, "companies.html")

def partnerships_page(request):
    return render(request, "partnerships.html")