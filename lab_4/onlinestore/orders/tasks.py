# from celery import task
# from django.core.mail import send_mail
# from .models import Order
#
# @task
# def order_created(order_id):
#     """Задача отправки email-уведомлений при успешном оформлении заказа."""
#     order = Order.objects.get(id=order_id)
#     subject = 'Заказ nr. {}'.format(order.id)
#     message = 'Уважаемый {},\n\nВы успешно разместили заказ.\
#                 id Вашего заказа: {}.'.format(order.first_name, order.id)
#     mail_sent = send_mail(subject, message,
#                       'onlinestore@gmail.com',
#                       [order.email])
#     return mail_sent