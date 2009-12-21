from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
#from jen.core.feeds import LatestEntries
admin.autodiscover()

admin.site.root_path = '/maya/'

#feeds = {
#    'latest': LatestEntries,
#    'categories': LatestEntriesByCategory,
#}
    
urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',
        view = 'hellonewman.blog.views.entry_detail',
        name = 'entry-detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',
        view = 'hellonewman.blog.views.archive_day',
        name = 'archive-day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
        view = 'hellonewman.blog.views.archive_month',
        name = 'archive-month'
    ),
    url(r'^(?P<year>\d{4})/$',
        view = 'hellonewman.blog.views.archive_year',
        name = 'archive-year'
    ),
    url(r'^$',
        view = 'hellonewman.blog.views.home_page',
        name = "home-page"),

    (r'^contact/', include('contact_form.urls')),
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
