from rest_framework import viewsets

from client.api.v1.serializers.offer import OfferCreateSerializer, OfferReadSerializer
from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin
from client.api.v1.filters.offer import OfferFilter
from client.models import Offer


class OfferViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet
):
    queryset = Offer.objects.all()
    write_serializer = OfferCreateSerializer
    read_only_serializer = OfferReadSerializer
    filterset_class = OfferFilter
