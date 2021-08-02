from car_dealerships.models import AvailableCars
from provider.models import CarPrice


def create_available_cars(showroom):
    cars = CarPrice.objects.filter(**showroom.preferred_characteristics)
    return iter_cars(cars, showroom)


def iter_cars(cars, showroom):
    available_cars = []

    for car in cars:
        available_cars.append(
            AvailableCars(
                cars_quantity=0,
                car_dealership=showroom.pk,
                car=car.pk,
                price=1,
            )
        )

    AvailableCars.objects.bulk_create(available_cars)
