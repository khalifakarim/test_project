from celery import shared_task
from django.db.models import Count, F

from car_dealerships.models import CarDealershipSale, CarDealership, CarDealershipBuy
from provider.models import CarPrice


@shared_task
def find_sold_cars():
    for showroom in _get_active_showrooms():
        _get_sale_history(showroom)


def _check_balance(showroom, providers):
    for provider in providers:
        if showroom.balance > provider.price:
            lost_showroom_money(showroom, provider.price)
            create_buy_history(showroom, provider)
        else:
            return


def _get_active_showrooms():
    return CarDealership.objects.get_active_showrooms()


def _get_sale_history(showroom):
    cars = CarDealershipSale.objects.filter(car_dealership=showroom.id).aggregate(Count('car__id')).order_by(
        Count('-car__id'))
    _get_better_provider(cars, showroom)


def _get_better_provider(cars, showroom):
    if not cars:
        return
    for car in cars:
        providers = CarPrice.objects.filter(
            car=car.pk, ).order_by('price')
    return _check_balance(showroom, providers)


def lost_showroom_money(showroom, price):
    showroom.balance = F('balance') + price
    showroom.save()


def create_buy_history(showroom, provider):
    CarDealershipBuy.objects.create(showroom=showroom.id,
                                    provider=provider.id,
                                    price=provider.price,
                                    car=provider.car.id,
                                    cars_quantity=1)
