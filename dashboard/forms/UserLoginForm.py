from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-2'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg mb-2'})
    )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())
