from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}), max_length=50,required=True,help_text="Required")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}),max_length=100,required=True,help_text="Required. Provide a valid email")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),max_length=150,required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),max_length=150,required=True)