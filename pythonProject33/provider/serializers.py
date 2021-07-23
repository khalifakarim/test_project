from rest_framework import serializers

from core.serializers.base import SoftDeleteSerializer
from core.serializers.base import BaseSerializer

from provider.models import (
    ProviderAction,
    Manufacturer,
    Provider,
    CarPrice,
    Car,
)


class ManufacturerSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = Manufacturer


class CarReadSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = Car


class CarCreateSerializer(SoftDeleteSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta(BaseSerializer.Meta):
        model = Car


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarPrice


class ProviderCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = Provider


class ProviderReadSerializer(serializers.ModelSerializer):
    cars = CarPriceSerializer(read_only=True, many=True)

    class Meta(BaseSerializer.Meta):
        model = Provider


class ProviderActionReadSerializer(serializers.ModelSerializer):
    provider = ProviderReadSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = ProviderAction


class ProviderActionCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = ProviderAction
