
from south.db import db
from django.db import models
from hellonewman.blog.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Entry'
        db.create_table('blog_entry', (
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(_('Title'), max_length=200)),
            ('slug', models.SlugField(_('Slug'), unique=True, max_length=100)),
            ('excerpt', models.TextField(_('Excerpt'), null=True, blank=True)),
            ('body', models.TextField(_('Body'), null=False, blank=False)),
            ('markup', MarkupField(default='textile')),
            ('keywords', models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True)),
            ('description', models.TextField(_('Meta Description'), null=True, blank=True)),
            ('tags', TagField()),
            ('category', models.ForeignKey(orm.Category)),
            ('published', models.BooleanField(_('Published'), default=True)),
            ('publish_on', models.DateTimeField(_('Publish On'), null=True, blank=True)),
            ('expire_on', models.DateTimeField(_('Expire On'), null=True, blank=True)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="%(class)s_created_by", null=True, editable=False)),
            ('created_on', models.DateTimeField(_('Created On'), default=datetime.datetime.now, editable=False)),
            ('updated_on', models.DateTimeField(_('Updated On'), editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], null=True, editable=False)),
        ))
        db.send_create_signal('blog', ['Entry'])
        
        # Adding model 'Distraction'
        db.create_table('blog_distraction', (
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(_('Title'), max_length=200)),
            ('description', models.TextField(_('Description'))),
            ('link', models.URLField(blank=False, max_length=200, null=False, verify_exists=True)),
            ('published', models.BooleanField(_('Published'), default=True)),
            ('publish_on', models.DateTimeField(_('Publish On'), null=True, blank=True)),
            ('expire_on', models.DateTimeField(_('Expire On'), null=True, blank=True)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="%(class)s_created_by", null=True, editable=False)),
            ('created_on', models.DateTimeField(_('Created On'), default=datetime.datetime.now, editable=False)),
            ('updated_on', models.DateTimeField(_('Updated On'), editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], null=True, editable=False)),
        ))
        db.send_create_signal('blog', ['Distraction'])
        
        # Adding model 'Category'
        db.create_table('blog_category', (
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(_('Title'), max_length=200)),
            ('slug', models.SlugField(_('Slug'), unique=True, max_length=100)),
        ))
        db.send_create_signal('blog', ['Category'])
        
        # Adding ManyToManyField 'Entry.related_content'
        db.create_table('blog_entry_related_content', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_entry', models.ForeignKey(orm.Entry, null=False)),
            ('to_entry', models.ForeignKey(orm.Entry, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Entry'
        db.delete_table('blog_entry')
        
        # Deleting model 'Distraction'
        db.delete_table('blog_distraction')
        
        # Deleting model 'Category'
        db.delete_table('blog_category')
        
        # Dropping ManyToManyField 'Entry.related_content'
        db.delete_table('blog_entry_related_content')
        
    
    
    models = {
        'blog.entry': {
            'Meta': {'ordering': "['-created_on',]"},
            'body': ('models.TextField', ["_('Body')"], {'null': 'False', 'blank': 'False'}),
            'category': ('models.ForeignKey', ["orm['blog.Category']"], {}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"%(class)s_created_by"', 'null': 'True', 'editable': 'False'}),
            'created_on': ('models.DateTimeField', ["_('Created On')"], {'default': 'datetime.datetime.now', 'editable': 'False'}),
            'description': ('models.TextField', ["_('Meta Description')"], {'null': 'True', 'blank': 'True'}),
            'excerpt': ('models.TextField', ["_('Excerpt')"], {'null': 'True', 'blank': 'True'}),
            'expire_on': ('models.DateTimeField', ["_('Expire On')"], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('models.CharField', ["_('Meta Keywords')"], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'markup': ('MarkupField', [], {'default': "'textile'"}),
            'publish_on': ('models.DateTimeField', ["_('Publish On')"], {'null': 'True', 'blank': 'True'}),
            'published': ('models.BooleanField', ["_('Published')"], {'default': 'True'}),
            'related_content': ('models.ManyToManyField', ["orm['blog.Entry']"], {'null': 'True', 'blank': 'True'}),
            'slug': ('models.SlugField', ["_('Slug')"], {'unique': 'True', 'max_length': '100'}),
            'tags': ('TagField', [], {}),
            'title': ('models.CharField', ["_('Title')"], {'max_length': '200'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'null': 'True', 'editable': 'False'}),
            'updated_on': ('models.DateTimeField', ["_('Updated On')"], {'editable': 'False'})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'blog.distraction': {
            'Meta': {'ordering': "['-created_on',]"},
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"%(class)s_created_by"', 'null': 'True', 'editable': 'False'}),
            'created_on': ('models.DateTimeField', ["_('Created On')"], {'default': 'datetime.datetime.now', 'editable': 'False'}),
            'description': ('models.TextField', ["_('Description')"], {}),
            'expire_on': ('models.DateTimeField', ["_('Expire On')"], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'link': ('models.URLField', [], {'blank': 'False', 'max_length': '200', 'null': 'False', 'verify_exists': 'True'}),
            'publish_on': ('models.DateTimeField', ["_('Publish On')"], {'null': 'True', 'blank': 'True'}),
            'published': ('models.BooleanField', ["_('Published')"], {'default': 'True'}),
            'title': ('models.CharField', ["_('Title')"], {'max_length': '200'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'null': 'True', 'editable': 'False'}),
            'updated_on': ('models.DateTimeField', ["_('Updated On')"], {'editable': 'False'})
        },
        'blog.category': {
            'Meta': {'ordering': "['title',]"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'slug': ('models.SlugField', ["_('Slug')"], {'unique': 'True', 'max_length': '100'}),
            'title': ('models.CharField', ["_('Title')"], {'max_length': '200'})
        }
    }
    
    complete_apps = ['blog']
