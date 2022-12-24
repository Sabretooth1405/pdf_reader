from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Custom user register field to take only neccsary info

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
