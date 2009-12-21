# Django settings for tracktice project.
import os

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Greg Newman', 'greg@20seven.org'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'newman.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../static')
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://s3.amazonaws.com/grappelli/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&jpg$9^-+5tvymn_jm_+08zp*i2ej3-zh=3zjt%w%%-hu5t-v('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'hellonewman.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, '../templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'hellonewman.core.context_processors.contact_email',
    'hellonewman.core.footer.footer_feeds',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',

    # Third Party
    'grappelli',
    'compressor',
    'syncr.flickr',
    'syncr.twitter',
    'syncr.readernaut',
    'south',
    'tagging',
    'django_extensions',
#    'contact_form',
    'tagging',
    'django_markup',
    'reversion',
    'disqus',

    # local
    'hellonewman.core',
    'hellonewman.blog',
)

MARKUP_CHOICES = (
    'none',
    'textile',
    'linebreaks',
    'markdown',
    'restructuredtext',
    )

GRAPPELLI_ADMIN_TITLE = 'Hello Newman'

COMPRESS_VERSION = True
#CSSTIDY_BINARY = '/usr/local/bin/csstidy'
COMPRESS_CSS = {
    'screen': {
        'source_filenames': ('css/reset.css', 'css/screen.css'),
        'output_filename': 'c/screen.r?.css',
        'extra_context': { 'media': 'screen,projection' }
    },
#    'print': {
#        'source_filenames': ('static/css/print.css',),
#        'output_filename': 'c/print.r?.css',
#        'extra_context': { 'media': 'print' }
#    }
}
COMPRESS_JS_FILTERS = None
#COMPRESS_JS = {
#    'scripts': {
#        'source_filenames': ('static/js/impact.js',),
#        'output_filename': 'c/scripts.r?.js'
#    }
#}

#syncr stuffz
READERNAUT_USERNAME = ''
FLICKR_API_KEY = ''
FLICKR_API_SECRET = ''

DEFAULT_FROM_EMAIL = ''
DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = ''

# Use local_settings.py for things to override privately
try:
    from local_settings import *
except ImportError:
    pass
