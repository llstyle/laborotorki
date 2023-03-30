from django.urls import re_path
from . import consumers

websockets = [
    re_path(r'ws/socketTask-server/', consumers.TaskConsumer.as_asgi())
]