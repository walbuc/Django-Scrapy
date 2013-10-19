# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Artist.slug'
        db.add_column('artists_artist', 'slug', self.gf('django.db.models.fields.SlugField')(default=1, max_length=50, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Artist.slug'
        db.delete_column('artists_artist', 'slug')


    models = {
        'artists.artist': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['artists']
