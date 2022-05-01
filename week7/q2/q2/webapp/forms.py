from django import forms

from .models import works,lives

class CreatepersonForm(forms.Form):
    person_name = forms.CharField()
    company_name = forms.CharField()
    salary = forms.IntegerField()
    street = forms.CharField()
    city = forms.CharField()
    

class CreatecompanyForm(forms.Form):
    company_name = forms.CharField()
    