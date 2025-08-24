'''Home forms.py'''
from django import forms

from products.widgets import CustomClearableFileInput
from .models import CallToAction


class ProductForm(forms.ModelForm):
    '''Allows products to be edited in the Products app, rather than in Admin'''

    class Meta: #pylint: disable=C0115
        model = CallToAction
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
