from top.models import *
from albums.api import AlbumResource
from artists.api import ArtistResource
from tastypie.resources import ModelResource
from tastypie import fields

class RankingResource(ModelResource):
    class Meta:
        queryset = Ranking.objects.all()
        resource_name = 'rankings'

class TopAlbumResource(ModelResource):
    ranking=fields.ForeignKey(RankingResource,'ranking')
    album=fields.ForeignKey(AlbumResource,'album')
    class Meta:
        queryset = TopAlbum.objects.all()
        resource_name='top_albums'

class TopArtistResource(ModelResource):
    ranking=fields.ForeignKey(RankingResource, 'ranking')
    artist=fields.ForeignKey(ArtistResource,'artist')
    class Meta:
        queryset = TopArtist.objects.all()
        resource_name='top_artists'