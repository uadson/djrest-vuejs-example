from rest_framework import viewsets

from api.models.options import Option
from api.serializers.options_serializer import OptionSerializer


class OptionsViewset(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
