from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.models import User

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_app(request):
    user = User.objects.get(id=request.user.id)
    data = {
        'first_name': user.first_name,
        'app_key': user.app_key,
        'app_secret': user.app_secret
    }
    return Response(data, status=status.HTTP_200_OK)