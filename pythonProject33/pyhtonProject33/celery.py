from celery import Celery

app = Celery("pythonProject33", include=["client.tasks", "car_dealerships.tasks"])
# app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     "take_offer": {"task": "client.tasks.take_offer", "schedule": 15}
# }
