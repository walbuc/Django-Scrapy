from artists.models import Artist
from tastypie.resources import ModelResource
from tastypie import fields

class ArtistResource(ModelResource):
    class Meta:
        queryset = Artist.objects.all()
        resource_name = 'artists'
