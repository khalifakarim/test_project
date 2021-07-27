from rest_framework import serializers

from provider.api.v1.serializers.provider import ProviderReadSerializer
from provider.api.v1.serializers.car import CarReadSerializer
from core.serializers.base import SoftDeleteSerializer
from core.serializers.base import BaseSerializer
from provider.models import ProviderAction


class ProviderActionReadSerializer(serializers.ModelSerializer):
    provider = ProviderReadSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = ProviderAction


class ProviderActionCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = ProviderAction
