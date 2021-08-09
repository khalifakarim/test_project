import logging

from django.db.models import Count, F

from car_dealerships.api.v1.exceptions.sale_history import SaleHistoryError
from car_dealerships.api.v1.exceptions.balance import BalanceError
from car_dealerships.models import PurchaseCharacteristics

from car_dealerships.models import (
    CarDealershipSale,
    CarDealershipBuy,
    AvailableCars,
    CarDealership,
)

logger = logging.getLogger(__name__)


def _check_balance(showroom, purchase_characteristics):
    for purchase_characteristic in purchase_characteristics:
        price = purchase_characteristic.provider.cars.filter(car__id=purchase_characteristic.car.id).first().price
        price = purchase_characteristic.preferred_cars_quantity * price
        if showroom.balance > price:
            lost_showroom_money(showroom, price, purchase_characteristic)
            create_buy_history(showroom, purchase_characteristic, price)
        else:
            raise BalanceError(showroom.name)


def _get_active_showrooms():
    return CarDealership.objects.get_active_instances()


def _get_sale_history(showroom):
    cars = CarDealershipSale.objects.filter(car_dealership=showroom).values("car").annotate(
        car_count=Count("car")).order_by("-car_count")
    _get_better_provider(cars, showroom)


def _get_better_provider(cars, showroom):
    purchase_characteristics = []
    if not cars:
        raise SaleHistoryError(showroom.name)
    for car in cars:
        try:
            purchase_characteristics.append(PurchaseCharacteristics.objects.filter(car__id=car['car']).first())
            _check_balance(showroom, purchase_characteristics)
        except BalanceError:
            logger.warning(f"{showroom.name} does not have enough money on the balance")


def lost_showroom_money(showroom, price, purchase_characteristic):
    CarDealership.objects.filter(id=showroom.id).update(
        balance=F('balance') - (price * purchase_characteristic.preferred_cars_quantity))


def create_buy_history(showroom, purchase_characteristic, price):
    CarDealershipBuy.objects.create(
        car_dealership=showroom,
        provider=purchase_characteristic.provider,
        price=price,
        car=purchase_characteristic.car,
        cars_quantity=1,
    )
    AvailableCars.objects.filter(
        car_dealership=showroom,
        car=purchase_characteristic.car,
    ).update(cars_quantity=purchase_characteristic.preferred_cars_quantity)
