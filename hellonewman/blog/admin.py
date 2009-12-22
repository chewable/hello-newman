from django.contrib import admin
from models import *
from django.db.models import get_model
from reversion.admin import VersionAdmin


class EntryAdmin(VersionAdmin):
    ordering = ('-created_on',)
    list_display = ('title', 'published', 'created_on', 'read_count')
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

class CategoryAdmin(VersionAdmin):
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class DistractionAdmin(VersionAdmin):
    ordering = ('title',)
    list_display = ('title', 'published', 'created_on')
    list_filter = ('published',)
    save_on_top = True
    
admin.site.register(get_model('blog', 'entry'), EntryAdmin)
admin.site.register(get_model('blog', 'category'), CategoryAdmin)
admin.site.register(get_model('blog', 'distraction'), DistractionAdmin)
admin.site.register(get_model('blog', 'blog'))
