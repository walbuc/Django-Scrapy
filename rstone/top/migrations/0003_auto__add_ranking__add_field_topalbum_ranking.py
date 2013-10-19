# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Ranking'
        db.create_table('top_ranking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('top', ['Ranking'])

        # Adding field 'TopAlbum.ranking'
        db.add_column('top_topalbum', 'ranking', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='albums', to=orm['top.Ranking']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Ranking'
        db.delete_table('top_ranking')

        # Deleting field 'TopAlbum.ranking'
        db.delete_column('top_topalbum', 'ranking_id')


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
            'had_it': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ranking': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': "orm['top.Ranking']"})
        }
    }

    complete_apps = ['top']
