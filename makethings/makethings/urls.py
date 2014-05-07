from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<city>[\w\d]+)', 'event.views.index', name='event'),
	url(r'^$', 'core.views.index', name='index'),
)


