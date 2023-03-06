


class IsPaymentByUser(BaseException):
    """
    Check if payment belongs to the appropriate buyer or admin
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated is True

    def has_object_permission(self, request, view, obj):
        return obj.order.buyer == request.user or request.user.is_superuser
