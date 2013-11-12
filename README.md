# Django Moqueta

**Awesome RESTful-web mocking application.**

# Overview

Django-moqueta is a Django application that allows you to simulate the behavior of complex, real JSON RESTful-web resources for testing purposes.
You can create a mock in an easy way just by creating a file in the template directory path that maps with the URL one.

# Requirements

* Python 2.7
* Django 1.5

# Installation

Install using `setup.py` (or just copy `djangomoqueta` application directory into your Django project):

```console
$ python setup.py install
```

Add `'djangomoqueta'` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = (
    [...]
    
    'djangomoqueta',        
)
```
  
Include the `djangomoqueta` URLs to a path at the end of your `url.py` file:

```python	
urlpatterns = patterns('',
	[...]

    # Default mocking
    url(r'^', include('djangomoqueta.urls')),
)
```

# Getting started

## Default use

1. Create a directory path in your `templates` directory by following the directory tree hierarchy that expresses the URL web path of the REST resource.

2. Create a `<method>.tpl` file, where `<method>` is the HTTP verb of the REST resource you are mocking: `get.tpl`, `post.tpl`, `put.tpl` or `delete.tpl`.

3. Write the JSON response template in that file by using Django’s built-in template tags and filters.

Considerations:

1. By default, the HTTP response status is `HTTP 200-OK`.

2. You can access to request body content in your template by using `{{body.<field>}}`.

3. You can access to request URL parameters in your template by using `{{url_params.<parameter>}}`.

## Customizing mock behavior

### Customized views

1. Create a view that inherits from `GeneralMockingView` in `views.py`:

```python
from djangomoqueta.views import GeneralMockingView

class ExampleView(GeneralMockingView):
def post(self, request):
	[...]
	
    response = GeneralMockingView.generate_response_from_request(self, request)
    
    return response
```

2. Add the view to `urls.py` file:

```python
urlpatterns = patterns('',
		url(r'^$', ExampleView.as_view(), name='Mocks-Example'),
	)

```

### Response status

Change status code in response object.

```python
class BooksView(GeneralMockingView):
	def post(self, request):
		[...]
        response = GeneralMockingView.generate_response_from_request(self, request)
        
        response.status_code = 201
        
        return response
```

### Dynamic URL path

Use named regular-expression groups `(?P<name>pattern)`, where `name` is the name of the group and `pattern` is some pattern to match.

```python
urlpatterns = patterns('',
    url(r'^(?P<book_id>\w+)/?$', BookView.as_view(), name='Mocks-Book'),
)
```

### Additional data

Create a dictionary and add it as `extra` parameter in `generate_response_from_request` function.

```python
class BookView(GeneralMockingView):
    def put(self, request, book_id):
    	[...]
        extra = {'update_time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}
        
        return GeneralMockingView.generate_response_from_request(self, request, 
        														 extra=extra)
```

You can access to that information in your template by using `{{extra.<field>}}`.

### Headers

Add the header as response dictionary field.

```python
class BooksView(GeneralMockingView):

    def post(self, request):
		[...]
        response = GeneralMockingView.generate_response_from_request(self, request, 
																	 extra=extra)
        
        [...]
        response['Location'] = request.build_absolute_uri(reverse('Mocks-Book', 
        												  args=(book_id,)))
        
        return response
```

# Executing mock server

To start the mock application in 8000 port, for example, just type:

```console
$ python manage.py runserver 0.0.0.0:8000
```

# License

Affero General Public License (GPL) version 3.
