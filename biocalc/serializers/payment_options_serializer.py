from rest_framework import serializers
from biocalc.models import Payment


class PaymentOptionSerializer(serializers.ModelSerializer):
    """
    Payment serializer for checkout. Order will be automatically set during checkout.
    """
    buyer = serializers.CharField(
        source='order.buyer.get_full_name', read_only=True)

    class Meta:
        model = Payment
        fields = ('id', 'buyer', 'status', 'payment_option',
                  'order', 'created_at', 'updated_at')
        read_only_fields = ('status', 'order')

