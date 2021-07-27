from car_dealerships.models import CarDealershipSale

from django_filters import (
    NumberFilter,
    FilterSet,
)


class CarDealershipSaleFilter(FilterSet):
    min_cars_quantity = NumberFilter(field_name="cars_quantity", lookup_expr='gte')
    max_cars_quantity = NumberFilter(field_name="cars_quantity", lookup_expr='lte')
    min_price = NumberFilter(field_name="price", lookup_expr='lte')
    max_price = NumberFilter(field_name="price", lookup_expr='gte')

    class Meta:
        model = CarDealershipSale
        fields = ('is_active', 'cars_quantity', 'price')
