'''Checkout app Apps.py'''
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    '''App config'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        from checkout import signals # pylint: disable=W0611, C0415
