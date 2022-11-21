from rest_framework import serializers
from core.models import Address, Item, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_field = ["id"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        read_only_field = ["id"]


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        read_only_field = ["id"]
