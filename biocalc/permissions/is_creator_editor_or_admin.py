from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCreatorEditorOrAdmin(BasePermission):
    """
    Check if authenticated user is seller of the product or admin
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated is True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user in (obj.user_placeholder, obj.latest_editor) or request.user.is_superuser