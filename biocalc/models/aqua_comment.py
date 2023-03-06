
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Comment(models.Model):
    social_segment = models.ForeignKey("biocalc.SocialSegment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def get_absolute_url(self):
        return reverse("Comment", kwargs={"pk": self.pk})