from django.shortcuts import render, HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_view(request):
    send_mail_func.delay()
    return HttpResponse('Mail Sent')

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=2, minute=58)
    task = PeriodicTask.objects.create(
        crontab=schedule,
        name="view_scheduled_task_1",
        task="send_mail_app.tasks.send_mail_func"
    )
        # args=json.dumps((2,3,))
    return HttpResponse("Done")