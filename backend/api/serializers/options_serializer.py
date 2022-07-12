from rest_framework import serializers

from api.models.options import Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            'id',
            'name',
        )
