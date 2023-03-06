from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrderByBuyerOrAdmin(BasePermission):
    """
    Check if order is owned by appropriate buyer or admin
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated is True

    def has_object_permission(self, request, view, obj):
        return obj.buyer == request.user or request.user.is_superuser
