

# Create your views here.
from django.shortcuts import render,redirect
from webapp.forms import LoginForm
from django.urls import reverse

def page1(request):
    username = 'not logged in'
    if (request.method == 'POST' and not(request.session.has_key('name'))) :
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            name = MyLoginForm.cleaned_data['name']
            roll_no=MyLoginForm.cleaned_data['roll_no']
            subject=MyLoginForm.cleaned_data['subject']

            request.session['name'] = name
            request.session['roll_no'] = roll_no
            request.session['subject'] = subject

            return render(request, 'home2.html',  {"name" : name,"roll_no" : roll_no,"subject" : subject})
    else:
        del request.session['name']
        MyLoginForm = LoginForm()
        return render(request,'home1.html',{"form":MyLoginForm})


def page2(request):

    if request.session.has_key('name'):
        name = request.session['username']
        roll_no = request.session['roll_no']
        subject = request.session['subject']

        return render(request, 'home2.html',  {"name" : name,"roll_no" : roll_no,"subject" : subject})
    else:
        MyLoginForm = LoginForm()
        return render(request,'home1.html',{"form":MyLoginForm}) 



def formView(request):
    
    
    if request.session.has_key('name'):
        name = request.session['name']
        roll_no = request.session['roll_no']
        subject = request.session['subject']
        return render(request, 'home2.html', {"name" : name,"roll_no" : roll_no,"subject" : subject})
    else:
        MyLoginForm = LoginForm()
        return render(request,'home1.html',{"form":MyLoginForm}) 


    






# Create your views here.
