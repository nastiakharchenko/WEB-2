#from __future__ import absolute_import   #, unicode_literals
import os
from celery import Celery
from django.conf import settings

#Задаем переменную окружения, содержащую название файла настроек проекта:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinestore.settings')
app = Celery('onlinestore')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()    #lambda: settings.INSTALLED_APPS)