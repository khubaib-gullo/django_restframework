from django.contrib import admin

from .models import Product, Store, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Order)