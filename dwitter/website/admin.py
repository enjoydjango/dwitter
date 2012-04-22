from django.contrib import admin
from website.models import Tweet, Profile


class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'timestamp')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Profile, ProfileAdmin)
