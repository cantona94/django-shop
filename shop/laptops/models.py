from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField()
    category = models.CharField(max_length=50)
    rating = models.IntegerField()
    availabilityToCart = models.IntegerField(blank=True)


class Order(models.Model):
    orderedProducts = models.TextField()
    quantityProducts = models.IntegerField()
    amountOfOrders = models.IntegerField()
    orderTime = models.DateTimeField(auto_now_add=True)
    shoppingCity = models.CharField(max_length=255)
