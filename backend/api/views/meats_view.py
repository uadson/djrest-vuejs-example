from rest_framework import viewsets

from api.models.meats import Meat
from api.serializers.meats_serializer import MeatSerializer


class MeatsViewset(viewsets.ModelViewSet):
    queryset = Meat.objects.all()
    serializer_class = MeatSerializer
