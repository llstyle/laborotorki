from celery import shared_task
from django.core.mail import send_mail
from .models import EmailUserSend
from chat.models import Message
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from datetime import datetime, timezone


@shared_task(name="my_first_task")
def my_first_task():
   email_list = list(EmailUserSend.objects.all().values_list("user__email", flat=True))

   subject = 'sending emails using celery'

   message = 'hello this is my first send email with celery using Django'

   send_mail(subject, message, None, email_list)
   now = datetime.now(timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
   channel_layer = get_channel_layer()
   async_to_sync(channel_layer.group_send)(
      'taskGroup',
      {
         'type': 'taskEmail',
         'name': 'Рассылка по почте',
         'dateEnd': now,
         'result': f'Было отпавленно сообщение {EmailUserSend.objects.all().count()} людям'
      }
   )


@shared_task(name="messageDelete")
def messageDelete():
   count = Message.objects.all().delete()
   print("Удалено")
   now = datetime.now(timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
   channel_layer = get_channel_layer()
   async_to_sync(channel_layer.group_send)(
      'taskGroup',
      {
         'type': 'taskDelMes',
         'name': 'Удалние сообщений чата',
         'dateEnd': now,
         'result': f'Было удалено {count[0]} сообщений'
      }
   )