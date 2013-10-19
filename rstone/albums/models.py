from django.core.urlresolvers import reverse
from django.contrib.gis.db import models
from django.template.defaultfilters import slugify

class Band(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(editable=False)
    class Meta:
        ordering=ordering=('name',)
    
    def get_absolute_url(self):
        return reverse('bands:detail',args=[self.slug])
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Band,self).save()
    
    def __unicode__(self):
        return u"%s"%(self.name,)

class Album(models.Model):
    band=models.ForeignKey(Band,related_name='albums')
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(editable=False)
    cover=models.CharField(max_length=250)
    description=models.TextField()
    class Meta:
        unique_together=(('band','name'),)
    
    def get_absolute_url(self):
        return reverse('albums:detail',args=[self.slug])
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Album,self).save()
    
    def __unicode__(self):
        return u"%s - %s"%(self.name,self.band)
