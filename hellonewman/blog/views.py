from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic import date_based
from django.utils import simplejson as json

from django.contrib.sites.models import Site
from tagging.models import Tag, TaggedItem

from hellonewman.blog.models import Entry, Distraction, Blog, FeedHit, Category
from hellonewman.blog.exceptions import InvalidBlog

@login_required
def preview(request, slug):
    """
    preview view for writing articles
    expects the user to be logged in to view the article
    """
    entry = get_object_or_404(Entry, slug=slug)

    return render_to_response("blog/entry_detail.html", {
        "entry": entry,
    }, context_instance=RequestContext(request))

def filter_blog(request, slug=None):
    """
    segregates the blog by blog type
    expects a slug in the url to set the session.
    this may change to cookie based session in the future
    but for now we will set it in the session

    if no slug is passed then the user wants to see all
    journal types.
    """

    if slug is None:
        try:
            del request.session['blog_filter']
        except KeyError:
            pass
    else:
        request.session['blog_filter'] = slug

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    

def home_page(request):
    """
    Displays the landing page
    If the blog filter is set in the session then only show
    those kind of entries
    """
    
    if 'blog_filter' in request.session:
        entries = Entry.objects.filter(blog__slug=request.session['blog_filter'], published=True)
    else:
        entries = Entry.objects.published()[:9]
                                 
    distractions = Distraction.objects.published()[:5]
    
    return render_to_response('blog/home_page.html', {
        "entries": entries,
        "distractions": distractions,
    }, context_instance=RequestContext(request))

def entry_detail(request, year, month, day, slug, **kwargs):
    """
    displays the details of an ``Entry``.
        
    """
    entry = get_object_or_404(Entry, slug=slug)
    entry.increase_read_count()

    return render_to_response("blog/entry_detail.html", {
        "entry": entry,
    }, context_instance=RequestContext(request))


def tagged_entries(request, tag):
    """
    returns all posts tagged with `tag`
    """
    tag = get_object_or_404(Tag, name=tag)
    entries = TaggedItem.objects.get_by_model(Entry, tag)

    if 'blog_filter' in request.session:
        entries = entries.filter(blog__slug=request.session['blog_filter'])

    return render_to_response("blog/tag_list.html", {
        "entries": entries,
        "tag": tag,
    }, context_instance=RequestContext(request))

def category_entries(request, slug):
    """
    returns all posts for a given category
    """
    entries = Entry.objects.filter(category__slug=slug, published=True)

    return render_to_response("blog/category_entries.html", {
        "entries": entries,
    }, context_instance=RequestContext(request))

def archive_index(request):
    """
    entry archives
    """
    return date_based.archive_index(
        request,
        queryset=Entry.objects.all(),
        date_field='created_on',
        template_object_name='entry'
    )

def archive_month(request):
    """
    A wrapper around ``django.views.generic.date_based.archive_month`` that
    displays an archive of entries for the given month.
    
    """
    return date_based.archive_month(
        request,
        queryset=Entry.objects.all(),
        date_field='created_on',
        template_object_name='entry'
    )

def archive_year(request):
    """
    A wrapper around ``django.views.generic.date_based.archive_year`` that
    displays an archive of entries for the given year.
    
    """
    return date_based.archive_year(
        request,
        queryset=Entry.objects.all(),
        date_field='created_on',
        make_object_list=True,
        template_object_name='entry'
    )

def serialize_request(request):
    """
    serializes the data for the atom feeds
    """
    data = {
        "path": request.path,
        "META": {
            "QUERY_STRING": request.META.get("QUERY_STRING"),
            "REMOTE_ADDR": request.META.get("REMOTE_ADDR"),
        }
    }
    for key in request.META:
        if key.startswith("HTTP"):
            data["META"][key] = request.META[key]
    return json.dumps(data)

def blog_feed(request, slug=None):
    """
    Atom Feeds.  Borrowed and modified from
    http://github.com/eldarion/biblion
    """

    if slug is None:
        blog_title = "combined"
        entries = Entry.objects.published()[:20]
    else:
        try:
            entries = Entry.objects.filter(blog__slug=slug, published=True)
        except InvalidBlog:
            raise Http404()
        blog = get_object_or_404(Blog, slug=slug)
        blog_title = blog.title
    
    feed_title = "Greg Newman: %s" % (blog_title)
    
    current_site = Site.objects.get_current()
    blog_url = "http://%s%s" % (current_site.domain, reverse("home-page"))
    
    if blog_title == "combined":
        url_name = "blog-feed-combined"
        kwargs = {}
    else:
        url_name = "blog-feed"
        kwargs = {"slug": blog.slug}
    feed_url = "http://%s%s" % (current_site.domain, reverse(url_name, kwargs=kwargs))

    if entries:
        feed_updated = entries[0].created_on
    else:
        feed_updated = datetime.now()
    
    # create a feed hit
    hit = FeedHit()
    hit.request_data = serialize_request(request)
    hit.save()
    
    atom = render_to_string("blog/atom_feed.xml", {
        "feed_id": feed_url,
        "feed_title": feed_title,
        "blog_url": blog_url,
        "feed_url": feed_url,
        "feed_updated": feed_updated,
        "entries": entries,
        "current_site": current_site,
    })
    return HttpResponse(atom, mimetype="application/atom+xml")

def category_feed(request, slug=None):
    """
    Atom Feeds.  Borrowed and modified from
    http://github.com/eldarion/biblion
    """

    if slug is None:
        blog_title = "category"
        entries = Entry.objects.published()[:20]
    else:
        try:
            entries = Entry.objects.filter(category__slug=slug, published=True)
        except InvalidBlog:
            raise Http404()
        category = get_object_or_404(Category, slug=slug)
    
    feed_title = "Greg Newman: %s" % (category.title)
    
    current_site = Site.objects.get_current()
    blog_url = "http://%s%s" % (current_site.domain, reverse("home-page"))
    
    url_name = "category-feed"
    kwargs = {"slug": category.slug}
    feed_url = "http://%s%s" % (current_site.domain, reverse(url_name, kwargs=kwargs))

    if entries:
        feed_updated = entries[0].created_on
    else:
        feed_updated = datetime.now()
    
    # create a feed hit
    hit = FeedHit()
    hit.request_data = serialize_request(request)
    hit.save()
    
    atom = render_to_string("blog/atom_feed.xml", {
        "feed_id": feed_url,
        "feed_title": feed_title,
        "blog_url": blog_url,
        "feed_url": feed_url,
        "feed_updated": feed_updated,
        "entries": entries,
        "current_site": current_site,
    })
    return HttpResponse(atom, mimetype="application/atom+xml")
 
