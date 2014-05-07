# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

	def forwards(self, orm):
		# Adding model 'Website'
		db.create_table('event_website', (
			('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
			('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Event'])),
			('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
			('is_archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
			('mailchimp_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
			('facebook_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
			('twitter_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
			('gplus_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
		))
		db.send_create_signal('event', ['Website'])

		# Adding model 'Event'
		db.create_table('event_event', (
			('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
			('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
			('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
			('date', self.gf('django.db.models.fields.DateField')()),
			('main_organizer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_organizer', to=orm['event.Organizer'])),
			('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
		))
		db.send_create_signal('event', ['Event'])

		# Adding M2M table for field team on 'Event'
		m2m_table_name = db.shorten_name('event_event_team')
		db.create_table(m2m_table_name, (
			('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
			('event', models.ForeignKey(orm['event.event'], null=False)),
			('organizer', models.ForeignKey(orm['event.organizer'], null=False))
		))
		db.create_unique(m2m_table_name, ['event_id', 'organizer_id'])

		# Adding model 'Organizer'
		db.create_table('event_organizer', (
			('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
			('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
			('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
			('twitter', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
			('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
		))
		db.send_create_signal('event', ['Organizer'])


	def backwards(self, orm):
		# Deleting model 'Website'
		db.delete_table('event_website')

		# Deleting model 'Event'
		db.delete_table('event_event')

		# Removing M2M table for field team on 'Event'
		db.delete_table(db.shorten_name('event_event_team'))

		# Deleting model 'Organizer'
		db.delete_table('event_organizer')


	models = {
		'auth.group': {
			'Meta': {'object_name': 'Group'},
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
			'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
		},
		'auth.permission': {
			'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
			'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
		},
		'auth.user': {
			'Meta': {'object_name': 'User'},
			'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
			'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
			'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
			'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
			'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
			'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
			'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
			'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
			'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
		},
		'contenttypes.contenttype': {
			'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
			'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
		},
		'event.event': {
			'Meta': {'object_name': 'Event'},
			'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'date': ('django.db.models.fields.DateField', [], {}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'main_organizer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_organizer'", 'to': "orm['event.Organizer']"}),
			'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
			'team': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team'", 'symmetrical': 'False', 'to': "orm['event.Organizer']"})
		},
		'event.organizer': {
			'Meta': {'object_name': 'Organizer'},
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
			'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
			'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
			'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
		},
		'event.website': {
			'Meta': {'object_name': 'Website'},
			'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Event']"}),
			'facebook_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'gplus_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'mailchimp_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
			'twitter_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
		}
	}

	complete_apps = ['event']