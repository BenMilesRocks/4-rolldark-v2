'''About app views'''
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import GameMaster
from .forms import GameMasterForm

def about(request):
    """View to return about page"""

    game_masters = GameMaster.objects.all() # pylint: disable=E1101

    context = {
        'game_masters': game_masters,
    }

    return render(request, 'about/about.html', context)

@login_required
def add_gm(request):
    '''Add a Call to Action to the home page'''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GameMasterForm(request.POST, request.FILES)
        if form.is_valid():
            game_master = form.save() # pylint: disable=W0612
            messages.success(request, f'Successfully added { game_master.name } to Game Masters!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add Game Master. Please ensure the form is valid.')
    else:
        form = GameMasterForm()

    template = 'home/add_call_to_action.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
