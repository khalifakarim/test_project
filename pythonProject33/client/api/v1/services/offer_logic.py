from car_dealerships.models import CarDealershipSale
from car_dealerships.models import AvailableCars
from client.models import Offer


def _active_offers():
    return Offer.objects.get_active_offers()


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
    car.car_dealership.balance += car.price
    car.cars_quantity -= 1
    car.save()


def _user_deduction_balance(user, car_price):
    user.balance -= car_price
    user.save()


def _create_sale_history(car, user):
    CarDealershipSale.objects.create(
        customer=user,
        car_dealership=car.car_dealership,
        price=car.price,
        car=car.car,
    )


def _deactivate_offer(offer):
    offer.is_active = False
    offer.save()
