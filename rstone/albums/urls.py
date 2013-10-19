from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

patterns_bands = patterns('albums.views',
    url(r'^$', 'index_bands', name='index'),
    url(r'^(?P<slug_band>[a-zA-Z0-9_.-]+)/$', 'detail_bands', name='detail'),
)
patterns_albums = patterns('albums.views',
    url(r'^$', 'index_albums', name='index'),
    url(r'^(?P<slug_album>[a-zA-Z0-9_.-]+)/$', 'detail_albums', name='detail'),
)

urlpatterns = patterns('',
    url(r'^albums/', include(patterns_albums, namespace='albums')),
    url(r'^bands/', include(patterns_bands, namespace='bands')),
)
