from django_filters import FilterSet, NumberFilter, ChoiceFilter
from client.models import User


class UserFilter(FilterSet):
    balance_lte = NumberFilter(field_name="balance", lookup_expr='lte')
    balance_gte = NumberFilter(field_name="balance", lookup_expr='gte')

    class Meta:
        model = User
        fields = ['balance', 'is_active']
