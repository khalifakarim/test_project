from rest_framework import serializers

from provider.api.v1.serializers.car_price import CarPriceSerializer
from core.serializers.base import SoftDeleteSerializer
from core.serializers.base import BaseSerializer
from provider.models import Provider


class ProviderCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = Provider


class ProviderReadSerializer(serializers.ModelSerializer):
    cars = CarPriceSerializer(read_only=True, many=True)

    class Meta(BaseSerializer.Meta):
        model = Provider
