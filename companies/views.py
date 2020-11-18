from django.shortcuts import render
from companies.models import Company, Partnership
from .forms import CompanyForm, PartnershipForm
import re

def start_page(request):
    return render(request, "index.html")

def companies_page(request):
    companies = Company.objects.all()
    return render(request, "companies.html", {'companies':companies})

def partnerships_page(request):
    partnerships = Partnership.objects.all()
    return render(request, "partnerships.html", {'partnerships':partnerships})

def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            if re.match(r'\d{4}-\d{2}-\d{2}', request.POST['organization_date']):
                company = form.save()
                company.name = request.POST['name']
                company.description = request.POST['description']
                company.specialization = request.POST['specialization']
                company.organization_date = request.POST['organization_date']
                company.site = request.POST['site']
                company.save()
        return render(request, "companies.html", {'companies':Company.objects.all()})
    else:
        form = CompanyForm()
        return render(request, "add_company.html", {'form':form})

def add_partnership(request):
    if request.method == 'POST':
        form = PartnershipForm(request.POST)
        if form.is_valid():
            partnership = form.save()
            partnership.type = request.POST['type']
            partnership.companies.set = request.POST['companies']
            partnership.description = request.POST['description']
            partnership.save()
        return render(request, "partnerships.html", {'partnerships':Partnership.objects.all()})
    else:
        form = PartnershipForm()
        return render(request, "add_partnership.html", {'form':form})

def delete_company(request, pk):
    company = Company.objects.get(id = pk)
    company.delete()
    return render(request, "companies.html", {'companies':Company.objects.all()})

def delete_partnerships(request, pk):
    partnership = Partnership.objects.get(id = pk)
    partnership.delete()
    return render(request, "partnerships.html", {'partnerships':Partnership.objects.all()})