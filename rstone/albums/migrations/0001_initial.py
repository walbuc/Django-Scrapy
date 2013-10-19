# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Band'
        db.create_table('albums_band', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('albums', ['Band'])

        # Adding model 'Album'
        db.create_table('albums_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cover', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('band', self.gf('django.db.models.fields.related.ForeignKey')(related_name='albums', to=orm['albums.Band'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('albums', ['Album'])

    def backwards(self, orm):
        
        # Deleting model 'Band'
        db.delete_table('albums_band')

        # Deleting model 'Album'
        db.delete_table('albums_album')

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
        }
    }

    complete_apps = ['albums']
