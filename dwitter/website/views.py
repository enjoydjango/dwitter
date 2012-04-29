from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from website.models import Tweet
from website.forms import TweetForm


def timeline(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            t = Tweet()
            t.user = request.user
            t.message = form.cleaned_data['message']
            t.save()
            return HttpResponseRedirect("/")
    else:
        form = TweetForm()
    tweets = Tweet.objects.all().order_by('-timestamp')
    return render(request, 'website/index.html', {'tweets': tweets, 'form': form})


def tweet_page(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, 'website/tweet_page.html', {'tweet': tweet})


def user_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'website/user_page.html', {'page_user': user})


def users_list(request):
    users = User.objects.all()
    return render(request, 'website/users_list.html', {'users': users})


def toggle_follow(request, username):
    profile = get_object_or_404(User, username=username).profile

    if profile == request.user.profile:
        return HttpResponseRedirect(reverse('timeline'))

    if profile in request.user.profile.following.all():
        request.user.profile.following.remove(profile)
    else:
        request.user.profile.following.add(profile)

    return HttpResponseRedirect(reverse('user-page', args=[request.user.username]))
