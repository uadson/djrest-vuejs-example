from rest_framework import viewsets

from api.models.breads import Bread
from api.serializers.breads_serializer import BreadSerializer


class BreadsViewset(viewsets.ModelViewSet):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer
