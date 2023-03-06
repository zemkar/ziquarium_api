
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _

from biocalc.models import Order

class IsPaymentForOrderNotCompleted(BasePermission):
    message = _(
        'Creating a checkout session for completed payment is not allowed.')

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            order_id = view.kwargs.get('order_id')
            order = get_object_or_404(Order, id=order_id)
            return order.status != 'C'
        return False