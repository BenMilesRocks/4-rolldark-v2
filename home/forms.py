'''Home forms.py'''
from django import forms

from products.widgets import CustomClearableFileInput
from .models import CallToAction


class CallToActionForm(forms.ModelForm):
    '''Allows CallToAction to be edited in the Home app, rather than in Admin'''

    class Meta:
        '''Call to action meta'''
        model = CallToAction
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
