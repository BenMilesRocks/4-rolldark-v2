'''Products forms.py'''
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    '''Allows products to be edited in the Products app, rather than in Admin'''

    class Meta: #pylint: disable=C0115
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all() #pylint: disable=E1101
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
