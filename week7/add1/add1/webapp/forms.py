from django import forms
from .models import human

class createhuman(forms.ModelForm):
    class Meta:
       model = human
       fields = ['firstname','lastname','phone','address','city']

