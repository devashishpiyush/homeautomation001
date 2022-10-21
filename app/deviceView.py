from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from app.models import Rooms, Items
from app.serializers import ItemSerializer, RoomInfoSerializer

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def devices(request):
    snippets = Rooms.objects.filter(created_by=request.user.id)
    serializer = RoomInfoSerializer(snippets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def addDevice(request):
    ins = request.data
    ins['created_by'] = request.user.id
    serializer = ItemSerializer(data=ins)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteDevice(request, deviceId):
    if Items.objects.filter(itemId=deviceId).exists():
        item = Items.objects.get(itemId=deviceId)
        item.delete()
        snippets = Rooms.objects.filter(created_by=request.user.id)
        serializer = RoomInfoSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)