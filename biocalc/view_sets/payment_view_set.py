
from rest_framework.viewsets import ModelViewSet
from biocalc.models import Payment
from biocalc.serializers import PaymentSerializer
from biocalc.permissions import IsPaymentByUser, IsPaymentPending



class PaymentViewSet(ModelViewSet):
    """
    CRUD payment for an order
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsPaymentByUser]

    def get_queryset(self):
        res = super().get_queryset()
        user = self.request.user
        return res.filter(order__buyer=user)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes += [IsPaymentPending]

        return super().get_permissions()
