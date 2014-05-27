from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG == False:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT,
		}),
	)

urlpatterns += patterns('',
    url(r'^inyourcity', 'core.views.inyourcity', name='inyourcity'),
	url(r'^(?P<city>[\w\d]+)', 'event.views.index', name='event'),
	url(r'^$', 'core.views.index', name='index'),

)



