from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Friendship(models.Model):
    user_id = models.IntegerField()
    accepted = models.BooleanField(default=False)


class Person(AbstractUser):
    photo = models.ImageField(blank=True, upload_to='media/photos/')
    friends = models.ForeignKey(Friendship, related_name='friends', on_delete=models.PROTECT, blank=True)


class UserProfile(models.Model):
    info = models.TextField(blank=True)
    user = models.OneToOneField(Person, on_delete=models.CASCADE)











