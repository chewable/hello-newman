from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

#feeds = {
#    'latest': LatestEntries,
#    'categories': LatestEntriesByCategory,
#}
    
urlpatterns = patterns('',
    url(r'^$', direct_to_template, { 'template': 'landing.html'}),
    (r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    (r'^admin/', include(admin.site.urls)),
#    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # Static Media Serving
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        })
    )
