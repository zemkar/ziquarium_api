
import os
import shutil
from django.conf import settings
from .aqua_item_gallery import ItemGalleryImage
from .plant import Plant
from .fish import Fish
from .aqua_user_profile import AquaProfile
from .shop_sale_data import ItemSellingData
from .aqua_social_segment import SocialSegment


from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver



@receiver(post_save, sender=Fish)
def create_fish_additional_table(sender, instance, created, **kwargs):
    if created:
        ItemSellingData.objects.create(shop_item=instance)
        SocialSegment.objects.create(name=instance.name, aquarium_object=instance)

@receiver(post_save, sender=Plant)
def create_plant_additional_table(sender, instance, created, **kwargs):
    if created:
        ItemSellingData.objects.create(shop_item=instance)
        SocialSegment.objects.create(name=instance.name, aquarium_object=instance)

@receiver(pre_delete, sender=ItemGalleryImage)
def image_pre_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(pre_save, sender=ItemGalleryImage)
def image_pre_save(sender, instance, **kwargs):
    try:
        old_image = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False
    
    if old_image.image != instance.image:
        old_image.image.delete(False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        AquaProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(f"save_user_profile.instance: {instance}")
    instance.profile.save()
