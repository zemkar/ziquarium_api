
from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _


class IsOrderPendingWhenCheckout(BasePermission):
    """
    Check the status of order is pending or completed before updating instance
    """
    message = _('Updating closed order is not allowed.')

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET',):
            return True
        return obj.status == 'P'