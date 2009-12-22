from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import date_based, list_detail

from hellonewman.blog.models import Entry, Distraction

def home_page(request):
    """
    Displays the page matching the given slug
    """

    entries = Entry.objects.filter(published=True)[:10]
    distractions = Distraction.objects.filter(published=True)[:6]
    
    return render_to_response('blog/home_page.html', {
        "entries": entries,
        "distractions": distractions,
    }, context_instance=RequestContext(request))

def entry_detail(request, year, month, day, slug, **kwargs):
    """
    A wrapper around ``django.views.generic.date_based.object_detail`` that
    displays the details of an ``Entry``.
        
    """
    return date_based.object_detail(
        request,
        year = year,
        month = month,
        day = day,
        slug = slug,
        queryset=Entry.objects.all(),
        date_field='created_on',
        template_object_name='entry'
    )

def archive_day(request, user):
    """
    A wrapper around ``django.views.generic.date_based.archive_day`` that
    displays an archive of entries.
    
    """
    return date_based.archive_day(
        request,
        queryset=Entry.all(),
        date_field='created_on',
        template_object_name='entry'
    )

def archive_index(request):
    """
    """
    return date_based.archive_index(
        request,
        queryset=Entry.all(),
        date_field='created_on',
        template_object_name='entry'
    )

def archive_month(request, user):
    """
    A wrapper around ``django.views.generic.date_based.archive_month`` that
    displays an archive of entries for the given month.
    
    """
    return date_based.archive_month(
        request,
        queryset=Entry.all(),
        date_field='created_on',
        template_object_name='entry'
    )

def archive_year(request, user):
    """
    A wrapper around ``django.views.generic.date_based.archive_year`` that
    displays an archive of entries for the given year.
    
    """
    return date_based.archive_year(
        request,
        queryset=Entry.all(),
        date_field='created_on',
        make_object_list=True,
        template_object_name='entry'
    )