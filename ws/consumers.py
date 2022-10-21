from channels.generic.websocket import JsonWebsocketConsumer
from channels.exceptions import StopConsumer

from account.models import User
from app.models import Rooms, Items
from asgiref.sync import async_to_sync

from app.serializers import RoomInfoSerializer

class MyConsumer(JsonWebsocketConsumer):

    def connect(self):
        global userId
        global app_key
        app_key = self.scope['url_route']['kwargs']['app_key']
        app_secret = self.scope['url_route']['kwargs']['app_secret']
        user = User.objects.get(app_key=app_key, app_secret=app_secret)
        if user:
            userId = user.id
            async_to_sync(self.channel_layer.group_add)(app_key, self.channel_name)
            self.accept()
            rooms = Rooms.objects.filter(created_by=userId)
            serializer = RoomInfoSerializer(rooms, many=True)
            self.send_json(serializer.data)
        else:
            self.close()

    def receive_json(self, content, **kwargs):
        try:
            item = Items.objects.get(itemId=content['itemId'])
            item.itemStatus = content['itemStatus']
            item.save()
        except:
            pass
        rooms = Rooms.objects.filter(created_by=userId)
        serializer = RoomInfoSerializer(rooms, many=True)
        async_to_sync(self.channel_layer.group_send)(
            app_key,
            {
                'type': 'chat.message',
                'message': serializer.data
            }
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(app_key, self.channel_name)
        raise StopConsumer()

    def chat_message(self, event):
        self.send_json(event['message'])
