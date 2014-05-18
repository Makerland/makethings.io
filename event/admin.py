# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class WebsiteAdmin(admin.ModelAdmin):
	list_display = ['name', 'event', 'url', 'status']
	
	fieldsets = [
		('General settings', {
			'classes': ('suit-tab suit-tab-general',),
			'fields': ['event', 'url', 'date', 'team', 'status']
		}),
		('Social', {
			'classes': ('suit-tab suit-tab-general',),
			'fields': ['mailchimp_id', 'facebook_url']
		}),
		('About section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['about_title', 'about_description', 'about_button', 'about_url']
		}),
	    ('Location section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['location_name', 'location_button', 'location_url']
		}),
	    ('Values section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['value_1', 'value_2', 'value_3']
		}),
	    ('Apply section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['apply_title', 'apply_description', 'apply_button', 'apply_url']
		}),
	    ('Workshop section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['workshops_title']
		}),
	    ('How it works section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['howitworks_title', 'howitworks_description']
		}),
	    ('Agenda section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['agenda_title']
		}),
	    ('Sponsors section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['sponsors_title', 'sponsors_description']
		}),
        ('FAQ section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['faqs'],
		}),
	    ('Newsletter section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['newsletter_title', 'newsletter_description', 'social_title']
		}),
		('Organizers section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['organizers_title']
		})

	]
	suit_form_tabs = (('general', 'General settings'), ('content', 'Content on website'))

	def queryset(self, request):
		qs = super(WebsiteAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		organizer = Organizer.objects.get(user=request.user)
		return qs.filter(team__in=[organizer,])

class EventAdmin(admin.ModelAdmin):
	list_display = ['city', 'country', 'main_organizer']

class OrganizerAdmin(admin.ModelAdmin):
	list_display = ['user', 'name', 'twitter',]

	def queryset(self, request):
		qs = super(OrganizerAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)

class WorkshopLeaderAdmin(admin.ModelAdmin):
	list_display = ['name', 'website', 'bio']
	list_filter = ['website', ]

	def get_form(self, request, obj=None, **kwargs):
		form = super(WorkshopLeaderAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			organizer = Organizer.objects.get(user=request.user)
			form.base_fields['website'].queryset = Website.objects.filter(team__in=[organizer,])
		return form

	def queryset(self, request):
		qs = super(WorkshopLeaderAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		organizer = Organizer.objects.get(user=request.user)
		return qs.filter(website__team__in=[organizer,])

class WorkshopAdmin(admin.ModelAdmin):
	list_display = ['name', 'website', 'is_public']
	list_filter = ['website', 'is_public']

	def get_form(self, request, obj=None, **kwargs):
		form = super(WorkshopAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			organizer = Organizer.objects.get(user=request.user)
			form.base_fields['website'].queryset = Website.objects.filter(team__in=[organizer,])
			form.base_fields['leaders'].queryset = WorkshopLeader.objects.filter(website__team__in=[organizer,])
		return form

	def queryset(self, request):
		qs = super(WorkshopAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		organizer = Organizer.objects.get(user=request.user)
		return qs.filter(website__team__in=[organizer,])

class AgendaAdmin(admin.ModelAdmin):
	list_display = ['title', 'website', 'start_time', 'end_time', 'is_highlighted', 'is_break']
	list_filter = ['website', ]

	def get_form(self, request, obj=None, **kwargs):
		form = super(AgendaAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			organizer = Organizer.objects.get(user=request.user)
			form.base_fields['website'].queryset = Website.objects.filter(team__in=[organizer,])
			form.base_fields['workshop'].queryset = Workshop.objects.filter(website__team__in=[organizer,])
		return form

	def queryset(self, request):
		qs = super(AgendaAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		organizer = Organizer.objects.get(user=request.user)
		return qs.filter(website__team__in=[organizer,])

class SponsorAdmin(admin.ModelAdmin):
	list_display = ['name', 'website', 'description', 'url', 'order']
	list_filter = ['website', ]

	def get_form(self, request, obj=None, **kwargs):
		form = super(SponsorAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			organizer = Organizer.objects.get(user=request.user)
			form.base_fields['website'].queryset = Website.objects.filter(team__in=[organizer,])
		return form

	def queryset(self, request):
		qs = super(SponsorAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		organizer = Organizer.objects.get(user=request.user)
		return qs.filter(website__team__in=[organizer,])

class FAQAdmin(admin.ModelAdmin):
	list_display = ['question', 'answer']
	list_filter = ['websites',]

	def get_form(self, request, obj=None, **kwargs):
		form = super(FAQAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			organizer = Organizer.objects.get(user=request.user)
			form.base_fields['websites'].queryset = Website.objects.filter(team__in=[organizer,])
		return form

	def queryset(self, request):
		qs = super(FAQAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		organizer = Organizer.objects.get(user=request.user)
		return qs.filter(website__team__in=[organizer,])

admin.site.register(Website, WebsiteAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(WorkshopLeader, WorkshopLeaderAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(FAQ, FAQAdmin)