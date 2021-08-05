from provider.models import CarPrice


def create_purchase_characteristics(showroom):
    from car_dealerships.models import AvailableCars
    available_cars = AvailableCars.objects.filter(car_dealership=showroom)
    get_providers(available_cars, showroom)


def get_providers(available_cars, showroom):
    providers = []
    for car in available_cars:
        providers.append(CarPrice.objects.filter(car=car.car).order_by('price').first())
    create_table(providers, showroom)


def create_table(providers, showroom):
    from car_dealerships.models import PurchaseCharacteristics

    available_providers = []

    for provider in providers:
        available_providers.append(
            PurchaseCharacteristics(
                preferred_cars_quantity=1,
                provider=provider.provider,
                car_dealership=showroom,
                car=provider.car,
            )
        )

    PurchaseCharacteristics.objects.bulk_create(available_providers)
