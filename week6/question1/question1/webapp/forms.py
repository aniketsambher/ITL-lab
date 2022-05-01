from django import forms



class LoginForm(forms.Form):
    
    manufacturer = forms.ChoiceField(choices=[("Hyundai","Hyundai"),("Mercedes-Benz","Mercedes-Benz"),("McLaren","McLaren"),("BMW","BMW")],label="Manufacturer")
    username = forms.CharField(max_length=100)
