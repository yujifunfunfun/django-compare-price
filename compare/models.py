from django.db import models

class Apparel(models.Model):
    images = models.ImageField(upload_to='')
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
