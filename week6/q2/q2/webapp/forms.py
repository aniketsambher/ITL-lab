
from django import forms



class LoginForm(forms.Form):
    
    name = forms.CharField(max_length=100)
    roll_no = forms.IntegerField() 
    subject = forms.ChoiceField(choices=[("maths","maths"),("science","science")],label="Manufacturer")
    
