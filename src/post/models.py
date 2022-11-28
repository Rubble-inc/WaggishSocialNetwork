from django.db import models


class Post(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='media/photos/', blank=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
