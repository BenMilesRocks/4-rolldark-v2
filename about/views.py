'''About app views'''
from django.shortcuts import render, redirect, get_object_or_404
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

    template = 'about/add_gm.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_gm(request, gm_id):
    '''Edit a call to action in the carousel'''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    gm = get_object_or_404(GameMaster, pk=gm_id)
    if request.method == 'POST':
        form = GameMasterForm(request.POST, request.FILES, instance=gm)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = GameMasterForm(instance=gm)
        messages.info(request, f"You are editing {gm.name}'s profile")

    template = 'about/edit_gm.html'
    context = {
        'form': form,
        'gm': gm,
    }

    return render(request, template, context)
