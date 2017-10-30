from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import Order
from django.contrib import messages


@task(name="send_mail_to_custormer")
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {} {},\n\nYou have successfully placed an order. Your order id is {}'.format(order.first_name,
                                                        order.last_name, order.id)



    from_email = settings.EMAIL_HOST_USER
    to_email = [order.email]
    mail_sent = send_mail(
                            subject,
                            message,
                            from_email,
                            to_email,
                            fail_silently=False
                          )
    return mail_sent