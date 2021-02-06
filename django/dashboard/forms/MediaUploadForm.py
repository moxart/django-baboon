from django import forms

from dashboard.models import Media


class MediaUploadNewForm(forms.ModelForm):
    class Meta:
        model = Media
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off'}),
        }
        fields = '__all__'
