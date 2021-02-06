from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
        fields = '__all__'

