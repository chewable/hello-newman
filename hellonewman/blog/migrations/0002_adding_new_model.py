
from south.db import db
from django.db import models
from hellonewman.blog.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Blog'
        db.create_table('blog_blog', (
            ('id', orm['blog.blog:id']),
            ('title', orm['blog.blog:title']),
            ('slug', orm['blog.blog:slug']),
            ('published', orm['blog.blog:published']),
            ('created_on', orm['blog.blog:created_on']),
            ('updated_on', orm['blog.blog:updated_on']),
        ))
        db.send_create_signal('blog', ['Blog'])
        
        # Deleting field 'Entry.created_by'
        db.delete_column('blog_entry', 'created_by_id')
        
        # Deleting field 'Entry.updated_by'
        db.delete_column('blog_entry', 'updated_by_id')
        
        # Changing field 'Entry.body'
        # (to signature: django.db.models.fields.TextField())
        db.alter_column('blog_entry', 'body', orm['blog.entry:body'])
        
        # Changing field 'Entry.category'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['blog.Category']))
        db.alter_column('blog_entry', 'category_id', orm['blog.entry:category'])
        
        # Changing field 'Entry.description'
        # (to signature: django.db.models.fields.TextField(null=True, blank=True))
        db.alter_column('blog_entry', 'description', orm['blog.entry:description'])
        
        # Changing field 'Entry.title'
        # (to signature: django.db.models.fields.CharField(max_length=200))
        db.alter_column('blog_entry', 'title', orm['blog.entry:title'])
        
        # Changing field 'Entry.expire_on'
        # (to signature: django.db.models.fields.DateTimeField(null=True, blank=True))
        db.alter_column('blog_entry', 'expire_on', orm['blog.entry:expire_on'])
        
        # Changing field 'Entry.tags'
        # (to signature: tagging.fields.TagField())
        db.alter_column('blog_entry', 'tags', orm['blog.entry:tags'])
        
        # Changing field 'Entry.excerpt'
        # (to signature: django.db.models.fields.TextField(null=True, blank=True))
        db.alter_column('blog_entry', 'excerpt', orm['blog.entry:excerpt'])
        
        # Changing field 'Entry.publish_on'
        # (to signature: django.db.models.fields.DateTimeField(null=True, blank=True))
        db.alter_column('blog_entry', 'publish_on', orm['blog.entry:publish_on'])
        
        # Changing field 'Entry.created_on'
        # (to signature: CreationDateTimeField())
        db.alter_column('blog_entry', 'created_on', orm['blog.entry:created_on'])
        
        # Changing field 'Entry.published'
        # (to signature: django.db.models.fields.BooleanField(blank=True))
        db.alter_column('blog_entry', 'published', orm['blog.entry:published'])
        
        # Changing field 'Entry.keywords'
        # (to signature: django.db.models.fields.CharField(max_length=200, null=True, blank=True))
        db.alter_column('blog_entry', 'keywords', orm['blog.entry:keywords'])
        
        # Changing field 'Entry.updated_on'
        # (to signature: ModificationDateTimeField())
        db.alter_column('blog_entry', 'updated_on', orm['blog.entry:updated_on'])
        
        # Changing field 'Entry.slug'
        # (to signature: django.db.models.fields.SlugField(unique=True, max_length=100, db_index=True))
        db.alter_column('blog_entry', 'slug', orm['blog.entry:slug'])
        
        # Changing field 'Distraction.updated_by'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['auth.User'], null=True))
        db.alter_column('blog_distraction', 'updated_by_id', orm['blog.distraction:updated_by'])
        
        # Changing field 'Distraction.title'
        # (to signature: django.db.models.fields.CharField(max_length=200))
        db.alter_column('blog_distraction', 'title', orm['blog.distraction:title'])
        
        # Changing field 'Distraction.expire_on'
        # (to signature: django.db.models.fields.DateTimeField(null=True, blank=True))
        db.alter_column('blog_distraction', 'expire_on', orm['blog.distraction:expire_on'])
        
        # Changing field 'Distraction.publish_on'
        # (to signature: django.db.models.fields.DateTimeField(null=True, blank=True))
        db.alter_column('blog_distraction', 'publish_on', orm['blog.distraction:publish_on'])
        
        # Changing field 'Distraction.created_by'
        # (to signature: django.db.models.fields.related.ForeignKey(null=True, to=orm['auth.User']))
        db.alter_column('blog_distraction', 'created_by_id', orm['blog.distraction:created_by'])
        
        # Changing field 'Distraction.created_on'
        # (to signature: django.db.models.fields.DateTimeField())
        db.alter_column('blog_distraction', 'created_on', orm['blog.distraction:created_on'])
        
        # Changing field 'Distraction.link'
        # (to signature: django.db.models.fields.URLField(max_length=200))
        db.alter_column('blog_distraction', 'link', orm['blog.distraction:link'])
        
        # Changing field 'Distraction.published'
        # (to signature: django.db.models.fields.BooleanField(blank=True))
        db.alter_column('blog_distraction', 'published', orm['blog.distraction:published'])
        
        # Changing field 'Distraction.updated_on'
        # (to signature: django.db.models.fields.DateTimeField())
        db.alter_column('blog_distraction', 'updated_on', orm['blog.distraction:updated_on'])
        
        # Changing field 'Distraction.description'
        # (to signature: django.db.models.fields.TextField())
        db.alter_column('blog_distraction', 'description', orm['blog.distraction:description'])
        
        # Changing field 'Category.slug'
        # (to signature: django.db.models.fields.SlugField(unique=True, max_length=100, db_index=True))
        db.alter_column('blog_category', 'slug', orm['blog.category:slug'])
        
        # Changing field 'Category.title'
        # (to signature: django.db.models.fields.CharField(max_length=200))
        db.alter_column('blog_category', 'title', orm['blog.category:title'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Blog'
        db.delete_table('blog_blog')
        
        # Adding field 'Entry.created_by'
        db.add_column('blog_entry', 'created_by', orm['blog.entry:created_by'])
        
        # Adding field 'Entry.updated_by'
        db.add_column('blog_entry', 'updated_by', orm['blog.entry:updated_by'])
        
        # Changing field 'Entry.body'
        # (to signature: models.TextField(_('Body'), null=False, blank=False))
        db.alter_column('blog_entry', 'body', orm['blog.entry:body'])
        
        # Changing field 'Entry.category'
        # (to signature: models.ForeignKey(orm['blog.Category']))
        db.alter_column('blog_entry', 'category_id', orm['blog.entry:category'])
        
        # Changing field 'Entry.description'
        # (to signature: models.TextField(_('Meta Description'), null=True, blank=True))
        db.alter_column('blog_entry', 'description', orm['blog.entry:description'])
        
        # Changing field 'Entry.title'
        # (to signature: models.CharField(_('Title'), max_length=200))
        db.alter_column('blog_entry', 'title', orm['blog.entry:title'])
        
        # Changing field 'Entry.expire_on'
        # (to signature: models.DateTimeField(_('Expire On'), null=True, blank=True))
        db.alter_column('blog_entry', 'expire_on', orm['blog.entry:expire_on'])
        
        # Changing field 'Entry.tags'
        # (to signature: TagField())
        db.alter_column('blog_entry', 'tags', orm['blog.entry:tags'])
        
        # Changing field 'Entry.excerpt'
        # (to signature: models.TextField(_('Excerpt'), null=True, blank=True))
        db.alter_column('blog_entry', 'excerpt', orm['blog.entry:excerpt'])
        
        # Changing field 'Entry.publish_on'
        # (to signature: models.DateTimeField(_('Publish On'), null=True, blank=True))
        db.alter_column('blog_entry', 'publish_on', orm['blog.entry:publish_on'])
        
        # Changing field 'Entry.created_on'
        # (to signature: models.DateTimeField(_('Created On'), editable=False))
        db.alter_column('blog_entry', 'created_on', orm['blog.entry:created_on'])
        
        # Changing field 'Entry.published'
        # (to signature: models.BooleanField(_('Published')))
        db.alter_column('blog_entry', 'published', orm['blog.entry:published'])
        
        # Changing field 'Entry.keywords'
        # (to signature: models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True))
        db.alter_column('blog_entry', 'keywords', orm['blog.entry:keywords'])
        
        # Changing field 'Entry.updated_on'
        # (to signature: models.DateTimeField(_('Updated On'), editable=False))
        db.alter_column('blog_entry', 'updated_on', orm['blog.entry:updated_on'])
        
        # Changing field 'Entry.slug'
        # (to signature: models.SlugField(_('Slug'), max_length=100, unique=True))
        db.alter_column('blog_entry', 'slug', orm['blog.entry:slug'])
        
        # Changing field 'Distraction.updated_by'
        # (to signature: models.ForeignKey(orm['auth.User'], null=True, editable=False))
        db.alter_column('blog_distraction', 'updated_by_id', orm['blog.distraction:updated_by'])
        
        # Changing field 'Distraction.title'
        # (to signature: models.CharField(_('Title'), max_length=200))
        db.alter_column('blog_distraction', 'title', orm['blog.distraction:title'])
        
        # Changing field 'Distraction.expire_on'
        # (to signature: models.DateTimeField(_('Expire On'), null=True, blank=True))
        db.alter_column('blog_distraction', 'expire_on', orm['blog.distraction:expire_on'])
        
        # Changing field 'Distraction.publish_on'
        # (to signature: models.DateTimeField(_('Publish On'), null=True, blank=True))
        db.alter_column('blog_distraction', 'publish_on', orm['blog.distraction:publish_on'])
        
        # Changing field 'Distraction.created_by'
        # (to signature: models.ForeignKey(orm['auth.User'], null=True, editable=False))
        db.alter_column('blog_distraction', 'created_by_id', orm['blog.distraction:created_by'])
        
        # Changing field 'Distraction.created_on'
        # (to signature: models.DateTimeField(_('Created On'), editable=False))
        db.alter_column('blog_distraction', 'created_on', orm['blog.distraction:created_on'])
        
        # Changing field 'Distraction.link'
        # (to signature: models.URLField(max_length=200, null=False, verify_exists=True, blank=False))
        db.alter_column('blog_distraction', 'link', orm['blog.distraction:link'])
        
        # Changing field 'Distraction.published'
        # (to signature: models.BooleanField(_('Published')))
        db.alter_column('blog_distraction', 'published', orm['blog.distraction:published'])
        
        # Changing field 'Distraction.updated_on'
        # (to signature: models.DateTimeField(_('Updated On'), editable=False))
        db.alter_column('blog_distraction', 'updated_on', orm['blog.distraction:updated_on'])
        
        # Changing field 'Distraction.description'
        # (to signature: models.TextField(_('Description')))
        db.alter_column('blog_distraction', 'description', orm['blog.distraction:description'])
        
        # Changing field 'Category.slug'
        # (to signature: models.SlugField(_('Slug'), max_length=100, unique=True))
        db.alter_column('blog_category', 'slug', orm['blog.category:slug'])
        
        # Changing field 'Category.title'
        # (to signature: models.CharField(_('Title'), max_length=200))
        db.alter_column('blog_category', 'title', orm['blog.category:title'])
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'blog.blog': {
            'created_on': ('CreationDateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('AutoSlugField', [], {'populate_from': "'title'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_on': ('ModificationDateTimeField', [], {})
        },
        'blog.category': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'blog.distraction': {
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'distraction_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'expire_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'publish_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        'blog.entry': {
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'created_on': ('CreationDateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expire_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'markup': ('MarkupField', [], {'default': "'textile'"}),
            'publish_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'related_content': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Entry']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('ModificationDateTimeField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['blog']
