from rest_framework import serializers
from app.models import Rooms, Items

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class RoomInfoSerializer(serializers.ModelSerializer):
    roomInfo = ItemSerializer(many=True)
    class Meta:
        model = Rooms
        fields = ['id', 'espId', 'roomName', 'active', 'roomInfo']

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['itemId', 'itemStatus']