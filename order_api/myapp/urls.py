from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name='home'),
    path("product/list/", views.ProductListApiView.as_view(), name="product_list"),
    path("product/info/<str:id>/", views.Product_RUDApiView.as_view(), name="info"),
    path("product/search/", views.ProductSearchListApiView.as_view(), name="search"),

    path("order/list/", views.orderList, name='order_list'),
    path("order/create/", views.createOrder, name="order_create"),





]