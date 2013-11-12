from django.conf.urls import patterns, url
from books.views import BooksView, BookView

urlpatterns = patterns('',
    # Examples: Books API
    url(r'^$', BooksView.as_view(), name='Mocks-Books'),
    url(r'^(?P<book_id>\w+)/?$', BookView.as_view(), name='Mocks-Book'),
)
