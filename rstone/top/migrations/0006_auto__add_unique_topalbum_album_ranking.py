# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'TopAlbum', fields ['album', 'ranking']
        db.create_unique('top_topalbum', ['album_id', 'ranking_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'TopAlbum', fields ['album', 'ranking']
        db.delete_unique('top_topalbum', ['album_id', 'ranking_id'])


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
            'Meta': {'ordering': "('position',)", 'unique_together': "(('ranking', 'album'),)", 'object_name': 'TopAlbum'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_rankings'", 'to': "orm['albums.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ranking': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': "orm['top.Ranking']"})
        }
    }

    complete_apps = ['top']
