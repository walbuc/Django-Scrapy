from django.contrib.gis import admin

from top.models import *

class TopAlbumAdmin(admin.ModelAdmin):
	list_display=('ranking','position','title','band')
	search_fields=('album__name','album__band__name')
	def title(self,obj):
		return obj.album.name
	
	def band(self,obj):
		return obj.album.band

class TopArtistAdmin(admin.ModelAdmin):
	list_display=('ranking','position','title')
	def title(self,obj):
		return obj.artist.name
	

class TopAdmin(admin.ModelAdmin):
    list_display=('ranking','position')
    list_filter=('ranking',)
    
admin.site.register(Ranking)
admin.site.register(Top,TopAdmin)
admin.site.register(TopAlbum,TopAlbumAdmin)
admin.site.register(TopArtist,TopArtistAdmin)