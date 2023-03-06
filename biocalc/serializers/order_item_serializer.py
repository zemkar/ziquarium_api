
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from biocalc.models import Order, OrderItem, ItemSellingData
from django.utils.translation import gettext_lazy as _


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing order items
    """
    price = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity',
                  'price', 'cost', 'created_at', 'updated_at', )
        read_only_fields = ('order', )

    def validate(self, validated_data):
        print(validated_data)
        order_quantity = validated_data['quantity']
        # product_quantity = validated_data['product'].quantity

        order_id = self.context['view'].kwargs.get('order_id')
        product = validated_data['product']
        current_item = OrderItem.objects.filter(
            order__id=order_id, product=product)

        # if(order_quantity > product_quantity):
        #     error = {'quantity': _('Ordered quantity is more than the stock.')}
        #     raise serializers.ValidationError(error)

        if not self.instance and current_item.count() > 0:
            error = {'product': _('Product already exists in your order.')}
            raise serializers.ValidationError(error)

        # if self.context['request'].user == product.seller:
        #     error = _('Adding your own product to your order is not allowed')
        #     raise PermissionDenied(error)

        return validated_data

    def get_price(self, obj):
        sellingData = ItemSellingData.objects.get(shop_item = obj.pk)
        return sellingData.price

    def get_cost(self, obj):
        return obj.cost
