from django.db import models

class Apparel(models.Model):
    images = models.ImageField(upload_to='')
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    shop = models.CharField(max_length=20)

class Favorite(models.Model):
    user_id = models.CharField(max_length=5)
    item_id = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    shop = models.CharField(max_length=20)
