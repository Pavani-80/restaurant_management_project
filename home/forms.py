from django import forms 
from .models import contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailFIeld(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
   
