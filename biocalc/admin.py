from django.contrib import admin

from .models import (
    AquaProfile,
    Plant,
    Fish, 
    Tank,
    PlantCategory,
    FishCategory,
    Comment,
    ItemGalleryImage,
    ItemSellingData,
    Order,
    OrderItem,
    SocialSegment,
    Payment,
    Address,
    PhoneNumber,
    )

admin.site.register(AquaProfile)
admin.site.register(Fish)
admin.site.register(Plant)

@admin.register(FishCategory)
class FishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
@admin.register(PlantCategory)
class PlantCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Comment)
admin.site.register(ItemGalleryImage)
admin.site.register(ItemSellingData)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(SocialSegment)

admin.site.register(Payment)

admin.site.register(Address)
admin.site.register(PhoneNumber)