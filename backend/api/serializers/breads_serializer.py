from rest_framework import serializers

from api.models.breads import Bread


class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = (
            'id',
            'name',
        )
