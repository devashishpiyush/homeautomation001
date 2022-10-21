from xmlrpc.client import Boolean
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from app.models import Rooms
from app.models import Items
from app.serializers import SwitchSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response('Welcome to SmartHome!', status=status.HTTP_200_OK)

@api_view(['GET'])
def getEsp(request, espId):
    roomId = Rooms.objects.get(espId=espId).id
    items = Items.objects.filter(roomId=roomId)
    serializer = SwitchSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def setEsp(request, itemId, value):
    item = Items.objects.filter(itemId=itemId)
    if item:
        switch = Items.objects.get(itemId=itemId)
        if value == 1:
            switch.itemStatus = True
        else:
            switch.itemStatus = False
        switch.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)