from albums.models import *
from tastypie.resources import ModelResource
from tastypie import fields

class BandResource(ModelResource):
    class Meta:
        queryset = Band.objects.all()
        resource_name = 'bands'

class AlbumResource(ModelResource):
    band=fields.ForeignKey(BandResource,'band')
    class Meta:
        queryset = Album.objects.all()
        resource_name='albums'
