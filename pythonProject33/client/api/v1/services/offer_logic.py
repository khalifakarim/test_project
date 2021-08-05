from django.db.models import F

from car_dealerships.models import CarDealershipSale
from car_dealerships.models import AvailableCars
from client.models import Offer


def _active_offers():
    return Offer.objects.get_active_instances()


def _get_car(offer):
    car = AvailableCars.objects.filter(
        car__id=offer.car.id,
        price__lte=offer.max_price,
        cars_quantity__gt=0).order_by('price').first()

    _showroom_additions_balance(car)
    _user_deduction_balance(offer.user, car.price)
    _create_sale_history(car, offer.user)
    _deactivate_offer(offer)


def _showroom_additions_balance(car):
    car.car_dealership.update(balance=F('balance') + car.price)
    car.update(cars_quantity=F('cars_quantity') - 1)


def _user_deduction_balance(user, car_price):
    user.update(balance=F('balance') - car_price)


def _create_sale_history(car, user):
    CarDealershipSale.objects.create(
        customer=user,
        car_dealership=car.car_dealership,
        price=car.price,
        car=car.car,
    )


def _deactivate_offer(offer):
    offer.update(is_active=False)
