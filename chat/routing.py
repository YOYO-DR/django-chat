from django.urls import re_path
import os
from . import consumers

websocket_urlpatterns = [
  re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
if "WEBSITE_HOSTNAME" in os.environ:
    websocket_urlpatterns.append(re_path(r'wss/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),)