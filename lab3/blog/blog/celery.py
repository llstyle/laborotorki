from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379')
app = Celery('blog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_url = BASE_REDIS_URL
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
app.conf.beat_schedule = {
    'mail-every-day-contrab': {
        'task': 'my_first_task',
        'schedule': crontab(minute=30, hour=7),
    },
    'delete-every-day-contrab': {
        'task': 'messageDelete',
        'schedule': crontab(minute=0, hour=0),
    },
}
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
