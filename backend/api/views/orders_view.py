from rest_framework import viewsets

from api.models.order import Order
from api.serializers.orders_serializer import OrderSerializer


class OrdersViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
