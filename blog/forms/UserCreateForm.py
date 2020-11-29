from django import forms
from django.contrib.auth.models import User
from blog.models import *


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'password': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'user_permissions': forms.Select(attrs={'multiple': '', 'class': 'form-control form-control-lg'}),
        }
        exclude = ['first_name', 'last_name', 'last_login', 'groups', 'date_joined']
