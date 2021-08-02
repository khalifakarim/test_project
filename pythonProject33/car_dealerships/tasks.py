from celery import shared_task

from car_dealerships.api.v1.services.popular_car_logic import (
    _get_active_showrooms,
    _get_sale_history,
)


@shared_task
def find_sold_cars():
    for showroom in _get_active_showrooms():
        _get_sale_history(showroom)
