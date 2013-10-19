from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from tastypie.models import create_api_key
post_save.connect(create_api_key, sender=User)

api=Api(api_name='v1')

from artists.api import *
api.register(ArtistResource())

from albums.api import *
api.register(BandResource())
api.register(AlbumResource())

from top.api import *
api.register(RankingResource())
api.register(TopAlbumResource())
api.register(TopArtistResource())

urlpatterns = patterns('views',
    url(r'^$', 'index', name='index'),
    url(r'^api/', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rankings/', include('top.urls', namespace='rankings')),
    url(r'^artists/', include('artists.urls', namespace='artists')),
    url(r'^', include('albums.urls')),
)
