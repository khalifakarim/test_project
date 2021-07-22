from rest_framework import viewsets, mixins

from core.views.mixins.base import SoftDeleteMixin
from client.serializers import UserSerializer
from core.permissions.customer import IsUser
from client.models import User


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
