from django.urls import path
from .views import test, send_mail_view, schedule_mail

urlpatterns = [
    path('', test, name='test'),
    path('sendmail/', send_mail_view, name='sendmail'),
    path('schedulemail/', schedule_mail, name='schedulemail'),
]
