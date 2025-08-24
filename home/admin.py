'''Home App admin.py'''
from django.contrib import admin

from .models import CallToAction

class CallToActionAdmin(admin.ModelAdmin):
    '''Admin class for CallToAction'''

    class Meta:
        '''Fixes the pluralisation on the Admin page, shows Categories instead of Categorys'''
        verbose_name_plural = 'Call To Action'

    list_display = (
        'name',
        'headline',
        'image',
        'description',
        'dark_text'
    )

admin.site.register(CallToAction, CallToActionAdmin)
