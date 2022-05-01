from django.shortcuts import render
from .forms import CreatepersonForm,CreatecompanyForm
from .models import works,lives
# Create your views here.


def insert(request):
    form = CreatepersonForm()
    
    form1 = CreatepersonForm(request.POST)
    if form1.is_valid():
        person_name = form1.cleaned_data["person_name"]
        company_name = form1.cleaned_data["company_name"]
        salary = form1.cleaned_data["salary"]
        street = form1.cleaned_data["street"]
        city = form1.cleaned_data["city"]
        works.objects.create(person_name = person_name, company_name = company_name,salary = salary)
        lives.objects.create(p_name = person_name, street = street,city = city)
    
    return render(request,'insert.html',{"form":form})

def display(request):
    form = CreatecompanyForm()
    form1 = CreatecompanyForm(request.POST)
    if form1.is_valid():
        company_name = form1.cleaned_data['company_name']
        company = works.objects.all().filter(company_name = company_name)
        employeeinfo=[]
        for e in company:
            employeeinfo.append(lives.objects.get(p_name=e.person_name))
        return render(request,'display.html',{"form":form,"employees":employeeinfo})
       
         
    return render(request,'display.html',{"form":form})

