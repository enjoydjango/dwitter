from django.shortcuts import render, get_object_or_404

from website.models import Tweet


def timeline(request):
    tweets = Tweet.objects.all().order_by('-timestamp')
    return render(request, 'website/index.html', {'tweets': tweets})


def tweet_page(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, 'website/tweet_page.html', {'tweet': tweet})
