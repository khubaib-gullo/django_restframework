from rest_framework import serializers
from .models import Order, Product, Store


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"





