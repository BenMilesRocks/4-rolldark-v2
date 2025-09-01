'''About forms.py'''
from django import forms

from products.widgets import CustomClearableFileInput
from .models import GameMaster


class GameMasterForm(forms.ModelForm):
    '''Allows GameMaster to be edited in the About app, rather than in Admin'''

    class Meta: #pylint: disable=C0115
        model = GameMaster
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
