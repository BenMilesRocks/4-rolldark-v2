"""Home app views"""
from django.shortcuts import render, redirect
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
