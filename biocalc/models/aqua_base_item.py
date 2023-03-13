import os
import shutil
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


def path_rename(instance, filename):
    ext = filename.split('.')[-1]
    return f'{instance.id}\{instance.name}.{ext}'

class AquaBaseItem(models.Model):
    """
    Base model of any Ziquarium item

    Contain:
        :key name              - name of item
        :key slug              - unique part of link to an item
        :key image             - cover picture
        :key gallery           - gallery of an item
        :key user_placeholder  - user who created an item
        :key latest_editor     - user who last edited an item
        :key approving_user    - user who approved publication of the item
        :key approved          - flag if approved
        :key created_at        - date and time of creation
        :key edited_at         - date and time of last edition
        :key approved_at       - date and time of approval
        :key description       - some descriptions
    
    - Slug is automatically generated from the item name.
    - When an item is removed, the cover is also removed.
    - If a picture is uploaded, then it is 
    saved after the object is created and received an ID.
    - When deleting an object, the gallery folder is also deleted from the server
    """

    TYPE_CATEGORIES = (
        ('Undefined', 'Undefined'), 
        ('Another', 'Another'), 
        ('Fish', 'Fish'), 
        ('Plant', 'Plant'), 
        ('Equipment', 'Equipment'), 
        )

    name = models.CharField(
        "Name", 
        max_length=50,
        unique=True)
    
    type_category = models.CharField(
        choices=TYPE_CATEGORIES, 
        max_length=20, 
        default="Undefined") 
    
    slug = models.SlugField(
        max_length=100, 
        unique=True, 
        db_index=True,
        blank=True, null=True) 
    
    image = models.ImageField(
        upload_to=path_rename,
        blank=True, null=True,
        height_field=None, 
        width_field=None, 
        max_length=None)
    
    gallery = models.ManyToManyField(
        "biocalc.ItemGalleryImage",
        blank=True)

    user_placeholder = models.ForeignKey(
        User, 
        related_name="placeholder", 
        verbose_name="Placeholder", 
        on_delete=models.SET_NULL, 
        null=True, blank=True)
    
    latest_editor = models.ForeignKey(
        User, 
        related_name="latest_editor", 
        verbose_name="latest_editor", 
        on_delete=models.SET_NULL, 
        null=True, blank=True)
    

    approving_user = models.ForeignKey(
        User, 
        related_name="acceptor", 
        verbose_name="Acceptor", 
        on_delete=models.SET_NULL, 
        null=True, blank=True)
    
    approved  = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now=True)

    edited_at = models.DateTimeField(auto_now_add=True)

    approved_at = models.DateTimeField(null=True, blank=True)

    description = models.TextField(
        "description", 
        max_length=2000, 
        blank=True)

    def __str__(self) -> str:
        return f"{self.id}) {self.type_category} {self.name}"

    def get_absolute_url(self):
        return reverse("biocalc:AquaBaseItem", kwargs={'pk':str(self.pk), 'slug':self.slug}) #[self.id, self.slug])
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if not self.pk:
            if self.image:
                # save without image and add it after saving in update field
                image = self.image
                print(f"save without image: {image}")
                self.image = None
                super(AquaBaseItem, self).save(*args, **kwargs)
                if self.pk:
                    self.image = image
                    print(f"add image: {image}")
                    super(AquaBaseItem, self).save(update_fields=['image'])
        super(AquaBaseItem, self).save()


    def delete(self, *args, **kwargs):
        file_location = os.path.join(settings.MEDIA_ROOT, str(self.pk))
        shutil.rmtree(file_location, ignore_errors = True)
        super(AquaBaseItem,self).delete(*args,**kwargs)

