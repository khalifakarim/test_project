from provider.models import (
    CarPrice,
    RegularProviderCustomers,
    ProviderAction,
)


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
    sorted_best_price = sorted(best_price)
    # final_offer = {sorted_best_price[0]: best_price[sorted_best_price[0]]}
    create_table(best_price, sorted_best_price, showroom)


def get_better_action(car):
    better_action_price = {}
    cars = CarPrice.objects.filter(car=car)
    for car in cars:
        discount_percentage = ProviderAction.objects.get(cars=car.car, provider=car.provider)
        if discount_percentage.discount_percentage == 0:
            raise ValueError
        total_price = car.price * (discount_percentage.discount_percentage / 100)
        better_action_price[total_price] = discount_percentage.provider
    sorted_promotion_action = sorted(better_action_price)
    return {sorted_promotion_action[0]: better_action_price[sorted_promotion_action[0]]}


def get_better_promotion(car, showroom):
    better_promotion_price = {}
    cars = CarPrice.objects.filter(car=car)
    for car in cars:
        discount_percentage = RegularProviderCustomers.objects.get(customer=showroom)
        if discount_percentage.discount_percentage == 0:
            raise ValueError
        total_price = car.price * (discount_percentage.discount_percentage / 100)
        better_promotion_price[total_price] = discount_percentage.provider
    sorted_promotion_price = sorted(better_promotion_price)
    return {sorted_promotion_price[0]: better_promotion_price[sorted_promotion_price[0]]}


def get_better_price(car, showroom):
    better_price = {}
    cars = CarPrice.objects.filter(car=car)
    for car in cars:
        car = CarPrice.objects.filter(car=car.car).order_by('price').first()
        better_price[car.price] = car.provider
    sorted_price = sorted(better_price)
    return {sorted_price[0]: better_price[sorted_price[0]]}


def create_table(best_price, sorted_best_price, showroom):
   pass
