import json
from django.http import HttpResponse, JsonResponse
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import time
from django.contrib.auth.models import User, auth
from .models import chatLogs
from asgiref.sync import async_to_sync, sync_to_async
from .models import chatLogs
from websocket import create_connection
import requests
from .views import fetchDataTest
from channels.db import database_sync_to_async
from channels.exceptions import StopConsumer
import secrets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from urllib.parse import parse_qs
# import urlparse
# from channels import Group
# from channels.sessions import channel_session

realtime_port = 8082

# username = 'tdws128'
# password = 'anand@128'

# ws = ''
# ws = create_connection(f"wss://push.truedata.in:{realtime_port}?user={username}&password={password}")

# ws.send('{"method": "addsymbol", "symbols":["AARTIIND"]}')


class DashConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'test'

        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name
        )

        # WS accept
        await self.accept()

        # Message to be sent on connection
        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected',
        }))

    async def disconnect(self, code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        raise StopConsumer()

    async def receive(self, text_data):

        text_data_json = json.loads(text_data)

        await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'send_data',
            'value': text_data_json
        }
        )

        # print('>>>>', text_data_json)

    async def send_data(self, event):
        # testusername = await database_sync_to_async(self.get_name)()

        # userDataJson = {
        #     'status': 'success',
        #     'username': testusername
        # }
        jsonValue = event['value']
        # jsonValue = userDataJson
        await self.send(text_data = json.dumps(jsonValue))

################################################################################

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # print(self.scope["url_route"]["kwargs"]["room"])
        # # print('ROOM KEY: ', room_key)
        # print(self.kwargs['room'])

        room_key = secrets.token_hex(10)

        self.room_group_name = room_key

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
        self.room_group_name,
        self.channel_name,
        )

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!',
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data = None):
        text_data_json = json.loads(text_data)
        message = text_data_json

        print('Received')

        async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
            {
        'type': 'send_data',
        'message': 'Order Placed',
            }
        )

    def send_data(self, event):
        self.send(text_data = json.dumps(event))
