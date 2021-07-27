from rest_framework import serializers

from provider.api.v1.serializers.manufacturer import ManufacturerSerializer
from core.serializers.base import SoftDeleteSerializer
from core.serializers.base import BaseSerializer
from provider.models import Car


class CarReadSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = Car


class CarCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = Car
