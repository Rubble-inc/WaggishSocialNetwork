from django.db import models
from user.models import Person


class Message(models.Model):
    text = models.TextField(max_length=200)

class Chat(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Person, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.PROTECT)


class Members(models.Model):
    users = models.ForeignKey(Person, on_delete=models.PROTECT)
    chat = models.OneToOneField(Chat, on_delete=models.CASCADE)




