from django.urls import path
from .views import test, send_mail_view

urlpatterns = [
    path('', test, name='test'),
    path('sendmail/', send_mail_view, name='sendmail')
]
