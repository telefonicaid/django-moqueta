from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^books/', include('books.urls')),

    # Default mocking
    url(r'^', include('djangomoqueta.urls')),
)
