"""Home app views"""
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CallToAction
from .forms import CallToActionForm

def index(request):
    """View to return index page"""

    call_to_action = CallToAction.objects.all() # pylint: disable=E1101

    context = {
        'call_to_action': call_to_action,
    }

    return render(request, 'home/index.html', context)

@login_required
def view_all_actions(request):
    """View to return all call to actions for editing"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    call_to_action = CallToAction.objects.all() # pylint: disable=E1101

    context = {
        'call_to_action': call_to_action,
    }

    return render(request, 'home/view_all_actions.html', context)

@login_required
def add_call_to_action(request):
    '''Add a Call to Action to the home page'''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CallToActionForm(request.POST, request.FILES)
        if form.is_valid():
            call_to_action = form.save() # pylint: disable=W0612
            messages.success(request, 'Successfully added Call to Action!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = CallToActionForm()

    template = 'home/add_call_to_action.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_call_to_action(request, call_to_action_id):
    '''Edit a call to action in the carousel'''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    call_to_action = get_object_or_404(CallToAction, pk=call_to_action_id)
    if request.method == 'POST':
        form = CallToActionForm(request.POST, request.FILES, instance=call_to_action)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = CallToActionForm(instance=call_to_action)
        messages.info(request, f'You are editing {call_to_action.name}')

    template = 'home/edit_call_to_action.html'
    context = {
        'form': form,
        'call_to_action': call_to_action,
    }

    return render(request, template, context)

@login_required
def delete_call_to_action(request, call_to_action_id):
    '''Delete a product from the store'''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    call_to_action = get_object_or_404(CallToAction, pk=call_to_action_id)
    call_to_action.delete()
    messages.success(request, 'call_to_action deleted!')
    return redirect(reverse('home'))
