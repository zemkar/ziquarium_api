
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

def product_image_path(instance, filename):
    return f'{instance.aqua_item.id}/gallery/{filename}'


class ItemGalleryImage(models.Model):
    aqua_item = models.ForeignKey("biocalc.AquaBaseItem", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path, blank=True, null=True, default='/media/SomeItem.png')

    # def delete(self, *args, **kwargs):
    #     # удаление изображения при удалении его записи в базе данных
    #     self.image.delete()
    #     super(ItemGalleryImage, self).delete(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # удаление старого изображения при обновлении записи
    #     try:
    #         this = ItemGalleryImage.objects.get(id=self.id)
    #         if this.image != self.image:
    #             this.image.delete()
    #     except:
    #         pass
    #     super(ItemGalleryImage, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']