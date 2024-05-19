from django.shortcuts import render
from .models import Product, Order, Store
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer, StoreSerializer, OrderSerializer
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,

)


class ProductListApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Product_RUDApiView(RetrieveUpdateDestroyAPIView,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class ProductSearchListApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'price', 'store_id__name__icontains']


@api_view(['GET'])
def orderList(request):
    order = Order.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 2
    page = paginator.paginate_queryset(order, request)
    serializer = OrderSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = Product.objects.get(id=serializer.data["product"])
        data.delete()
    print(serializer.data)
    return Response(serializer.data)





def home(request):
    data = Order.objects.get()

    data = data.product_set.all()
    for d in data:
        print(d.name)

    context = {"data": data}
    return render(request, "myapp/index.html", context)
