
from south.db import db
from django.db import models
from hellonewman.blog.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'FeedHit'
        db.create_table('blog_feedhit', (
            ('id', orm['blog.feedhit:id']),
            ('request_data', orm['blog.feedhit:request_data']),
            ('created', orm['blog.feedhit:created']),
        ))
        db.send_create_signal('blog', ['FeedHit'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'FeedHit'
        db.delete_table('blog_feedhit')
        
    
    
    models = {
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
            'created_on': ('CreationDateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'expire_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'publish_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('ModificationDateTimeField', [], {})
        },
        'blog.entry': {
            'blog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Blog']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Category']"}),
            'created_on': ('CreationDateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expire_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'markup': ('MarkupField', [], {'default': "'textile'"}),
            'publish_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'read_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'related_content': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Entry']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('ModificationDateTimeField', [], {})
        },
        'blog.feedhit': {
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_data': ('django.db.models.fields.TextField', [], {})
        }
    }
    
    complete_apps = ['blog']
