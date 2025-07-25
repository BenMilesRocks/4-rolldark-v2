'''Cart app views'''
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from products.models import Product

def view_cart(request):
    '''Returns cart page'''
    return render(request, 'cart/cart.html')

def add_product_to_cart(request, item_id):
    '''Adds products to the cart'''

    # Fetch variables from page
    product = Product.objects.get(pk=item_id) #pylint: disable=E1101
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Checks for ticket options for games
    if product.game_dates:
        if request.POST.get(f'option_{product}') == 'campaign_ticket':
            ticket_option = 'campaign_ticket'
        else:
            ticket_option = request.POST.get(f'option_{product}')

    # If cart exists in session fetches it, else create empty cart
    cart = request.session.get('cart', {})

    # Check if product is a game
    if product.game_dates:
        # Check if already in cart
        if item_id in list(cart.keys()):
            # If in cart, check if ticket option in cart
            if ticket_option in cart[item_id]['game_by_ticket_option'].keys():
                # If in cart, increment quantity
                cart[item_id]['game_by_ticket_option'][ticket_option] += quantity
            else:
                # Else add ticket option to game ID
                cart[item_id]['game_by_ticket_option'][ticket_option] = quantity
        else:
            # If not, add new key to cart
            cart[item_id] = {'game_by_ticket_option': {ticket_option: quantity}}
            messages.success(request, f'Added {product.name} to your cart')

    # Otherwise just add to cart
    else:
        # Check if already in cart
        if item_id in list(cart.keys()):
            # If in cart, increment quantity
            cart[item_id] += quantity
        else:
            # If not, add new key to cart
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    # Pushes cart back to session
    request.session['cart'] = cart

    # Redirect to last page visited
    return redirect(redirect_url)
