from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    bio = models.CharField(blank=True, max_length=200)
    followers = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="following")

    def __unicode__(self):
        return self.username


class Tweet(models.Model):
    message = models.TextField(blank=True, max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="tweets")

    def __unicode__(self):
        return self.message
