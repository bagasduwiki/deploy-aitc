from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class AdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['profile_pict']

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']
