from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import index

app_name = MailingsConfig.name

urlpatterns = [
    path('', index, name='index'),
]
