import os
from django.conf import settings
from django.shortcuts import  render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from biocalc.serializers import FishSerializer

def index(request):
    return render(request, 'base.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected(request):
    media_path = settings.MEDIA_ROOT
    for path, subdirs, files in os.walk(media_path):
        for name in files:
            print(os.path.join(path, name))

    return Response({"status": "OK, goodbye", "msg":"you are user"})

@api_view(['GET'])
@permission_classes([IsAdminUser])
def protected_set(request):
    user = request.user     # вытаскивает юзера из авторизированого запроса
    fishes_from_current_user = FishSerializer(user.fishes_set.all(), many=True).data # возвращает список рыб, связанных с юзером
    return Response( fishes_from_current_user )
