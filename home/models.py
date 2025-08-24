'''Home App models'''
from django.db import models

class CallToAction(models.Model):
    '''Call to action panes for carousel on index.html'''

    name = models.CharField(max_length=250)

    headline = models.CharField(max_length=50, null=True, blank=True)

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    description = models.CharField(max_length=250)
    dark_text = models.BooleanField(default=False)

    product_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.name)
