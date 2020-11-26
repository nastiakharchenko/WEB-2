# import os
# from celery import Celery
#
# #Задаем переменную окружения, содержащую название файла настроек проекта:
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinestore.settings')
# app = Celery('onlinestore')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()