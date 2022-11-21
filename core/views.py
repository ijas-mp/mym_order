from django.shortcuts import render
from rest_framework import viewsets
from core.models import Item, Address, Order
from core.serializers import ItemSerializers, OrderSerializer, AddressSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("id")
    serializer_class = ItemSerializers
    http_method_names = ["get", "post", "put", "delete"]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by("id")
    serializer_class = AddressSerializer
    http_method_names = ["get", "post", "put", "delete"]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer
    http_method_names = ["get", "post", "put", "delete"]
