from syncr.twitter.models import Tweet
from syncr.flickr.models import Photo
from syncr.readernaut.models import Book

def footer_feeds(request):
    flickr_photos = Photo.objects.all()[:6]
    tweets = Tweet.objects.all().order_by("-pub_time")[:5]
    books = Book.objects.all()[:2]
    return {'flickr_photos': flickr_photos,
            'tweets': tweets,
            'books': books,}
