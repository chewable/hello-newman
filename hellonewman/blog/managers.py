from django.db import models

class BlogManager(models.Manager):
    
    def published(self):
        return self.exclude(published=False)
    
    def current(self):
        return self.published().order_by("-title")
 
class EntryManager(models.Manager):
    
    def published(self):
        return self.exclude(published=False)
    
    def current(self):
        return self.published().order_by("-created_on")


class DistractionManager(models.Manager):
    
    def published(self):
        return self.exclude(published=False)
    
    def current(self):
        return self.published().order_by("-created_on")
