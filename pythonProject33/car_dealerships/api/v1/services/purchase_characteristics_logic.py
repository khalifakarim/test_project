from provider.models import (
    RegularProviderCustomers,
    ProviderAction,
    CarPrice,
)
from car_dealerships.models import PurchaseCharacteristics


def create_purchase_characteristics(showroom):
    from car_dealerships.models import AvailableCars
    available_cars = AvailableCars.objects.filter(car_dealership=showroom)
    get_better_providers(available_cars, showroom)


def get_better_providers(available_cars, showroom):
    for car in available_cars:
        get_better_offer(car, showroom)


def get_better_offer(car, showroom):
    action = get_better_action(car)
    promotion = get_better_promotion(car, showroom)
    price = get_better_price(car)
    best_price = {**promotion, **action, **price}
    min_price = sorted(best_price).pop(0)
    final_price = {min_price: best_price[min_price]}
    create_table(final_price, showroom, min_price, car.car)


def get_better_action(car):
    better_action_price = {}
    car_prices = CarPrice.objects.filter(car=car)

    for car_price in car_prices:
        discount_percentage = ProviderAction.objects.get(car=car_price.car, provider=car_price.provider)
        if not discount_percentage.discount_percentage:
            raise ValueError({"message": "there is no action for this car "})
        total_price = car_price.price * (discount_percentage.discount_percentage / 100)
        better_action_price[total_price] = discount_percentage.provider

    if not better_action_price:
        raise ValueError({"message": "there is no any actions for this car "})

    min_price = sorted(better_action_price)
    return {min_price: better_action_price[min_price]}


def get_better_promotion(car, showroom):
    better_promotion_price = {}
    car_prices = CarPrice.objects.filter(car=car)

    for car_price in car_prices:
        regular_provider_customer = RegularProviderCustomers.objects.filter(customer=showroom)
        if not regular_provider_customer.discount_percentage:
            raise ValueError({"message": "you have not discount_percentage "})
        total_price = car_price.price * (regular_provider_customer.discount_percentage / 100)
        better_promotion_price[total_price] = regular_provider_customer.provider

    if not better_promotion_price:
        raise ValueError({"message": "you have not any promotions on this car"})

    min_price = sorted(better_promotion_price).pop(0)
    return {min_price: better_promotion_price[min_price]}


def get_better_price(car, showroom):
    better_price = {}
    car_prices = CarPrice.objects.filter(car=car)

    for car_price in car_prices:
        car = CarPrice.objects.filter(car=car_price.car).order_by('price').first()
        better_price[car_price.price] = car_price.provider
    if not better_price:
        raise ValueError({"message": "you have not car"})

    min_price = sorted(better_price).pop(0)
    return {min_price: better_price[min_price]}


def create_table(final_price, showroom, min_price, car):
    PurchaseCharacteristics.objects.create(
        preferred_cars_quantity=1,
        provider=final_price[min_price],
        car_dealership=showroom,
        car=car

    )
