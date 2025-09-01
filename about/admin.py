'''About app Admin'''
from django.contrib import admin

from .models import GameMaster


class GameMasterAdmin(admin.ModelAdmin):
    '''Admin class for GameMaster'''

    class Meta:
        '''Fixes the pluralisation on the Admin page, shows Categories instead of Categorys'''
        verbose_name_plural = 'Call To Action'

    list_display = (
        'name',
        'location',
        'image',
        'description',
    )

admin.site.register(GameMaster, GameMasterAdmin)
