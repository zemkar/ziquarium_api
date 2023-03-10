
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
        fields = ('id', 'order', 'product', 'quantity', 'product_name',
                  'price', 'cost', 'created_at', 'updated_at', )
        read_only_fields = ('order', )

    def validate(self, validated_data):
        print(validated_data)
        order_quantity = validated_data['quantity']
        product = validated_data['product']
        try: 
            saleData = ItemSellingData.objects.get(shop_item = product)
            product_quantity = saleData.quantity
        except: product_quantity = 0

        order_id = self.context['view'].kwargs.get('order_id')
        current_item = OrderItem.objects.filter(
            order__id=order_id, product=product)

        if(order_quantity > product_quantity):
            error = {'quantity': _('Ordered quantity is more than the stock.')}
            raise serializers.ValidationError(error)

        if not self.instance and current_item.count() > 0:
            error = {'product': _('Product already exists in your order.')}
            raise serializers.ValidationError(error)


        return validated_data

    def get_price(self, obj):
        try:
            sellingData = ItemSellingData.objects.get(shop_item = obj.product)
            return sellingData.get_price()
        except:
            return 0

    def get_cost(self, obj):
        try:
            return obj.cost
        except: 
            return None
