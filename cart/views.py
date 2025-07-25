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

def adjust_cart(request, item_id):
    '''Amends the number of items in the cart'''

    # Fetch variables from page
    quantity = int(request.POST.get('quantity'))

    # Check for ticket options
    ticket_option = None
    if 'ticket_option' in request.POST:
        ticket_option = request.POST['ticket_option']

    # If cart exists in session fetches it, else create empty cart
    cart = request.session.get('cart', {})

    # Check if product being altered has a ticket option
    if ticket_option:

        if quantity > 0:
            # If items left in cart, update quantity
            cart[item_id]['game_by_ticket_option'][ticket_option] = quantity
        else:
            # If quantity == 0, delete item
            del cart[item_id]['game_by_ticket_option'][ticket_option]

            # If no other tickets for this game exist, delete item_id from cart
            if not cart[item_id]['game_by_ticket_option']:
                cart.pop(item_id)

    else:
        # Update quantity
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    # Pushes cart back to session
    request.session['cart'] = cart

    # Redirect to last page visited
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    '''Deletes item from cart'''

    try:
        # Check for ticket options
        ticket_option = None
        if 'ticket_option' in request.POST:
            ticket_option = request.POST['ticket_option']

        # If cart exists in session fetches it, else create empty cart
        cart = request.session.get('cart', {})

        if ticket_option:
            del cart[item_id]['game_by_ticket_option'][ticket_option]
            # If no other tickets for this game exist, delete item_id from cart
            if not cart[item_id]['game_by_ticket_option']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        # Pushes cart back to session
        request.session['cart'] = cart

        # Redirect to last page visited
        return HttpResponse(status=200)

    except Exception as e: #pylint: disable=W0612,W0718
        return HttpResponse(status=500)
