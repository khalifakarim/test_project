from rest_framework import serializers

from provider.models import (
    Manufacturer,
    Car,
    Provider,
    CarPrice,
    ProviderAction,
)


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = (
            'name',
            'description',
            'location',
            'foundation_time',
            'is_active',
        )


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'manufacturer',
            'model',
            'carcase',
            'state',
            'price',
            'is_active',
            'production_year',
            'type_of_engine',
            'horse_power',

        )


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'name',
            'description',
            'foundation_time',
            'cars',
            'customers',
            'is_active',
        )


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPrice
        fields = (
            'provider',
            'price',
            'car',
        )


class ProviderActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderAction
        fields = (
            'provider',
            'title',
            'description',
            'cars',
            'action_start_time',
            'action_end_time',
            'discount_percentage',
        )
