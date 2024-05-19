from django.db import models
from django.contrib.auth.admin import User



class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.TextField(null=False, blank=False)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=12)
    total_items = models.IntegerField(null=True)

    def __str__(self):
        return self.phone