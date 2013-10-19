from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _ 
from django.template.defaultfilters import slugify

from model_utils import Choices

# Create your models here.
class Artist(models.Model):
    ROLES=Choices(
        ('singer',_('Singer')),
        ('guitarrist',_('Guitarrist'))
    )
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(editable=False)
    role=models.CharField(max_length=20,choices=ROLES)
    class Meta:
        ordering=('name',)
    
    def get_absolute_url(self):
        return reverse('artists:detail',args=[self.slug])
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Artist,self).save()
    
    def __unicode__(self):
        return u"%s"%self.name
    
