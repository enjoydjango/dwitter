from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Tweet(models.Model):
    message = models.TextField(blank=True, max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.message
