from django.shortcuts import  render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def order_handler(request):
    user = request.user     # вытаскивает юзера из авторизированого запроса
    order = request.data['order']
    print(user, order)

    return Response( {"status": "order send in test mode"} )
