'''About app models'''
from django.db import models

class GameMaster(models.Model):
    '''Game Master profiles, allowing for dynamic creation of GM cards on about.html'''

    name = models.CharField(max_length=250)

    location = models.CharField(max_length=50, null=False, blank=False)

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    description = models.TextField(max_length=1500, null=False, blank=False)

    def __str__(self):
        return str(self.name)
