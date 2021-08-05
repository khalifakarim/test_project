from celery import shared_task

from client.api.v1.services.offer_logic import (
    _active_offers,
    _get_car,
)


@shared_task
def take_offer():
    for offer in _active_offers():
        _get_car(offer)
