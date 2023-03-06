
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, pagination, status
from rest_framework.response import Response
from biocalc.models import AquaProfile
from biocalc.serializers import UserProfileSerializer

from biocalc.permissions import is_superuser
from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny, 
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    )


class UserProfilesViewSet(viewsets.ModelViewSet):
    """
    Created automatically for each new user.

    Can be read or changed. 

    Cannot be created or deleted manually.
    """
    queryset = AquaProfile.objects.all()
    permission_classes = (is_superuser,)
    serializer_class = UserProfileSerializer

    
    def list(self, request):
        queryset = AquaProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        print("User in list:", self.request.user)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        print("User in retrieve:", pk)
        queryset = AquaProfile.objects.all()
        userProfile = get_object_or_404(queryset, pk=pk)
        serializer = UserProfileSerializer(userProfile)
        return Response(serializer.data)
    
    def create(self, request):
        return Response({"error": "Read only"}, status=status.HTTP_403_FORBIDDEN)
    
    def update(self, request, pk=None):
        if self.request.user.is_superuser:
            queryset = AquaProfile.objects.all()
            userProfile = get_object_or_404(queryset, pk=pk)
            
            serializer = UserProfileSerializer(userProfile, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Read only"}, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        return Response({"error": "Read only"}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        return Response({"error": "Read only"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk=None):
        return Response({"error": "Read only"}, status=status.HTTP_403_FORBIDDEN)
