from django.conf import settings
from django.core.mail import send_mail
from django.views import generic

from contact.forms.ContactForm import ContactForm


class ContactView(generic.FormView):
    template_name = 'contact/index.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        send_mail(
            subject="Hello",
            message="Baboon is loading...",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL]
        )
        return super().form_valid(form)