from django.shortcuts import render
from webapp.forms import LoginForm

def page1(request):
    username = 'not logged in'
    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            manufacturer=MyLoginForm.cleaned_data['manufacturer']
            return render(request, 'submitted.html', {"username" : username,"manufacturer": manufacturer})
    else:
        MyLoginForm = LoginForm()
        return render(request,'home.html',{"form":MyLoginForm})
    






# Create your views here.
