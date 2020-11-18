from django import forms
from .models import Company, Partnership

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class PartnershipForm(forms.ModelForm):
    class Meta:
        model = Partnership
        fields = "__all__"