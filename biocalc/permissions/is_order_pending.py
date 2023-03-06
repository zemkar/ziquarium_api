
from rest_framework.permissions import BasePermission

from django.utils.translation import gettext_lazy as _

class IsOrderPending(BasePermission):
    """
    Check the status of order is pending or completed before updating/deleting instance
    """
    message = _('Updating or deleting closed order is not allowed.')

    def has_object_permission(self, request, view, obj):
        if view.action in ('retrieve',):
            return True
        return obj.status == 'P'