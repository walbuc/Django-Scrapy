# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TopArtist'
        db.create_table('top_topartist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ranking', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['top.Ranking'])),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('site_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='in_rankings', to=orm['artists.Artist'])),
        ))
        db.send_create_signal('top', ['TopArtist'])

        # Adding unique constraint on 'TopArtist', fields ['ranking', 'artist']
        db.create_unique('top_topartist', ['ranking_id', 'artist_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'TopArtist', fields ['ranking', 'artist']
        db.delete_unique('top_topartist', ['ranking_id', 'artist_id'])

        # Deleting model 'TopArtist'
        db.delete_table('top_topartist')


    models = {
        'albums.album': {
            'Meta': {'unique_together': "(('band', 'name'),)", 'object_name': 'Album'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': "orm['albums.Band']"}),
            'cover': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        'top.ranking': {
            'Meta': {'object_name': 'Ranking'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'top.topalbum': {
            'Meta': {'unique_together': "(('ranking', 'album'),)", 'object_name': 'TopAlbum'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_rankings'", 'to': "orm['albums.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ranking': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['top.Ranking']"}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'top.topartist': {
            'Meta': {'unique_together': "(('ranking', 'artist'),)", 'object_name': 'TopArtist'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_rankings'", 'to': "orm['artists.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ranking': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['top.Ranking']"}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['top']
