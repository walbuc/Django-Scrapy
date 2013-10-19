from django.contrib.gis import admin
from albums.models import *

class AlbumAdmin(admin.ModelAdmin):
    list_display=('name','band')

admin.site.register(Band)
admin.site.register(Album,AlbumAdmin)