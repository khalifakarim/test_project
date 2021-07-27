from car_dealerships.models import CarDealershipAction
from django_filters import (
    FilterSet,
    NumberFilter,
    ChoiceFilter,
)


class ProviderActionFilter(FilterSet):
    discount_percentage_gte = NumberFilter(field_name="discount_percentage", lookup_expr='gte')
    discount_percentage_lte = NumberFilter(field_name="discount_percentage", lookup_expr='lte')

    class Meta:
        model = CarDealershipAction
        fields = ['is_active', 'discount_percentage']
