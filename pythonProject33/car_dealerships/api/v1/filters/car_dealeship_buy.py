from car_dealerships.models import CarDealershipBuy

from django_filters import (
    FilterSet,
    NumberFilter,
    ChoiceFilter,
)


class CarDealershipBuyFilter(FilterSet):
    cars_quantity_gte = NumberFilter(field_name="cars_quantity", lookup_expr='gte')
    cars_quantity_lte = NumberFilter(field_name="cars_quantity", lookup_expr='lte')
    price_lte = NumberFilter(field_name="price", lookup_expr='lte')
    price_gte = NumberFilter(field_name="price", lookup_expr='gte')

    class Meta:
        model = CarDealershipBuy
        fields = ['is_active', 'cars_quantity', 'price']
