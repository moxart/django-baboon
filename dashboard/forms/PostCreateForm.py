from django import forms

from dashboard.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control form-control-lg', 'style': 'width: 150px'}),
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'content': forms.Textarea(attrs={'id': 'editor', 'rows': 15}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'tags': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'class': 'textarea form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control form-control-lg', 'style': 'width: 150px'}),
        }
        fields = '__all__'
