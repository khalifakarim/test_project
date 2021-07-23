from rest_framework import serializers

from core.serializers.base import BaseSerializer
from provider.models import CarPrice


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarPrice
