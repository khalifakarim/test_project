from rest_framework import viewsets, mixins

from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin
from core.permissions.customer import IsUser
from client.models import User, Offer

from client.serializers import (
    OfferCreateSerializer,
    OfferReadSerializer,
    UserSerializer,
)


class UserViewSet(
    SoftDeleteMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateViewSet(
    SoftDeleteMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class OfferViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet
):
    queryset = Offer.objects.all()
    write_serializer = OfferCreateSerializer
    read_only_serializer = OfferReadSerializer
