import random
from asyncio import sleep

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.shortcuts import render


# Create your views here.
class CheckUserConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        while True:
            await self.send_json({"type": "connect", "data": random.randint(0, 1000)})
            await sleep(1)

    async def user_update(self, event):
        await self.send_json(
            {
                'type': 'update',
                'data': random.randint(0, 1000)
            }
        )


def index(request):
    return render(request, 'index.html')
