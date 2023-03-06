
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, pagination, status
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny, 
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    )


from biocalc.models import ItemSellingData
from biocalc.serializers import ItemSellingDataSerializer


class ItemSellingDataViewSet(viewsets.ModelViewSet):
    """
    Product cards with information for sales
    """
    queryset = ItemSellingData.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ItemSellingDataSerializer

    
    def list(self, request):
        queryset = ItemSellingData.objects.all()
        serializer = ItemSellingDataSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = ItemSellingData.objects.all()
        itemData = get_object_or_404(queryset, pk=pk)
        serializer = ItemSellingDataSerializer(itemData)
        return Response(serializer.data)
    
    def create(self, request):
        return Response({"error": "Read only"}, status=status.HTTP_403_FORBIDDEN)
    
    def update(self, request, pk=None):
        if self.request.user.is_superuser:
            queryset = ItemSellingData.objects.all()
            itemData = get_object_or_404(queryset, pk=pk)
            
            cleared_data = {"shop_item":pk}
            for field in request.data: # filter for empty fields
                if request.data[field] != '':
                    cleared_data[field] = request.data[field]
                

            serializer = ItemSellingDataSerializer(itemData, data=cleared_data, partial=True)
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
