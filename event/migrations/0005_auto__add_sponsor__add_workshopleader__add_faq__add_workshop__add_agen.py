# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

	def forwards(self, orm):
		# Adding model 'Sponsor'
		db.create_table('event_sponsor', (
			('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
			('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Website'])),
			('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
			('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
			('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
			('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
			('order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
		))
		db.send_create_signal('event', ['Sponsor'])

		# Adding model 'WorkshopLeader'
		db.create_table('event_workshopleader', (
			('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
			('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
			('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
			('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
		))
		db.send_create_signal('event', ['WorkshopLeader'])

		# Adding model 'FAQ'
		db.create_table('event_faq', (
			('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
			('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Website'])),
			('question', self.gf('django.db.models.fields.TextField')()),
			('answer', self.gf('django.db.models.fields.TextField')()),
		))
		db.send_create_signal('event', ['FAQ'])

		# Adding model 'Workshop'
		db.create_table('event_workshop', (
			('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
			('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Website'])),
			('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
			('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
			('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
			('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
		))
		db.send_create_signal('event', ['Workshop'])

		# Adding M2M table for field leaders on 'Workshop'
		m2m_table_name = db.shorten_name('event_workshop_leaders')
		db.create_table(m2m_table_name, (
			('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
			('workshop', models.ForeignKey(orm['event.workshop'], null=False)),
			('workshopleader', models.ForeignKey(orm['event.workshopleader'], null=False))
		))
		db.create_unique(m2m_table_name, ['workshop_id', 'workshopleader_id'])

		# Adding model 'Agenda'
		db.create_table('event_agenda', (
			('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
			('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Website'])),
			('workshop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Workshop'], null=True, blank=True)),
			('start_time', self.gf('django.db.models.fields.TimeField')()),
			('end_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
			('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
			('is_highlighted', self.gf('django.db.models.fields.BooleanField')(default=False)),
			('is_break', self.gf('django.db.models.fields.BooleanField')(default=False)),
		))
		db.send_create_signal('event', ['Agenda'])


	def backwards(self, orm):
		# Deleting model 'Sponsor'
		db.delete_table('event_sponsor')

		# Deleting model 'WorkshopLeader'
		db.delete_table('event_workshopleader')

		# Deleting model 'FAQ'
		db.delete_table('event_faq')

		# Deleting model 'Workshop'
		db.delete_table('event_workshop')

		# Removing M2M table for field leaders on 'Workshop'
		db.delete_table(db.shorten_name('event_workshop_leaders'))

		# Deleting model 'Agenda'
		db.delete_table('event_agenda')


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
		'event.agenda': {
			'Meta': {'object_name': 'Agenda'},
			'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'is_break': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'is_highlighted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'start_time': ('django.db.models.fields.TimeField', [], {}),
			'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
			'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Website']"}),
			'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Workshop']", 'null': 'True', 'blank': 'True'})
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
		'event.faq': {
			'Meta': {'object_name': 'FAQ'},
			'answer': ('django.db.models.fields.TextField', [], {}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'question': ('django.db.models.fields.TextField', [], {}),
			'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Website']"})
		},
		'event.organizer': {
			'Meta': {'object_name': 'Organizer'},
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
			'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
			'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
			'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
		},
		'event.sponsor': {
			'Meta': {'object_name': 'Sponsor'},
			'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
			'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
			'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
			'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Website']"})
		},
		'event.website': {
			'Meta': {'object_name': 'Website'},
			'about_button': ('django.db.models.fields.CharField', [], {'default': "'Apply for a pass'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'about_description': ('django.db.models.fields.TextField', [], {'default': "'Welcome to the free, one-day event that will get you excited and teach you everything you want to know about the world of hardware, Internet of Things and Maker Movement.'"}),
			'about_title': ('django.db.models.fields.CharField', [], {'default': "'Make Things in ...'", 'max_length': '255'}),
			'about_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'agenda_title': ('django.db.models.fields.CharField', [], {'default': "'Agenda'", 'max_length': '255'}),
			'apply_button': ('django.db.models.fields.CharField', [], {'default': "'Apply'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'apply_description': ('django.db.models.fields.TextField', [], {'default': '"Workshops are aimed for people of any age with basic knowledge of working with a computer. Most of the program is run in Polish, but basic reading skills in English are helpful - some materials are available only in English. We will choose a diverse group of people who are truly motivated and curious about learning. Event is free for everyone, we have a limited space for only 70 participants.<br /><br />You\'ll receive your acceptance letter by 19th June 2014."', 'null': 'True', 'blank': 'True'}),
			'apply_title': ('django.db.models.fields.CharField', [], {'default': "'Apply for a ticket!'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'apply_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Event']"}),
			'facebook_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'gplus_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'howitworks_description': ('django.db.models.fields.TextField', [], {'default': '"Make Things is all about learning, having fun and meeting new people. We care about people: you\'re in the center of the event and we will make sure you fell in love with the world of hardware. During the whole day we will have a couple of workshop stations that will be working all the time. It means that you can join a workshop anytime you want and stay for as long as you want. If you want to get a little bit of everything, you can do that. If you want to get a deep dive into one topic, you can do that. No fixed schedule, no boredom: just fun, robots and MAKING THINGS."', 'null': 'True', 'blank': 'True'}),
			'howitworks_title': ('django.db.models.fields.CharField', [], {'default': "'How it works?'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
			'location_button': ('django.db.models.fields.CharField', [], {'default': "'Get directions \\xc2\\xbb'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'location_name': ('django.db.models.fields.CharField', [], {'default': "'Location: TBA'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'location_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'mailchimp_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
			'newsletter_description': ('django.db.models.fields.TextField', [], {'default': "'If you want to ocasionally receive latest news about Make Things, Makerland or Internet of Things world, subscribe to our newsletter:'", 'null': 'True', 'blank': 'True'}),
			'newsletter_title': ('django.db.models.fields.CharField', [], {'default': "'Stay in touch:'", 'max_length': '255'}),
			'organizers_title': ('django.db.models.fields.CharField', [], {'default': "'Make Things in ... is organized by'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'social_title': ('django.db.models.fields.CharField', [], {'default': "'Follow us on social media:'", 'max_length': '255'}),
			'sponsors_description': ('django.db.models.fields.CharField', [], {'default': '"We couldn\'t be here without the amazing support of our sponsors:"', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'sponsors_title': ('django.db.models.fields.CharField', [], {'default': "'Sponsors'", 'max_length': '255'}),
			'twitter_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
			'url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
			'value_1': ('django.db.models.fields.CharField', [], {'default': "'<b>Make Things</b> aims to give everyone a chance to start their journey with hardware.'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'value_2': ('django.db.models.fields.CharField', [], {'default': "'Come & learn about <b>3D printing, Arduino, Raspberry Pi, drones, robots and DIY</b> in a friendly enviroment.'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'value_3': ('django.db.models.fields.CharField', [], {'default': "'Become a Maker! Be a part of <b>global community of Makers</b>. Start making the future.'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'workshops_title': ('django.db.models.fields.CharField', [], {'default': "'Workshops'", 'max_length': '255', 'null': 'True', 'blank': 'True'})
		},
		'event.workshop': {
			'Meta': {'object_name': 'Workshop'},
			'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
			'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
			'leaders': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['event.WorkshopLeader']", 'null': 'True', 'blank': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
			'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Website']"})
		},
		'event.workshopleader': {
			'Meta': {'object_name': 'WorkshopLeader'},
			'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
			'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
			'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
		}
	}

	complete_apps = ['event']