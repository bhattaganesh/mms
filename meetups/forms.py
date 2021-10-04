from django import forms
from django.forms import fields
from .models import Participant

class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Your Email:")
        