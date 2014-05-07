# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

	def forwards(self, orm):
		# Adding field 'Website.about_title'
		db.add_column('event_website', 'about_title',
					  self.gf('django.db.models.fields.CharField')(default='Make Things in ...', max_length=255),
					  keep_default=False)

		# Adding field 'Website.about_desc'
		db.add_column('event_website', 'about_desc',
					  self.gf('django.db.models.fields.TextField')(default='Welcome to the free, one-day event that will get you excited and teach you everything you want to know about the world of hardware, Internet of Things and Maker Movement.'),
					  keep_default=False)

		# Adding field 'Website.about_button'
		db.add_column('event_website', 'about_button',
					  self.gf('django.db.models.fields.CharField')(default='Apply for a pass', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.about_url'
		db.add_column('event_website', 'about_url',
					  self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.location_name'
		db.add_column('event_website', 'location_name',
					  self.gf('django.db.models.fields.CharField')(default='Location: TBA', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.location_button'
		db.add_column('event_website', 'location_button',
					  self.gf('django.db.models.fields.CharField')(default='Get directions \xc2\xbb', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.location_url'
		db.add_column('event_website', 'location_url',
					  self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.value_1'
		db.add_column('event_website', 'value_1',
					  self.gf('django.db.models.fields.CharField')(default='<b>Make Things</b> aims to give everyone a chance to start their journey with hardware.', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.value_2'
		db.add_column('event_website', 'value_2',
					  self.gf('django.db.models.fields.CharField')(default='Come & learn about <b>3D printing, Arduino, Raspberry Pi, drones, robots and DIY</b> in a friendly enviroment.', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.value_3'
		db.add_column('event_website', 'value_3',
					  self.gf('django.db.models.fields.CharField')(default='Become a Maker! Be a part of <b>global community of Makers</b>. Start making the future.', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.apply_title'
		db.add_column('event_website', 'apply_title',
					  self.gf('django.db.models.fields.CharField')(default='Apply for a ticket!', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.apply_description'
		db.add_column('event_website', 'apply_description',
					  self.gf('django.db.models.fields.TextField')(default="Workshops are aimed for people of any age with basic knowledge of working with a computer. Most of the program is run in Polish, but basic reading skills in English are helpful - some materials are available only in English. We will choose a diverse group of people who are truly motivated and curious about learning. Event is free for everyone, we have a limited space for only 70 participants.<br /><br />You'll receive your acceptance letter by 19th June 2014.", null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.apply_button'
		db.add_column('event_website', 'apply_button',
					  self.gf('django.db.models.fields.CharField')(default='Apply', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.apply_url'
		db.add_column('event_website', 'apply_url',
					  self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.workshops_title'
		db.add_column('event_website', 'workshops_title',
					  self.gf('django.db.models.fields.CharField')(default='Workshops', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.howitworks_title'
		db.add_column('event_website', 'howitworks_title',
					  self.gf('django.db.models.fields.CharField')(default='How it works?', max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.howitworks_description'
		db.add_column('event_website', 'howitworks_description',
					  self.gf('django.db.models.fields.TextField')(default="Make Things is all about learning, having fun and meeting new people. We care about people: you're in the center of the event and we will make sure you fell in love with the world of hardware. During the whole day we will have a couple of workshop stations that will be working all the time. It means that you can join a workshop anytime you want and stay for as long as you want. If you want to get a little bit of everything, you can do that. If you want to get a deep dive into one topic, you can do that. No fixed schedule, no boredom: just fun, robots and MAKING THINGS.", null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.agenda_title'
		db.add_column('event_website', 'agenda_title',
					  self.gf('django.db.models.fields.CharField')(default='Agenda', max_length=255),
					  keep_default=False)

		# Adding field 'Website.sponsors_title'
		db.add_column('event_website', 'sponsors_title',
					  self.gf('django.db.models.fields.CharField')(default='Sponsors', max_length=255),
					  keep_default=False)

		# Adding field 'Website.sponsors_description'
		db.add_column('event_website', 'sponsors_description',
					  self.gf('django.db.models.fields.CharField')(default="We couldn't be here without the amazing support of our sponsors:", max_length=255, null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.newsletter_title'
		db.add_column('event_website', 'newsletter_title',
					  self.gf('django.db.models.fields.CharField')(default='Stay in touch:', max_length=255),
					  keep_default=False)

		# Adding field 'Website.newsletter_description'
		db.add_column('event_website', 'newsletter_description',
					  self.gf('django.db.models.fields.TextField')(default='If you want to ocasionally receive latest news about Make Things, Makerland or Internet of Things world, subscribe to our newsletter:', null=True, blank=True),
					  keep_default=False)

		# Adding field 'Website.social_title'
		db.add_column('event_website', 'social_title',
					  self.gf('django.db.models.fields.CharField')(default='Follow us on social media:', max_length=255),
					  keep_default=False)

		# Adding field 'Website.organizers_title'
		db.add_column('event_website', 'organizers_title',
					  self.gf('django.db.models.fields.CharField')(default='Make Things in ... is organized by', max_length=255, null=True, blank=True),
					  keep_default=False)


	def backwards(self, orm):
		# Deleting field 'Website.about_title'
		db.delete_column('event_website', 'about_title')

		# Deleting field 'Website.about_desc'
		db.delete_column('event_website', 'about_desc')

		# Deleting field 'Website.about_button'
		db.delete_column('event_website', 'about_button')

		# Deleting field 'Website.about_url'
		db.delete_column('event_website', 'about_url')

		# Deleting field 'Website.location_name'
		db.delete_column('event_website', 'location_name')

		# Deleting field 'Website.location_button'
		db.delete_column('event_website', 'location_button')

		# Deleting field 'Website.location_url'
		db.delete_column('event_website', 'location_url')

		# Deleting field 'Website.value_1'
		db.delete_column('event_website', 'value_1')

		# Deleting field 'Website.value_2'
		db.delete_column('event_website', 'value_2')

		# Deleting field 'Website.value_3'
		db.delete_column('event_website', 'value_3')

		# Deleting field 'Website.apply_title'
		db.delete_column('event_website', 'apply_title')

		# Deleting field 'Website.apply_description'
		db.delete_column('event_website', 'apply_description')

		# Deleting field 'Website.apply_button'
		db.delete_column('event_website', 'apply_button')

		# Deleting field 'Website.apply_url'
		db.delete_column('event_website', 'apply_url')

		# Deleting field 'Website.workshops_title'
		db.delete_column('event_website', 'workshops_title')

		# Deleting field 'Website.howitworks_title'
		db.delete_column('event_website', 'howitworks_title')

		# Deleting field 'Website.howitworks_description'
		db.delete_column('event_website', 'howitworks_description')

		# Deleting field 'Website.agenda_title'
		db.delete_column('event_website', 'agenda_title')

		# Deleting field 'Website.sponsors_title'
		db.delete_column('event_website', 'sponsors_title')

		# Deleting field 'Website.sponsors_description'
		db.delete_column('event_website', 'sponsors_description')

		# Deleting field 'Website.newsletter_title'
		db.delete_column('event_website', 'newsletter_title')

		# Deleting field 'Website.newsletter_description'
		db.delete_column('event_website', 'newsletter_description')

		# Deleting field 'Website.social_title'
		db.delete_column('event_website', 'social_title')

		# Deleting field 'Website.organizers_title'
		db.delete_column('event_website', 'organizers_title')


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
			'about_button': ('django.db.models.fields.CharField', [], {'default': "'Apply for a pass'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
			'about_desc': ('django.db.models.fields.TextField', [], {'default': "'Welcome to the free, one-day event that will get you excited and teach you everything you want to know about the world of hardware, Internet of Things and Maker Movement.'"}),
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
		}
	}

	complete_apps = ['event']