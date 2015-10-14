from django.contrib import admin
from website.models import Tweet, User


class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'timestamp')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'bio')


admin.site.register(Tweet, TweetAdmin)
admin.site.register(User, UserAdmin)
