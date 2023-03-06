
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class SocialSegment(models.Model):

    name = models.CharField("Name", max_length=50, unique=True)
    aquarium_object = models.ForeignKey('biocalc.AquaBaseItem', on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.ManyToManyField(User, through='Comment', related_name='social_segments', blank=True)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Social segment", kwargs={"pk": self.pk})
