from car_dealerships.models import CarDealershipAction

from django_filters import (
    NumberFilter,
    FilterSet,
)


class CarDealershipActionFilter(FilterSet):
    max_discount_percentage = NumberFilter(field_name="discount_percentage", lookup_expr='gte')
    min_discount_percentage_ = NumberFilter(field_name="discount_percentage", lookup_expr='lte')

    class Meta:
        model = CarDealershipAction
        fields = ('is_active', 'discount_percentage')
