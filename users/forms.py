from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms import fields, widgets
from .models import Contact
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'username', 'email','password1', 'password2']        

class ContactUs(forms.ModelForm):
    
    
    class Meta:
        model=Contact
        fields=['username','Phone_no','email_id','Message']
        widgets= {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'Phone_no': forms.TextInput(attrs={'class':'form-control'}),
            'email_id': forms.TextInput(attrs={'class':'form-control'}),
            'Message': forms.TextInput(attrs={'class':'form-control'}),

        }



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']        