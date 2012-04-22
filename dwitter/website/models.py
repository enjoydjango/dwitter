from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Tweet(models.Model):
    message = models.TextField(blank=True, max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.message


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    bio = models.CharField(blank=True, max_length=200)
    followers = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="following")

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
