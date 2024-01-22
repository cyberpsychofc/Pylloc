from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Room

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}), max_length=50,required=True,help_text="Required")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}),max_length=100,required=True,help_text="Required. Provide a valid email")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),max_length=150,required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),max_length=150,required=True)

class AddRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('num','year')

    last_room_entry = list(Room.objects.filter(user_id__isnull=True).order_by('num').desc())        
    #ROOM_CHOICES = {last_room_entry : pass}        
    YEAR_CHOICES = {'1':"First Year", '2':"Second Year", '3':"Third Year", '4':"Fourth Year" }
