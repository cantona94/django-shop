from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField()
    category = models.CharField(max_length=50)
    rating = models.IntegerField()
    availabilityToCart = models.IntegerField(blank=True)
