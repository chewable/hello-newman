from django.conf import settings
from blog.models import Blog

def contact_email(request):
    return {'contact_email': getattr(settings, 'CONTACT_EMAIL', '')}

def site_name(request):
    return {'site_name': getattr(settings, 'SITE_NAME', '')}

def journals(request):
    journals = Blog.objects.all()
    return {'journals': journals}
