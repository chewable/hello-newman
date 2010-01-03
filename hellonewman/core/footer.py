from syncr.twitter.models import Tweet
from syncr.flickr.models import Photo
from syncr.readernaut.models import Book

def footer_feeds(request):
    books = Book.objects.all()[:8]
    return {'books': books,}
