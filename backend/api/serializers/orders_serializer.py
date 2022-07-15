from rest_framework import serializers

from api.models.orders import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'bread',
            'meat',
            'options',
            'status',
            'created',
            'updated',
        )
