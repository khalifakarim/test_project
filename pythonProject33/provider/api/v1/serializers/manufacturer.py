from core.serializers.base import SoftDeleteSerializer
from core.serializers.base import BaseSerializer
from provider.models import Manufacturer


class ManufacturerSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = Manufacturer
