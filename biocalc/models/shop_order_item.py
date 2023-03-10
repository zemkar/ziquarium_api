from django.db import models
from django.utils.translation import gettext_lazy as _

from django.utils.functional import cached_property
from .shop_sale_data import ItemSellingData
from .shop_order import Order
from .aqua_base_item import AquaBaseItem as Product


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="product_orders", on_delete=models.CASCADE)
    product_name = models.CharField("product_name", max_length=200)
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.order.buyer.get_full_name()}  {self.product} {self.quantity}"

    @cached_property
    def cost(self):
        """
        Total cost of the ordered item
        """
        try:
            sellingData = ItemSellingData.objects.get(shop_item = self.product)
            return round(self.quantity * sellingData.price, 2)
        except: return 0