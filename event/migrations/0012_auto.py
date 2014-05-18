# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field websites on 'FAQ'
        m2m_table_name = db.shorten_name(u'event_faq_websites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faq', models.ForeignKey(orm[u'event.faq'], null=False)),
            ('website', models.ForeignKey(orm[u'event.website'], null=False))
        ))
        db.create_unique(m2m_table_name, ['faq_id', 'website_id'])


    def backwards(self, orm):
        # Removing M2M table for field websites on 'FAQ'
        db.delete_table(db.shorten_name(u'event_faq_websites'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'event.agenda': {
            'Meta': {'ordering': "('website', 'start_time')", 'object_name': 'Agenda'},
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_break': ('django.db.models.fields.BooleanField', [], {}),
            'is_highlighted': ('django.db.models.fields.BooleanField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Website']"}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Workshop']", 'null': 'True', 'blank': 'True'})
        },
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_organizer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_organizer'", 'to': u"orm['event.Organizer']"})
        },
        u'event.faq': {
            'Meta': {'object_name': 'FAQ'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Website']"}),
            'websites': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'faqs'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['event.Website']"})
        },
        u'event.organizer': {
            'Meta': {'object_name': 'Organizer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'event.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Website']"})
        },
        u'event.website': {
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
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            'facebook_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'howitworks_description': ('django.db.models.fields.TextField', [], {'default': '"Make Things is all about learning, having fun and meeting new people. We care about people: you\'re in the center of the event and we will make sure you fell in love with the world of hardware. During the whole day we will have a couple of workshop stations that will be working all the time. It means that you can join a workshop anytime you want and stay for as long as you want. If you want to get a little bit of everything, you can do that. If you want to get a deep dive into one topic, you can do that. No fixed schedule, no boredom: just fun, robots and MAKING THINGS."', 'null': 'True', 'blank': 'True'}),
            'howitworks_title': ('django.db.models.fields.CharField', [], {'default': "'How it works?'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'websites'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['event.Organizer']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value_1': ('django.db.models.fields.CharField', [], {'default': "'<b>Make Things</b> aims to give everyone a chance to start their journey with hardware.'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'value_2': ('django.db.models.fields.CharField', [], {'default': "'Come & learn about <b>3D printing, Arduino, Raspberry Pi, drones, robots and DIY</b> in a friendly enviroment.'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'value_3': ('django.db.models.fields.CharField', [], {'default': "'Become a Maker! Be a part of <b>global community of Makers</b>. Start making the future.'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'workshops_title': ('django.db.models.fields.CharField', [], {'default': "'Workshops'", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'event.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'leaders': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['event.WorkshopLeader']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Website']"})
        },
        u'event.workshopleader': {
            'Meta': {'object_name': 'WorkshopLeader'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Website']", 'null': 'True'})
        }
    }

    complete_apps = ['event']