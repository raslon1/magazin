from celery import shared_task
from .utils import JsonToData


@shared_task
def Task():
    r = JsonToData()
    r.run()
