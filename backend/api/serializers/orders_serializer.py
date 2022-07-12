from rest_framework import serializers

from api.models.order import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'bread',
            'meat',
            'status',
        )
