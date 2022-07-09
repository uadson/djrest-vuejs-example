from rest_framework import serializers

from api.models.meats import Meat


class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meat
        fields = (
            'id',
            'name',
        )
