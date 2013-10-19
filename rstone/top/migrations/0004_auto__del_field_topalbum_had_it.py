# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'TopAlbum.had_it'
        db.delete_column('top_topalbum', 'had_it')


    def backwards(self, orm):
        
        # Adding field 'TopAlbum.had_it'
        db.add_column('top_topalbum', 'had_it', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    models = {
        'albums.album': {
            'Meta': {'object_name': 'Album'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': "orm['albums.Band']"}),
            'cover': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'albums.band': {
            'Meta': {'object_name': 'Band'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'top.ranking': {
            'Meta': {'object_name': 'Ranking'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'top.topalbum': {
            'Meta': {'ordering': "('position',)", 'object_name': 'TopAlbum'},
            'album': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['albums.Album']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ranking': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': "orm['top.Ranking']"})
        }
    }

    complete_apps = ['top']
