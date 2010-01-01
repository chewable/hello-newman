from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^filter/(?P<slug>[-\w]+)/$',
        view = 'hellonewman.blog.views.filter_blog',
        name = 'filter-blog'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',
        view = 'hellonewman.blog.views.entry_detail',
        name = 'entry-detail'
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
)
