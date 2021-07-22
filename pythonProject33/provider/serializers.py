from rest_framework import serializers

from provider.models import (
    ProviderAction,
    Manufacturer,
    Provider,
    CarPrice,
    Car,
)


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = ('creation_time', 'modification_time')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('creation_time', 'modification_time')


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        exclude = ('creation_time', 'modification_time')


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPrice
        exclude = ('creation_time', 'modification_time')


class ProviderActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderAction
        exclude = ('creation_time', 'modification_time')
