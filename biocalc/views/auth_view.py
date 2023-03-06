
from django.contrib.auth.models import User
from biocalc.serializers import (
    UserRegistrationSerializer, 
    UserLoginSerializer,
    API_Login_Serializer)
from biocalc.permissions import IsPostRequestOrAdmin

from rest_framework import generics
from rest_framework.decorators import authentication_classes

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


	
class APILogoutView(APIView):
    """
    Logout via API - send user token to blacklist

    requires an access token for authorization and
    a refresh token for blacklisting it
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK, goodbye"})


class APIRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsPostRequestOrAdmin,)
    serializer_class = UserRegistrationSerializer
    
class APILoginView(TokenObtainPairView):
    """
    Obtain pair tokens with inserting name and status "is_editor" into access token
    """
    
    serializer_class = API_Login_Serializer # UserLoginSerializer #



