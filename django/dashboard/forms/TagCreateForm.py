from django import forms

from dashboard.models import Tag


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
            'description': forms.Textarea(attrs={'class': 'textarea form-control', 'rows': 3}),
        }
        fields = '__all__'
        labels = {
            'title': 'عنوان',
            'description': 'توضیحات'
        }