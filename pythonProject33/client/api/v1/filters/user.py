from client.models import User

from django_filters import (
    FilterSet,
    NumberFilter,
)


class UserFilter(FilterSet):
    min_balance = NumberFilter(field_name="balance", lookup_expr='lte')
    max_balance = NumberFilter(field_name="balance", lookup_expr='gte')

    class Meta:
        model = User
        fields = ('balance', 'is_active')
