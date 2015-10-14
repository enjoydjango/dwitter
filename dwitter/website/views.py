from datetime import datetime
from django.shortcuts import render, get_object_or_404

from website.models import User, Tweet


def timeline(request):
    tweets = Tweet.objects.all().order_by('-timestamp')
    return render(request, 'website/index.html', {'tweets': tweets})


def tweet_page(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, 'website/tweet_page.html', {'tweet': tweet})


def user_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'website/user_page.html', {'page_user': user})
