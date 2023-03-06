from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from biocalc.models import Order, OrderItem
from biocalc.serializers import OrderItemSerializer


class OrderReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading orders
    """
    buyer = serializers.CharField(source='buyer.get_full_name', read_only=True)
    order_items = OrderItemSerializer(read_only=True, many=True)
    total_cost = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'buyer', 'shipping_address', 'billing_address', 'payment',
                  'order_items', 'total_cost', 'status', 'created_at', 'updated_at')

    def get_total_cost(self, obj):
        return obj.total_cost


class OrderWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for creating orders and order items
    Shipping address, billing address and payment are not included here
    They will be created/updated on checkout
    """
    buyer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'buyer', 'status', 'order_items',
                  'created_at', 'updated_at',)
        read_only_fields = ('status', )

    def create(self, validated_data):
        orders_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        for order_data in orders_data:
            OrderItem.objects.create(order=order, **order_data)

        return order

    def update(self, instance, validated_data):
        orders_data = validated_data.pop('order_items', None)
        orders = list((instance.order_items).all())

        if orders_data:
            for order_data in orders_data:
                order = orders.pop(0)
                order.product = order_data.get('product', order.product)
                order.quantity = order_data.get('quantity', order.quantity)
                order.save()

        return instance