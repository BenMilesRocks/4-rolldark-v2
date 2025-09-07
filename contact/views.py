'''Contact app Views'''

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import ContactForm


class SuccessView(TemplateView):
    '''Return message sent after form submission'''
    template_name = "contact/success.html"


class ContactView(FormView):
    '''Return view for Contact Us page'''
    form_class = ContactForm
    template_name = "contact/contact_us.html"

    def form_valid(self, form):
        # Use form.cleaned_data because we're getting the data direct from the form, not a model
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        game_details = form.cleaned_data.get("game_details")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {name}, {email}
            ________________________

            Game info:
            {game_details}

            Message:
            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return render(self.request, "contact/success.html")
