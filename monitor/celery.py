import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitor.settings')

app = Celery(main='monitor')

app.conf.beat_schedule = {
    'search_cards_every_15_min': {
        'task': 'apps.management.tasks.search_all_active_order',
        'schedule': crontab(minute='*/3')
    }
}

app.conf.broker_connection_retry_on_startup = True

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
