# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Ranking', fields ['slug']
        db.create_unique('top_ranking', ['slug'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Ranking', fields ['slug']
        db.delete_unique('top_ranking', ['slug'])


    models = {
        'albums.album': {
            'Meta': {'unique_together': "(('band', 'name'),)", 'object_name': 'Album'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': "orm['albums.Band']"}),
            'cover': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'albums.band': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Band'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'artists.artist': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'top.ranking': {
            'Meta': {'object_name': 'Ranking'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'top.top': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Top'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_top.top_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ranking': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['top.Ranking']"}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'top.topalbum': {
            'Meta': {'ordering': "('position',)", 'object_name': 'TopAlbum', '_ormbases': ['top.Top']},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_rankings'", 'to': "orm['albums.Album']"}),
            'top_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['top.Top']", 'unique': 'True', 'primary_key': 'True'})
        },
        'top.topartist': {
            'Meta': {'ordering': "('position',)", 'object_name': 'TopArtist', '_ormbases': ['top.Top']},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_rankings'", 'to': "orm['artists.Artist']"}),
            'top_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['top.Top']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['top']
