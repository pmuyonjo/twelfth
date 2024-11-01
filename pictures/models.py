from django.db import models

# Create your models here.
class Pictures(models.Model):
    name = models.CharField(max_length=255)
    banner = models.ImageField(default='', blank=True)