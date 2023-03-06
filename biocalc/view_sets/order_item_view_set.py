from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from biocalc.models import OrderItem, Order
from biocalc.serializers import OrderItemSerializer
from biocalc.permissions import IsOrderItemByBuyerOrAdmin, IsOrderItemPending

class OrderItemViewSet(viewsets.ModelViewSet):
    """
    CRUD order items that are associated with the current order id.
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsOrderItemByBuyerOrAdmin]

    def get_queryset(self):
        res = super().get_queryset()
        order_id = self.kwargs.get('order_id')
        return res.filter(order__id=order_id)

    def perform_create(self, serializer):
        order = get_object_or_404(Order, id=self.kwargs.get('order_id'))
        serializer.save(order=order)

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            self.permission_classes += [IsOrderItemPending]

        return super().get_permissions()

