from django.contrib.gis import admin

from artists.models import *

class ArtistAdmin(admin.ModelAdmin):
	list_display=('name','role')

admin.site.register(Artist,ArtistAdmin)