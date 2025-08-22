'''Cart app contexts'''
from decimal import Decimal
from django.shortcuts import get_object_or_404

from rolldark.settings import DELIVERY_COST
from products.models import Product

def cart_contents(request):
    '''Show content of cart'''

    cart_items = []
    total = 0
    product_count = 0
    delivery = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():

        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

        else:
            product = get_object_or_404(Product, pk=item_id)
            for option, quantity in item_data['game_by_ticket_option'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'option': option,
                })

        if product.delivery_charge:
            delivery = Decimal(DELIVERY_COST) * Decimal(item_data)

    grand_total = float(delivery) + float(total)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
