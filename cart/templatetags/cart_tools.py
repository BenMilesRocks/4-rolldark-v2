'''Tools for the cart page'''
from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    '''calculate subtotal for cart items'''
    return price * quantity

@register.simple_tag(name='campaign_subtotal')
def campaign_subtotal(price, dates, quantity):
    '''calculate subtotal for campaign tickets'''
    unit_price = float(price)
    total_dates = len(dates)
    number = float(quantity)
    result = (unit_price * total_dates) * number
    return f'{result:.2f}'

@register.filter(name='campaign_cost')
def campaign_cost(price, dates):
    '''calculate price for campaign tickets'''
    unit_price = float(price)
    total_dates = len(dates)
    result = unit_price * total_dates
    return f'{result:.2f}'
