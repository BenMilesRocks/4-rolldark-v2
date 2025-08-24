"""Home app views"""
from django.shortcuts import render

from .models import CallToAction

def index(request):
    """View to return index page"""

    call_to_action = CallToAction.objects.all() # pylint: disable=E1101

    context = {
        'call_to_action': call_to_action,
    }

    return render(request, 'home/index.html', context)
