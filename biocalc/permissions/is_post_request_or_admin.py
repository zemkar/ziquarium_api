
from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _

class IsPostRequestOrAdmin(BasePermission):
    """
    Allow POST requests for any, or any request for admin
    """

    message = _(
        'Only for creating entries.')
    
    def has_permission(self, request, view):
        if request.method =='POST' or (request.user and request.user.is_superuser): 
            return True 
        return False