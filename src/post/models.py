from django.db import models

from user.models import UserProfile


class Post(models.Model):
    text = models.TextField()
    user_id = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='media/photos/', blank=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
