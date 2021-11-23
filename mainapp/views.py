from django.shortcuts import render, HttpResponse
from .tasks import test_func
from send_mail_aap.task import send_mail_func

def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_view(request):
    send_mail_func.delay()
    return HttpResponse('Mail Sent')