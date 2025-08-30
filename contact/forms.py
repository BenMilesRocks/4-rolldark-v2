'''Contact app forms'''

from django import forms


class ContactForm(forms.Form):
    '''Contact form'''
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    game_details = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Location | Number of Players | Online or in person | Time of Day | Weeknight or Weekday"} #pylint: disable=C0301
            )
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"Tell us about your group and the kind of story you'd love!"})
    )
