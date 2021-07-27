from rest_framework import serializers

from client.api.v1.serializers.customer import UserSerializer
from provider.api.v1.serializers.car import CarReadSerializer
from core.serializers.base import SoftDeleteSerializer
from client.models import Offer


class OfferReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = (
            'user',
            'car',
            'max_price',
        )


class OfferCreateSerializer(SoftDeleteSerializer):
    class Meta:
        model = Offer
        fields = (
            'user',
            'car',
            'max_price',
        )
