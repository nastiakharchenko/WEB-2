from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """Задача отправки email-уведомлений при успешном оформлении заказа."""
    order = Order.objects.get(id=order_id)
    subject = 'Заказ nr. {}'.format(order.id)
    message = 'Уважаемый(ая) {},\n\nВы успешно разместили заказ.\
                id Вашего заказа: {}.'.format(order.first_name, order.id)
    print("Hello")
    mail_sent = send_mail(subject, message,
                      'admin@onlinestore.com',
                      [order.email], fail_silently=False)
    return mail_sent