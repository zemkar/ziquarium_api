
from rest_framework import viewsets
from biocalc.models import Address
from biocalc.serializers import AddressReadOnlySerializer
from biocalc.permissions import IsUserAddressOwner

class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve user addresses
    """
    queryset = Address.objects.all()
    serializer_class = AddressReadOnlySerializer
    permission_classes = (IsUserAddressOwner,)

    def get_queryset(self):
        res = super().get_queryset()
        user = self.request.user
        return res.filter(user=user)