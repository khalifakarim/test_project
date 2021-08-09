import decimal
import logging

from car_dealerships.api.v1.exceptions.best_price import BestPriceError
from django.core.exceptions import ObjectDoesNotExist

from provider.models import (
    RegularProviderCustomer,
    ProviderAction,
    CarPrice,
)

logger = logging.getLogger(__name__)


def create_purchase_characteristics(showroom):
    from car_dealerships.models import AvailableCars
    available_cars = AvailableCars.objects.filter(car_dealership=showroom)
    get_better_providers(available_cars, showroom)


def get_better_providers(available_cars, showroom):
    for available_car in available_cars:
        get_better_offer(available_car, showroom)


def get_better_offer(available_car, showroom):
    action = get_better_action(available_car)
    promotion = get_better_promotion(available_car, showroom)
    price = get_better_price(available_car)
    best_price = {**promotion, **action, **price}

    if not best_price:
        raise BestPriceError()

    min_price = sorted(best_price).pop(0)
    final_price = {min_price: best_price[min_price]}
    create_table(final_price[min_price], showroom, available_car.car)


def get_better_action(available_car):
    better_action_price = {}
    car_prices = CarPrice.objects.filter(car=available_car.car)

    for car_price in car_prices:
        try:
            provider_action = ProviderAction.objects.get(car=car_price.car, provider=car_price.provider)
        except ObjectDoesNotExist:
            logger.warning(f"{provider_action.provider.name} does not have action on this car")
        total_price = car_price.price * (decimal.Decimal(provider_action.discount_percentage / 100))
        better_action_price[total_price] = provider_action.provider

    if not better_action_price:
        return {}

    min_price = sorted(better_action_price).pop(0)
    return {min_price: better_action_price[min_price]}


def get_better_promotion(available_car, showroom):
    better_promotion_price = {}
    car_prices = CarPrice.objects.filter(car=available_car.car)

    for car_price in car_prices:
        regular_provider_customers = RegularProviderCustomer.objects.filter(customer=showroom).order_by(
            "-discount_percentage")

        for regular_provider_customer in regular_provider_customers:
            total_price = car_price.price * (decimal.Decimal(regular_provider_customer.discount_percentage / 100))
            better_promotion_price[total_price] = regular_provider_customer.provider

    if not better_promotion_price:
        return {}

    min_price = sorted(better_promotion_price).pop(0)
    return {min_price: better_promotion_price[min_price]}


def get_better_price(available_car):
    car_price = CarPrice.objects.filter(car=available_car.car).order_by('price').first()
    if not car_price:
        return {}
    return {car_price.price: car_price.provider}


def create_table(provider, showroom, car):
    from car_dealerships.models import PurchaseCharacteristics

    PurchaseCharacteristics.objects.create(
        preferred_cars_quantity=1,
        provider=provider,
        car_dealership=showroom,
        car=car
    )
