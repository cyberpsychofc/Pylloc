from django import forms
from .models import User

class Preference(forms.ModelForm):
    class Meta:
        model = User
        fields = ['room1','room2','room3']
