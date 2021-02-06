from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off', 'readonly': 'readonly'}),
            'last_login': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off', 'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'date_joined': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off', 'readonly': 'readonly'}),
        }
        exclude = ['user_permissions', 'password', 'groups']