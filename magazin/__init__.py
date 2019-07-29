__all__ = ['app']

import os
import logging
import celery
import raven
from raven.contrib.celery import register_logger_signal, register_signal

from .settings import SENTRY_DSN
# Инициализация джанго
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magazin.settings')

class Celery(celery.Celery):

    def on_configure(self):
        client = raven.Client(SENTRY_DSN)

        # hook into the Celery error handler
        register_logger_signal(client, loglevel=logging.ERROR)
        register_signal(client)



# Инициализация Celery
app = Celery('magazin')

app.config_from_object('magazin.settings')

app.autodiscover_tasks()