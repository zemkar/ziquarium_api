
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _

from biocalc.models import Order

class DoesOrderHaveAddress(BasePermission):
    message = _(
        'Creating a checkout session without having a shipping and billing address is not allowed.')

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            order_id = view.kwargs.get('order_id')
            order = get_object_or_404(Order, id=order_id)
            return order.shipping_address and order.billing_address
        return False
