'''Models for Checkout App'''
import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile
from rolldark.settings import DELIVERY_COST


class Order(models.Model):
    '''Order model. Creates order no, delivery details, delivery cost and grand total'''
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country (Please select from list)', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    # auto_now_add - adds current date and time to order automatically
    date = models.DateTimeField(auto_now_add=True)
    # Calculate delivery based on order total
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        '''Generate random, unique order no using UUID'''
        return uuid.uuid4().hex.upper()

    def update_total(self):
        '''
        Update Grand Total each time a line item is added,
        accounting for delivery costs
        '''

        # If line item deleted sets default to 0 not NONE, hence the 'or 0' line at the end
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0 # pylint: disable=E1101, C0301

        for item in self.lineitems.all(): # pylint: disable=E1101, C0301
            product = get_object_or_404(Product, pk=item.product.id)
            if product.delivery_charge:
                self.delivery_cost += Decimal(DELIVERY_COST) * Decimal(item.quantity)

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        '''
        Override original save method to set the Order No
        if not set already
        '''
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

# pylint: disable=C0301
class OrderLineItem(models.Model):
    '''Class for line item, allowing iteration through each item in the bag'''
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        '''
        Override original save method to set the lineitem total
        and update the order total
        '''

        self.lineitem_total = self.product.price * self.quantity # pylint: disable=E1101

        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}' # pylint: disable=E1101
