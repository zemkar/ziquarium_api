
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from biocalc.models import Order


class IsOrderItemByBuyerOrAdmin(BasePermission):
    """
    Check if order item is owned by appropriate buyer or admin
    """

    def has_permission(self, request, view):
        order_id = view.kwargs.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        return order.buyer == request.user or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.order.buyer == request.user or request.user.is_superuser
