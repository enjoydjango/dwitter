from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dwitter.views.home', name='home'),
    # url(r'^dwitter/', include('dwitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tweet/(\d+)/$', 'website.views.tweet_page', name='tweet-page'),
    url(r'^user/(\w+)/$', 'website.views.user_page', name='user-page'),
    url(r'^$', 'website.views.timeline', name='timeline'),
)
