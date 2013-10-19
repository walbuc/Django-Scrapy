from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('artists.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<slug_artist>[a-zA-Z0-9_.-]+)/$', 'detail', name='detail'),
)
