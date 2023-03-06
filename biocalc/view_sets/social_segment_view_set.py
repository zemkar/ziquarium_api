
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, pagination, status
from rest_framework.response import Response
from biocalc.models import SocialSegment
from biocalc.serializers import SocialSegmentSerializer

from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny, 
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    )



class SocialSegmentViewSet(viewsets.ModelViewSet):
    """
    Rating and comments of item.

    Created automatically for each new item.

    Can be read or changed. 

    Cannot be created or deleted manually.
    """
    queryset = SocialSegment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SocialSegmentSerializer

    
    def list(self, request):
        queryset = SocialSegment.objects.all()
        serializer = SocialSegmentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = SocialSegment.objects.all()
        socialSegment = get_object_or_404(queryset, pk=pk)
        serializer = SocialSegmentSerializer(socialSegment)
        return Response(serializer.data)
    
    def create(self, request):
        return Response({"error": "Read only"}, status=status.HTTP_403_FORBIDDEN)
    
    def update(self, request, pk=None):
        if self.request.user.is_superuser:
            queryset = SocialSegment.objects.all()
            socialSegment = get_object_or_404(queryset, pk=pk)
            
            serializer = SocialSegmentSerializer(socialSegment, data=request.data, partial=True)
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
