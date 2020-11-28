from django import forms
from blog.models import *


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-large', 'autocomplete': 'off'}),
            'content': forms.Textarea(attrs={'id': 'editor', 'rows': 15}),
            'excerpt': forms.Textarea(attrs={'class': 'textarea', 'rows': 5}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'rows': 10}),
        }
        fields = '__all__'
