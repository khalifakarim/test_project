from provider.models import Car


def create_available_cars(showroom):
    cars = Car.objects.filter(**showroom.preferred_characteristics)
    create_carshowroom_cars(cars, showroom)


def create_carshowroom_cars(cars, showroom):
    from car_dealerships.models import AvailableCars

    available_cars = []

    for car in cars:
        available_cars.append(
            AvailableCars(
                cars_quantity=0,
                car_dealership=showroom,
                car=car,
                price=0,
            )
        )

    AvailableCars.objects.bulk_create(available_cars)
