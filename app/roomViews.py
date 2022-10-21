from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from app.models import Rooms
from app.serializers import RoomSerializer

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rooms(request):
    snippets = Rooms.objects.filter(created_by=request.user.id)
    serializer = RoomSerializer(snippets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def addRoom(request):
    ins = request.data
    ins['created_by'] = request.user.id
    serializer = RoomSerializer(data=ins)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteRoom(request, roomId):
    if Rooms.objects.filter(id=roomId).exists():
        room = Rooms.objects.get(id=roomId)
        room.delete()
        snippets = Rooms.objects.filter(created_by=request.user.id)
        serializer = RoomSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)