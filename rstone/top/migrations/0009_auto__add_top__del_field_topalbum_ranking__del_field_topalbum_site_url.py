# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'TopArtist', fields ['ranking', 'artist']
        db.delete_unique('top_topartist', ['ranking_id', 'artist_id'])

        # Removing unique constraint on 'TopAlbum', fields ['album', 'ranking']
        db.delete_unique('top_topalbum', ['album_id', 'ranking_id'])

        # Adding model 'Top'
        db.create_table('top_top', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_top.top_set', null=True, to=orm['contenttypes.ContentType'])),
            ('ranking', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['top.Ranking'])),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('site_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('top', ['Top'])

        # Deleting field 'TopAlbum.ranking'
        db.delete_column('top_topalbum', 'ranking_id')

        # Deleting field 'TopAlbum.site_url'
        db.delete_column('top_topalbum', 'site_url')

        # Deleting field 'TopAlbum.position'
        db.delete_column('top_topalbum', 'position')

        # Deleting field 'TopAlbum.id'
        db.delete_column('top_topalbum', 'id')

        # Adding field 'TopAlbum.top_ptr'
        db.add_column('top_topalbum', 'top_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['top.Top'], unique=True, primary_key=True), keep_default=False)

        # Deleting field 'TopArtist.ranking'
        db.delete_column('top_topartist', 'ranking_id')

        # Deleting field 'TopArtist.site_url'
        db.delete_column('top_topartist', 'site_url')

        # Deleting field 'TopArtist.position'
        db.delete_column('top_topartist', 'position')

        # Deleting field 'TopArtist.id'
        db.delete_column('top_topartist', 'id')

        # Adding field 'TopArtist.top_ptr'
        db.add_column('top_topartist', 'top_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['top.Top'], unique=True, primary_key=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Top'
        db.delete_table('top_top')

        # User chose to not deal with backwards NULL issues for 'TopAlbum.ranking'
        raise RuntimeError("Cannot reverse this migration. 'TopAlbum.ranking' and its values cannot be restored.")

        # Adding field 'TopAlbum.site_url'
        db.add_column('top_topalbum', 'site_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'TopAlbum.position'
        raise RuntimeError("Cannot reverse this migration. 'TopAlbum.position' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'TopAlbum.id'
        raise RuntimeError("Cannot reverse this migration. 'TopAlbum.id' and its values cannot be restored.")

        # Deleting field 'TopAlbum.top_ptr'
        db.delete_column('top_topalbum', 'top_ptr_id')

        # Adding unique constraint on 'TopAlbum', fields ['album', 'ranking']
        db.create_unique('top_topalbum', ['album_id', 'ranking_id'])

        # User chose to not deal with backwards NULL issues for 'TopArtist.ranking'
        raise RuntimeError("Cannot reverse this migration. 'TopArtist.ranking' and its values cannot be restored.")

        # Adding field 'TopArtist.site_url'
        db.add_column('top_topartist', 'site_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'TopArtist.position'
        raise RuntimeError("Cannot reverse this migration. 'TopArtist.position' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'TopArtist.id'
        raise RuntimeError("Cannot reverse this migration. 'TopArtist.id' and its values cannot be restored.")

        # Deleting field 'TopArtist.top_ptr'
        db.delete_column('top_topartist', 'top_ptr_id')

        # Adding unique constraint on 'TopArtist', fields ['ranking', 'artist']
        db.create_unique('top_topartist', ['ranking_id', 'artist_id'])


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
