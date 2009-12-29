
from south.db import db
from django.db import models
from hellonewman.blog.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Deleting field 'Distraction.updated_by'
        db.delete_column('blog_distraction', 'updated_by_id')
        
        # Deleting field 'Distraction.created_by'
        db.delete_column('blog_distraction', 'created_by_id')
        
        # Changing field 'Distraction.created_on'
        # (to signature: CreationDateTimeField())
        db.alter_column('blog_distraction', 'created_on', orm['blog.distraction:created_on'])
        
        # Changing field 'Distraction.updated_on'
        # (to signature: ModificationDateTimeField())
        db.alter_column('blog_distraction', 'updated_on', orm['blog.distraction:updated_on'])
        
    
    
    def backwards(self, orm):
        
        # Adding field 'Distraction.updated_by'
        db.add_column('blog_distraction', 'updated_by', orm['blog.distraction:updated_by'])
        
        # Adding field 'Distraction.created_by'
        db.add_column('blog_distraction', 'created_by', orm['blog.distraction:created_by'])
        
        # Changing field 'Distraction.created_on'
        # (to signature: django.db.models.fields.DateTimeField())
        db.alter_column('blog_distraction', 'created_on', orm['blog.distraction:created_on'])
        
        # Changing field 'Distraction.updated_on'
        # (to signature: django.db.models.fields.DateTimeField())
        db.alter_column('blog_distraction', 'updated_on', orm['blog.distraction:updated_on'])
        
    
    
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
        }
    }
    
    complete_apps = ['blog']
