from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    bio = models.CharField(blank=True, max_length=200)

    def __unicode__(self):
        return self.user.username


class Tweet(models.Model):
    message = models.TextField(blank=True, max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.message
