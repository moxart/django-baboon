from django import forms

from dashboard.models import Category


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'description': forms.Textarea(attrs={'class': 'textarea form-control', 'rows': 3}),
        }
        fields = '__all__'
