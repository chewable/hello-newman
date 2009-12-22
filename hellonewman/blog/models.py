from datetime import datetime
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from hellonewman import settings
from django_markup.fields import MarkupField
from django.db.models import get_model, permalink
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField

tagging = models.get_app('tagging')
from tagging.fields import TagField
from blog.managers import EntryManager, DistractionManager

class Blog(models.Model):
    """
    Base class for blogs.
    Each entry must be assigned to a blog but can also
    reside in multiple blogs.
    The blog model class will allow entries to be
    segregated by content type. ie art, code, photography
    """

    title = models.CharField(_('Title'), max_length=100, help_text=_("Name for this blog. ie 'Art'"))
    slug = AutoSlugField(populate_from='title')
    published = models.BooleanField(_('Published'), default=True)
    created_on = CreationDateTimeField()
    updated_on = ModificationDateTimeField()
    
    class Meta:
        ordering = ['title',]

    def __unicode__(self):
        return self.title
    
class Category(models.Model):
    """
    Base class for categories.
    Each entry should be assigned a category
    """
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True, help_text=_("This is a unique identifier that allows your page to display its detail view, ex 'this-is-my-title'"))

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title',]

    def __unicode__(self):
        return self.title

class Entry(models.Model):
    """
    Base class for blog entries
    """
    
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True, help_text=_("This is a unique identifier that allows your page to display its detail view, ex 'this-is-my-title'"))

    excerpt = models.TextField(_('Excerpt'), blank=True, null=True, help_text=_("This is a teaser of the body text; optional"))
    body = models.TextField(_('Body'), blank=False, null=False)

    # markup
    markup = MarkupField(default='textile')
    
    # Meta
    keywords = models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True)
    description = models.TextField(_('Meta Description'), null=True, blank=True)
    tags = TagField()

    # relations
    related_content = models.ManyToManyField("self", null=True, blank=True)
    # category assignment
    category = models.ManyToManyField(Category)
    blog = models.ManyToManyField(Blog)
    
    # flags
    published = models.BooleanField(_('Published'), default=True, help_text=_("If unchecked the page will not be accessible to users"))

    # dates
    publish_on = models.DateTimeField(_('Publish On'), null=True, blank=True)
    expire_on = models.DateTimeField(_('Expire On'), null=True, blank=True)

    read_count = models.IntegerField(default=0, editable=False)
    created_on = CreationDateTimeField()
    updated_on = ModificationDateTimeField()

    class Meta:
        ordering = ['-created_on', ]
        verbose_name_plural = 'Entries'
        
    def __unicode__(self):
        return self.title

    objects = EntryManager()

    @permalink
    def get_absolute_url(self):
        return ('entry-detail', None, {
            'year': self.created_on.year,
            'month': self.created_on.strftime('%b').lower(),
            'day': self.created_on.day,
            'slug': self.slug
        })

    def is_published(self):
        return self.published

    def increase_read_count(self):
        self.read_count += 1
        self.save()


class Distraction(models.Model):
    """
    Base class for external links that I call distractions.
    """
    title = models.CharField(_('Title'), max_length=200)
    description = models.TextField(_('Description'))
    link = models.URLField(verify_exists=True, max_length=200, null=False, blank=False)

    # flags
    published = models.BooleanField(_('Published'), default=True, help_text=_("If unchecked the page will not be accessible to users"))

    # dates
    publish_on = models.DateTimeField(_('Publish On'), null=True, blank=True)
    expire_on = models.DateTimeField(_('Expire On'), null=True, blank=True)

    created_by = models.ForeignKey(User, null=True, editable=False, related_name="%(class)s_created_by")
    created_on = models.DateTimeField(_('Created On'), default=datetime.now, editable=False)
    updated_on = models.DateTimeField(_('Updated On'), editable=False)
    updated_by = models.ForeignKey(User, null=True, editable=False)
    
    class Meta:
        ordering = ['-created_on', ]

    def __unicode__(self):
        return self.title

    objects = DistractionManager()

    def save(self, *args, **kwargs):
        self.updated_on = datetime.now()
        super(Distraction, self).save()

    def is_published(self):
        return self.published
