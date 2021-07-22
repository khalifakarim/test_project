from rest_framework import serializers

from core.serializers.base import BaseSerializer

from provider.models import (
    ProviderAction,
    Manufacturer,
    Provider,
    CarPrice,
    Car,
)


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = Manufacturer


class CarSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = Car


class ProviderSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = Provider


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarPrice


class ProviderActionSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = ProviderAction
