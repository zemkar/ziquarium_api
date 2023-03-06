from rest_framework import viewsets
from biocalc.models import Order
from biocalc.serializers import OrderReadSerializer, OrderWriteSerializer
from biocalc.permissions import IsOrderPending, IsOrderByBuyerOrAdmin

class OrderViewSet(viewsets.ModelViewSet):
    """
    CRUD orders of a user
    """
    queryset = Order.objects.all()
    permission_classes = [IsOrderByBuyerOrAdmin]

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return OrderWriteSerializer

        return OrderReadSerializer

    def get_queryset(self):
        res = super().get_queryset()
        user = self.request.user
        return res.filter(buyer=user)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes += [IsOrderPending]

        return super().get_permissions()