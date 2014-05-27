# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'event_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='organizers', null=True, to=orm['event.Event'])),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'event', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'event_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'event.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'event_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'event.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding model 'Event'
        db.create_table(u'event_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('main_organizer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['event.User'])),
        ))
        db.send_create_signal(u'event', ['Event'])

        # Adding model 'Website'
        db.create_table(u'event_website', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Event'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('about_title', self.gf('django.db.models.fields.CharField')(default='Make Things in ...', max_length=255)),
            ('about_description', self.gf('django.db.models.fields.TextField')(default='Welcome to the free, one-day event that will get you excited and teach you everything you want to know about the world of hardware, Internet of Things and Maker Movement.')),
            ('about_button', self.gf('django.db.models.fields.CharField')(default='Apply for a pass', max_length=255, null=True, blank=True)),
            ('about_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('location_name', self.gf('django.db.models.fields.CharField')(default='Location: TBA', max_length=255, null=True, blank=True)),
            ('location_button', self.gf('django.db.models.fields.CharField')(default='Get directions \xc2\xbb', max_length=255, null=True, blank=True)),
            ('location_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('location_photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('value_1', self.gf('django.db.models.fields.CharField')(default='<b>Make Things</b> aims to give everyone a chance to start their journey with hardware.', max_length=255, null=True, blank=True)),
            ('value_2', self.gf('django.db.models.fields.CharField')(default='Come & learn about <b>3D printing, Arduino, Raspberry Pi, drones, robots and DIY</b> in a friendly enviroment.', max_length=255, null=True, blank=True)),
            ('value_3', self.gf('django.db.models.fields.CharField')(default='Become a Maker! Be a part of <b>global community of Makers</b>. Start making the future.', max_length=255, null=True, blank=True)),
            ('apply_title', self.gf('django.db.models.fields.CharField')(default='Apply for a ticket!', max_length=255, null=True, blank=True)),
            ('apply_description', self.gf('django.db.models.fields.TextField')(default="Workshops are aimed for people of any age with basic knowledge of working with a computer. Most of the program is run in Polish, but basic reading skills in English are helpful - some materials are available only in English. We will choose a diverse group of people who are truly motivated and curious about learning. Event is free for everyone, we have a limited space for only 70 participants.<br /><br />You'll receive your acceptance letter by 19th June 2014.", null=True, blank=True)),
            ('apply_button', self.gf('django.db.models.fields.CharField')(default='Apply', max_length=255, null=True, blank=True)),
            ('apply_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('apply_photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('workshops_title', self.gf('django.db.models.fields.CharField')(default='Workshops', max_length=255, null=True, blank=True)),
            ('howitworks_title', self.gf('django.db.models.fields.CharField')(default='How it works?', max_length=255, null=True, blank=True)),
            ('howitworks_description', self.gf('django.db.models.fields.TextField')(default="Make Things is all about learning, having fun and meeting new people. We care about people: you're in the center of the event and we will make sure you fell in love with the world of hardware. During the whole day we will have a couple of workshop stations that will be working all the time. It means that you can join a workshop anytime you want and stay for as long as you want. If you want to get a little bit of everything, you can do that. If you want to get a deep dive into one topic, you can do that. No fixed schedule, no boredom: just fun, robots and MAKING THINGS.", null=True, blank=True)),
            ('howitworks_photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('agenda_title', self.gf('django.db.models.fields.CharField')(default='Agenda', max_length=255)),
            ('sponsors_title', self.gf('django.db.models.fields.CharField')(default='Sponsors', max_length=255)),
            ('sponsors_description', self.gf('django.db.models.fields.CharField')(default="We're looking for sponsors! Want to help make MAKE THINGS in ... a success? Contact us: ...@makethings.io", max_length=255, null=True, blank=True)),
            ('newsletter_title', self.gf('django.db.models.fields.CharField')(default='Stay in touch:', max_length=255)),
            ('newsletter_description', self.gf('django.db.models.fields.TextField')(default='If you want to ocasionally receive latest news about Make Things, Makerland or Internet of Things world, subscribe to our newsletter:', null=True, blank=True)),
            ('social_title', self.gf('django.db.models.fields.CharField')(default='Follow us on social media:', max_length=255)),
            ('social_photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('organizers_title', self.gf('django.db.models.fields.CharField')(default='Make Things in ... is organized by', max_length=255, null=True, blank=True)),
            ('makerland_photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('mailchimp_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('facebook_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'event', ['Website'])

        # Adding M2M table for field team on 'Website'
        m2m_table_name = db.shorten_name(u'event_website_team')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('website', models.ForeignKey(orm[u'event.website'], null=False)),
            ('user', models.ForeignKey(orm[u'event.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['website_id', 'user_id'])

        # Adding model 'WorkshopLeader'
        db.create_table(u'event_workshopleader', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='workshop_leaders', to=orm['event.Event'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'event', ['WorkshopLeader'])

        # Adding model 'Workshop'
        db.create_table(u'event_workshop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Website'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'event', ['Workshop'])

        # Adding M2M table for field leaders on 'Workshop'
        m2m_table_name = db.shorten_name(u'event_workshop_leaders')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workshop', models.ForeignKey(orm[u'event.workshop'], null=False)),
            ('workshopleader', models.ForeignKey(orm[u'event.workshopleader'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workshop_id', 'workshopleader_id'])

        # Adding model 'FAQ'
        db.create_table(u'event_faq', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'event', ['FAQ'])

        # Adding M2M table for field websites on 'FAQ'
        m2m_table_name = db.shorten_name(u'event_faq_websites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faq', models.ForeignKey(orm[u'event.faq'], null=False)),
            ('website', models.ForeignKey(orm[u'event.website'], null=False))
        ))
        db.create_unique(m2m_table_name, ['faq_id', 'website_id'])

        # Adding model 'AgendaEntry'
        db.create_table(u'event_agendaentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agenda_entries', to=orm['event.Website'])),
            ('workshop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Workshop'], null=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_highlighted', self.gf('django.db.models.fields.BooleanField')()),
            ('is_break', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'event', ['AgendaEntry'])

        # Adding model 'Sponsor'
        db.create_table(u'event_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Website'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal(u'event', ['Sponsor'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'event_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'event_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'event_user_user_permissions'))

        # Deleting model 'Event'
        db.delete_table(u'event_event')

        # Deleting model 'Website'
        db.delete_table(u'event_website')

        # Removing M2M table for field team on 'Website'
        db.delete_table(db.shorten_name(u'event_website_team'))

        # Deleting model 'WorkshopLeader'
        db.delete_table(u'event_workshopleader')

        # Deleting model 'Workshop'
        db.delete_table(u'event_workshop')

        # Removing M2M table for field leaders on 'Workshop'
        db.delete_table(db.shorten_name(u'event_workshop_leaders'))

        # Deleting model 'FAQ'
        db.delete_table(u'event_faq')

        # Removing M2M table for field websites on 'FAQ'
        db.delete_table(db.shorten_name(u'event_faq_websites'))

        # Deleting model 'AgendaEntry'
        db.delete_table(u'event_agendaentry')

        # Deleting model 'Sponsor'
        db.delete_table(u'event_sponsor')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'event.agendaentry': {
            'Meta': {'ordering': "('website', 'start_time')", 'object_name': 'AgendaEntry'},
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_break': ('django.db.models.fields.BooleanField', [], {}),
            'is_highlighted': ('django.db.models.fields.BooleanField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agenda_entries'", 'to': u"orm['event.Website']"}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Workshop']", 'null': 'True', 'blank': 'True'})
        },
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_organizer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['event.User']"})
        },
        u'event.faq': {
            'Meta': {'object_name': 'FAQ'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'websites': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'faqs'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['event.Website']"})
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
        u'event.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'organizers'", 'null': 'True', 'to': u"orm['event.Event']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
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
            'apply_photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'apply_title': ('django.db.models.fields.CharField', [], {'default': "'Apply for a ticket!'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'apply_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            'facebook_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'howitworks_description': ('django.db.models.fields.TextField', [], {'default': '"Make Things is all about learning, having fun and meeting new people. We care about people: you\'re in the center of the event and we will make sure you fell in love with the world of hardware. During the whole day we will have a couple of workshop stations that will be working all the time. It means that you can join a workshop anytime you want and stay for as long as you want. If you want to get a little bit of everything, you can do that. If you want to get a deep dive into one topic, you can do that. No fixed schedule, no boredom: just fun, robots and MAKING THINGS."', 'null': 'True', 'blank': 'True'}),
            'howitworks_photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'howitworks_title': ('django.db.models.fields.CharField', [], {'default': "'How it works?'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_button': ('django.db.models.fields.CharField', [], {'default': "'Get directions \\xc2\\xbb'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'default': "'Location: TBA'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location_photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mailchimp_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'makerland_photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'newsletter_description': ('django.db.models.fields.TextField', [], {'default': "'If you want to ocasionally receive latest news about Make Things, Makerland or Internet of Things world, subscribe to our newsletter:'", 'null': 'True', 'blank': 'True'}),
            'newsletter_title': ('django.db.models.fields.CharField', [], {'default': "'Stay in touch:'", 'max_length': '255'}),
            'organizers_title': ('django.db.models.fields.CharField', [], {'default': "'Make Things in ... is organized by'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'social_photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'social_title': ('django.db.models.fields.CharField', [], {'default': "'Follow us on social media:'", 'max_length': '255'}),
            'sponsors_description': ('django.db.models.fields.CharField', [], {'default': '"We\'re looking for sponsors! Want to help make MAKE THINGS in ... a success? Contact us: ...@makethings.io"', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sponsors_title': ('django.db.models.fields.CharField', [], {'default': "'Sponsors'", 'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'websites'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['event.User']"}),
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
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'workshop_leaders'", 'to': u"orm['event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['event']