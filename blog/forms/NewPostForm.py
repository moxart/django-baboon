from django import forms
from blog.models import *


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control form-control-lg', 'style': 'width: 150px'}),
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'content': forms.Textarea(attrs={'id': 'editor', 'rows': 15}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control form-control-lg', 'style': 'width: 150px'}),
            'description': forms.Textarea(attrs={'class': 'textarea form-control', 'rows': 10}),
            'status': forms.Select(attrs={'class': 'form-control form-control-lg', 'style': 'width: 150px'}),
        }
        fields = '__all__'
