# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import *
from forms import UserChangeForm, UserCreationForm, UserLimitedChangeForm


class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'twitter', 'photo', 'event')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'twitter', 'photo')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = UserChangeForm
    limited_form = UserLimitedChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_superuser')
    list_filter = ('event', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)

    def get_queryset(self, request):
		qs = super(UserAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(pk=request.user.pk)

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj and not request.user.is_superuser:
            defaults.update({
                'form': self.limited_form,
                'fields': admin.util.flatten_fieldsets(self.limited_fieldsets),
            })
        defaults.update(kwargs)
        return super(UserAdmin, self).get_form(request, obj, **defaults)

    def get_fieldsets(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return self.limited_fieldsets
        return super(UserAdmin, self).get_fieldsets(request, obj)


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
	    ('Newsletter section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['newsletter_title', 'newsletter_description', 'social_title']
		}),
		('Organizers section', {
			'classes': ('suit-tab suit-tab-content',),
		    'fields': ['organizers_title']
		}),
        ('Background photos', {
			'classes': ('suit-tab suit-tab-photos',),
			'fields': ['location_photo', 'apply_photo', 'howitworks_photo', 'makerland_photo', 'social_photo']
		}),
	]
	suit_form_tabs = (('general', 'General settings'), ('content', 'Content on website'), ('photos', 'Background photos'), )

	def get_form(self, request, obj=None, **kwargs):
		form = super(WebsiteAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			form.base_fields['team'].queryset = User.objects.filter(event=request.user.event)
		return form

	def queryset(self, request):
		qs = super(WebsiteAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(team__in=[request.user,])

class EventAdmin(admin.ModelAdmin):
	list_display = ['city', 'country', 'main_organizer']

class WorkshopLeaderAdmin(admin.ModelAdmin):
	list_display = ['name', 'event', 'bio']
	limited_fieldsets = (None, {'fields': ('name', 'bio', 'photo')}),

	def get_fieldsets(self, request, obj=None):
		if not request.user.is_superuser:
			return self.limited_fieldsets
		return super(WorkshopLeaderAdmin, self).get_fieldsets(request, obj)

	def save_model(self, request, obj, form, change):
		if not request.user.is_superuser:
			obj.event = request.user.event
		obj.save()

	def queryset(self, request):
		qs = super(WorkshopLeaderAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(event=request.user.event)

class WorkshopAdmin(admin.ModelAdmin):
	list_display = ['name', 'website', 'is_public']
	list_filter = ['website', 'is_public']

	def get_form(self, request, obj=None, **kwargs):
		form = super(WorkshopAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			form.base_fields['website'].queryset = Website.objects.filter(team__in=[request.user])
			form.base_fields['leaders'].queryset = WorkshopLeader.objects.filter(event=request.user.event)
		return form

	def queryset(self, request):
		qs = super(WorkshopAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(website__team__in=[request.user,])

class AgendaEntryAdmin(admin.ModelAdmin):
	list_display = ['title', 'website', 'start_time', 'end_time', 'is_highlighted', 'is_break']
	list_filter = ['website', ]

	def get_form(self, request, obj=None, **kwargs):
		form = super(AgendaEntryAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			form.base_fields['website'].queryset = Website.objects.filter(team__in=[request.user])
			form.base_fields['workshop'].queryset = Workshop.objects.filter(website__team__in=[request.user])
		return form

	def queryset(self, request):
		qs = super(AgendaEntryAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(website__team__in=[request.user,])

class SponsorAdmin(admin.ModelAdmin):
	list_display = ['name', 'website', 'description', 'url', 'order']
	list_filter = ['website', ]

	def get_form(self, request, obj=None, **kwargs):
		form = super(SponsorAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			form.base_fields['website'].queryset = Website.objects.filter(team__in=[request.user])
		return form

	def queryset(self, request):
		qs = super(SponsorAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(website__team__in=[request.user,])

class FAQAdmin(admin.ModelAdmin):
	list_display = ['question', 'answer']
	list_filter = ['websites',]

	def get_form(self, request, obj=None, **kwargs):
		form = super(FAQAdmin, self).get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			form.base_fields['websites'].queryset = Website.objects.filter(team__in=[request.user,])
		return form


admin.site.register(User, UserAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(WorkshopLeader, WorkshopLeaderAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(AgendaEntry, AgendaEntryAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(FAQ, FAQAdmin)