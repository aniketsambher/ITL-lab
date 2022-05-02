from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import human
from .forms import createhuman


def insert(request):
    
    context={}
    form=createhuman()
    form1=createhuman(request.POST )
    if form1.is_valid():
        firstname = form1.cleaned_data["firstname"]
        lastname = form1.cleaned_data["lastname"]
        phone = form1.cleaned_data["phone"]
        address = form1.cleaned_data["address"]
        city = form1.cleaned_data["city"]
        human.objects.create(firstname = firstname, lastname = lastname,phone = phone,address=address,city=city)
    context['form']=form
    return render(request,'insert.html',context);


def display(request):
    context={}

    selected_person=None
    persons=human.objects.all()
    details=None

    if request.method == "POST":
        selected_person=request.POST.get("name")
        print(selected_person)
        details=human.objects.get(firstname=selected_person)
        #print(details.address)
        #print(details.phone)
    context ={
        "names":persons,
        "selected_name":selected_person,
        "details":details
                
    }

    return render(request, 'display.html', context)

def update_view(request,id):

    context ={}
    
    obj = get_object_or_404(human, firstname = id)
    # pass the object as instance in form
    form = createhuman(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/display")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update.html", context)



def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(human, firstname = id)
    # delete object
    obj.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("/insert")
 
    
