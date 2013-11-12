from datetime import datetime
from djangomoqueta.views import GeneralMockingView
import random
from django.core.urlresolvers import reverse


class BooksView(GeneralMockingView):

    def post(self, request):
        book_id = random.randint(1, 999999)
        extra = {'id': book_id,
                 'creation_time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}

        response = GeneralMockingView.generate_response_from_request(self,
                                                                     request,
                                                                     extra=extra)
        response.status_code = 201
        response['Location'] = request.build_absolute_uri(reverse('Mocks-Book',
                                                                  args=(book_id,)))

        return response


class BookView(GeneralMockingView):

    def put(self, request, book_id):
        extra = {'update_time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}
        return GeneralMockingView.generate_response_from_request(self,
                                                                 request,
                                                                 extra=extra)

    def delete(self, request, book_id):
        response = GeneralMockingView.generate_response_from_request(self,
                                                                     request)
        response.status_code = 204
        return response
