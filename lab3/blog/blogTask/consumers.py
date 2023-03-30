from email import message
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class TaskConsumer(WebsocketConsumer):

    def connect(self):
        self.room_group_name = 'taskGroup'
        self.accept()
        async_to_sync(self.channel_layer.group_add) (
            self.room_group_name,
            self.channel_name
        )
        self.send(text_data=json.dumps({
            'type' : 'connection-established',
            'message' : 'You are now connect!'
        }))

    def taskEmail(self, event):
        name = event['name']
        dateEnd = event['dateEnd']
        result = event['result']
        self.send(text_data=json.dumps({
            'type': 'email',
            'name': name,
            'dateEnd': dateEnd,
            'result': result
        }))
    def taskDelMes(self, event):
        name = event['name']
        dateEnd = event['dateEnd']
        result = event['result']
        self.send(text_data=json.dumps({
            'type': 'delete',
            'name': name,
            'dateEnd': dateEnd,
            'result': result
        }))


