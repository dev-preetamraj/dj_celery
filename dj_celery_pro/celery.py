from __future__ import absolute_import, unicode_literals
from datetime import timezone
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_celery_pro.settings')

app = Celery('dj_celery_pro')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery beat settings
app.conf.beat_schedule = {
    'send-mail-on-mon-tue': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=18, minute=39, day_of_week=2) # day_of_week=2 for tuesday
        # 'args': 
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')