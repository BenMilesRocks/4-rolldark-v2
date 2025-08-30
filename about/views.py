'''About app views'''
from django.shortcuts import render

from .models import GameMaster

def about(request):
    """View to return about page"""

    game_masters = GameMaster.objects.all() # pylint: disable=E1101

    context = {
        'game_masters': game_masters,
    }

    return render(request, 'about/about.html', context)
