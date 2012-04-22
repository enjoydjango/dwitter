from django.shortcuts import render

from website.models import Tweet


def timeline(request):
    tweets = Tweet.objects.all().order_by('-timestamp')
    return render(request, 'website/index.html', {'tweets': tweets})
