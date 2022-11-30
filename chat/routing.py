from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    # path('ws/socket-server/<slug:room>', consumers.ChatConsumer.as_asgi()),
    re_path(r'^ws/socket-server/(?P<room>\w+)/$', consumers.ChatConsumer.as_asgi()),

    path('ws/polData/<slug:usernamee>', consumers.DashConsumer.as_asgi())
]
