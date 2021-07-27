from provider.models import ProviderAction

from django_filters import (
    NumberFilter,
    FilterSet,
)


class ProviderActionFilter(FilterSet):
    min_discount_percentage = NumberFilter(field_name="discount_percentage", lookup_expr='gte')
    max_discount_percentage = NumberFilter(field_name="discount_percentage", lookup_expr='lte')

    class Meta:
        model = ProviderAction
        fields = ('is_active', 'discount_percentage')
