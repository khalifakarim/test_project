from django.db.models import Count, F, Max

from car_dealerships.api.v1.exceptions.sale_history import SaleHistoryError
from car_dealerships.api.v1.exceptions.balance import BalanceError
from provider.models import CarPrice

from car_dealerships.models import (
    CarDealershipSale,
    CarDealershipBuy,
    CarDealership,
)


def _check_balance(showroom, providers):
    for provider in providers:
        if showroom.balance > provider.price:
            lost_showroom_money(showroom, provider.price)
            create_buy_history(showroom, provider)
        else:
            raise BalanceError(showroom.name)


def _get_active_showrooms():
    return CarDealership.objects.get_active_showrooms()


def _get_sale_history(showroom):
    cars = CarDealershipSale.objects.filter(car_dealership=showroom).values("car").annotate(
        car_count=Count("car")).order_by("-car_count")
    _get_better_provider(cars, showroom)


def _get_better_provider(cars, showroom):
    providers = []
    if not cars:
        raise SaleHistoryError(showroom.name)
    for car in cars:
        providers.append(CarPrice.objects.filter(car__id=car['car'], ).order_by('price'))
    return _check_balance(showroom, providers)


def lost_showroom_money(showroom, price):
    CarDealership.objects.filter(id=showroom.id).update(balance=F('balance') - price)


def create_buy_history(showroom, provider):
    CarDealershipBuy.objects.create(
        car_dealership=showroom,
        provider=provider.provider,
        price=provider.price,
        car=provider.car,
        cars_quantity=1,
    )
