from rest_framework import viewsets, mixins

from client.api.v1.serializers.customer import UserSerializer
from core.views.mixins.base import SoftDeleteMixin
from client.api.v1.filters.user import UserFilter
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
    filterset_class = UserFilter
    search_fields = (
        'email',
        'username',
    )


class UserUpdateViewSet(
    SoftDeleteMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
