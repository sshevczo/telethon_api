from django import forms
from .models import TelethonClient

class LoginForm(forms.Form):
    
    class Meta:
        model = TelethonClient