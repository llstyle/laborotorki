from django.urls import re_path
from . import consumers

websockets = [
    re_path(r'ws/socket-server/', consumers.PracticeConsumer.as_asgi())
]