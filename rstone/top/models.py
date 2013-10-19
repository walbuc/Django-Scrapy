from django.template.defaultfilters import slugify
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from albums.models import Album
from artists.models import Artist


class Ranking(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(editable=False,unique=True)
    def __unicode__(self):
        return u"%s"%self.title
    
    def get_absolute_url(self):
        return reverse('rankings:detail',args=[self.slug])
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Ranking,self).save()
    

from polymorphic import PolymorphicModel

class Top(PolymorphicModel):
    ranking=models.ForeignKey(Ranking,related_name='positions')
    position=models.PositiveIntegerField()
    site_url=models.URLField(blank=True,null=True)
    class Meta:
        ordering=('position',)

class TopAlbum(Top):
    album=models.ForeignKey(Album,related_name='in_rankings')
    def __unicode__(self):
        return u"%s | %s"%(self.position, self.album)
    

class TopArtist(Top):
    artist=models.ForeignKey(Artist,related_name='in_rankings')
    def __unicode__(self):
        return u"%s | %s"%(self.position, self.artist)
    
    