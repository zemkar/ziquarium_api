

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, pagination, status
from django.contrib.auth.models import User

from biocalc.models import (
    Tank,
    FishCategory,
    PlantCategory,
    Comment,
    ItemGalleryImage,
    )
from biocalc.permissions import is_superuser
from biocalc.serializers import (
    UserSerializer,
    FishCategorySerializer,
    TankSerializer,
    PlantCategorySerializer,
    CommentSerializer,
    ItemGalleryImageSerializer,
    )

from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny, 
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    )






class ItemGalleryImageViewSet(viewsets.ModelViewSet):
    """
    Image for gallery of item
    """
    queryset = ItemGalleryImage.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ItemGalleryImageSerializer        

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (is_superuser,)
    serializer_class = UserSerializer

class FishCategoryViewSet(viewsets.ModelViewSet):
    queryset = FishCategory.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FishCategorySerializer

class PlantCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlantCategory.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PlantCategorySerializer

class TankViewSet(viewsets.ModelViewSet):
    queryset = Tank.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TankSerializer

