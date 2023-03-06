
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, pagination, status
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny, 
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    )

from .data_cleaner_func import data_cleaner
from biocalc.models import Fish
from biocalc.serializers import FishSerializer


class FishViewSet(viewsets.ModelViewSet):
    """
    For CRUD of operations on an fish.
    """
    queryset = Fish.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FishSerializer
    # TODO TODO TODO
    # pagination_class = CustomFishPagination
    # TODO TODO TODO    

    
    def retrieve(self, request, pk=None):
        queryset = Fish.objects.all()
        fish = get_object_or_404(queryset, pk=pk)
        if fish and not fish.approved:
            if self.request.user.is_authenticated:
                if self.request.user.is_superuser or self.request.user == fish.user_placeholder or self.request.user == fish.latest_editor:
                    serializer = FishSerializer(fish)
                    return Response(serializer.data)
        elif fish:
            serializer = FishSerializer(fish)
            return Response(serializer.data)
        return Response({"error": "sorry, is no publicly available data for this object"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def list(self, request):
        queryset = Fish.objects.all()

        if self.request.user.is_authenticated:
            print("user is_authenticated", self.request.user)
            if self.request.user.is_superuser: pass
            else: queryset = queryset.filter(Q(approved=True) | Q(user_placeholder=self.request.user) | Q(latest_editor=self.request.user))
        else:
            queryset = queryset.filter(approved=True)

        serializer = FishSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        
        cleared_data = data_cleaner(request.data, "Fish", self.request.user.id)
        serializer = FishSerializer(data=cleared_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    # def update(self, request, pk=None):
        
    def update(self, request, *args, **kwargs):
        partial = True # Here I change partial to True
        instance = self.get_object()
        if instance:
            cleared_data = data_cleaner(request.data, "Fish", self.request.user.id, instance)
            serializer = FishSerializer(instance, data=cleared_data, partial=partial)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        return Response(status=status.HTTP_404_NOT_FOUND)
