
from django.db import models
from django.db.models.signals import post_save


class ItemSellingData(models.Model):
    """
    Related model of data for selling.

    contain:\n
        :key shop_item -               Related field | 
        :key price -                   DecimalField | Price
        :key quantity -                PositiveIntegerField | Quantity in shop
        :key quantity_for_discount  -  PositiveSmallIntegerField | Quantity in order for the discount.
        :key quantity_discount  -      DecimalField | % of discount for quantity.
        :key sale_status -             BooleanField | Sale status
        :key sale_discount -           DecimalField | % of discount for sale.
        :key sale_end_date -           Date field, | Sale end date
    """
    shop_item = models.OneToOneField("biocalc.AquaBaseItem", on_delete=models.CASCADE, related_name='shop_item')
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    quantity_for_discount = models.PositiveSmallIntegerField(default=0)
    quantity_discount = models.IntegerField(default=0)
    sale_status = models.BooleanField(default=False)
    sale_discount = models.IntegerField(default=0)
    sale_end_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.shop_item} "
