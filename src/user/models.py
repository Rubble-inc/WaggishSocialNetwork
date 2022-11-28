from django.contrib.auth.models import AbstractUser
from django.db import models

from post.models import Post


class Friendship(models.Model):
    user_id = models.IntegerField()
    accepted = models.BooleanField(default=False)


class Person(AbstractUser):
    photo = models.ImageField(blank=True, upload_to='media/photos/')
    friends = models.ForeignKey(Friendship, related_name='friends', on_delete=models.PROTECT, blank=True, null=True)


class UserProfile(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    info = models.TextField(blank=True)
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
