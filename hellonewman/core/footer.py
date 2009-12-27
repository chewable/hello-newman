from syncr.twitter.models import Tweet
from syncr.flickr.models import Photo
from syncr.readernaut.models import Book

def footer_feeds(request):
    flickr_photos = Photo.objects.all()[:6]
    books = Book.objects.all()[:4]
    return {'flickr_photos': flickr_photos,
            'books': books,}
