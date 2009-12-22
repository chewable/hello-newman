from django.db import models
 
class EntryManager(models.Manager):
    
    def published(self):
        return self.exclude(published=None)
    
    def current(self):
        return self.published().order_by("-created_on")


class DistractionManager(models.Manager):
    
    def published(self):
        return self.exclude(published=None)
    
    def current(self):
        return self.published().order_by("-created_on")
