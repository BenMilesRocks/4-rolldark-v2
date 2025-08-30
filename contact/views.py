'''Contact app Views'''

from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from .forms import ContactForm


class SuccessView(TemplateView):
    '''Return message sent after form submission'''
    template_name = "message_sent.html"


class ContactView(FormView):
    '''Return view for Contact Us page'''
    form_class = ContactForm
    template_name = "contact_us.html"

    def get_success_url(self):
        return reverse("contact_us")

    def form_valid(self, form):
        # Use form.cleaned_data because we're getting the data direct from the form, not a model
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)
