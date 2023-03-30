from email import message
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from .models import  Message, OnlineChatUsers
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class PracticeConsumer(WebsocketConsumer):

    def connect(self):
        self.user = self.scope["user"]
        self.room_group_name = 'blog'
        self.accept()
        async_to_sync(self.channel_layer.group_add) (
            self.room_group_name,
            self.channel_name
        )
        OnlineChatUsers.objects.all().first().online.add(self.user)
        async_to_sync(self.channel_layer.group_send) (
            self.room_group_name,
            {
                'type': 'user_on',
                'users' : [user.username for user in OnlineChatUsers.objects.all().first().online.all()],
            }
        )
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.save_message(message)
        async_to_sync(self.channel_layer.group_send) (
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': self.user.username,
                'message' : message,
            }
        )

    def chat_message(self, event):
        username = event['username']
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'username': username
        }))
    def user_on(self, event):
        users = event['users']
        self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': users
        }))
    def disconnect(self, close_code):
        OnlineChatUsers.objects.all().first().online.remove(self.user)
        async_to_sync(self.channel_layer.group_send) (
            self.room_group_name,
            {
                'type': 'user_on',
                'users' : [user.username for user in OnlineChatUsers.objects.all().first().online.all()],
            }
        )
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def save_message(self, message):
        Message.objects.create(user=self.user, content=message)

