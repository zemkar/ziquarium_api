

from rest_framework.generics import RetrieveUpdateAPIView
from biocalc.models import Order
from biocalc.serializers import CheckoutSerializer
from biocalc.permissions import IsOrderByBuyerOrAdmin, IsOrderPendingWhenCheckout


class CheckoutAPIView(RetrieveUpdateAPIView):
    """
    Create, Retrieve, Update billing address, shipping address and payment of an order
    """
    queryset = Order.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [IsOrderByBuyerOrAdmin]

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH'):
            self.permission_classes += [IsOrderPendingWhenCheckout]

        return super().get_permissions()

