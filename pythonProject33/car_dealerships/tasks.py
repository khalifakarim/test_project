from celery import shared_task
import logging

from car_dealerships.api.v1.exceptions.sale_history import SaleHistoryError

from car_dealerships.api.v1.services.popular_car_logic import (
    _get_active_showrooms,
    _get_sale_history,
)

logger = logging.getLogger(__name__)


@shared_task
def find_sold_cars():
    for showroom in _get_active_showrooms():
        try:
            _get_sale_history(showroom)
        except SaleHistoryError:
            logger.warning(f"{showroom.name} has no sales history")
            continue
