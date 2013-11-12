# -*- coding: utf-8 -*-

# Copyright 2013 Telefonica Investigación y Desarrollo, S.A.U
#
# This file is part of django-moqueta.
#
# django-moqueta is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# django-moqueta is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with django-moqueta. If not, see http://www.gnu.org/licenses/.
#
# For those usages not covered by the GNU Affero General Public License please
# contact with::[fabio@tid.es]

from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.base import TemplateDoesNotExist
from django.template.context import RequestContext
from django.utils import simplejson
from django.views.generic.base import View
from string import lower
from urlparse import urlparse


class GeneralMockingView(View):

    authentication = ()

    def __get_default_template_path(self, request, template_path=None):
        if template_path is None:
            template_path = request.path_info
            if self.kwargs is not None and len(self.kwargs.keys()) > 0:
                view_name = resolve(request.path_info).url_name
                args = {key: key for key in self.kwargs}
                url = reverse(view_name, kwargs=args)
                parser = urlparse(url)
                template_path = parser.path

        if not template_path.endswith('/'):
            template_path += '/'

        return template_path.lstrip('/') + lower(request.method) + '.tpl'

    def __get_body(self, request):
        if 'application/json' in request.META['CONTENT_TYPE']:
            body = simplejson.loads(request.body)
            return body
        return {}

    def get(self, request, *args, **kwargs):
        return self.generate_response_from_request(request)

    def post(self, request, *args, **kwargs):
        return self.generate_response_from_request(request)

    def update(self, request, *args, **kwargs):
        return self.generate_response_from_request(request)

    def delete(self, request, *args, **kwargs):
        return self.generate_response_from_request(request)

    def generate_response_from_request(self, request, path=None, extra=None):
        data = {
                    'body': self.__get_body(request),
                    'url_params': self.kwargs,
                    'extra': extra
            }

        path = self.__get_default_template_path(request, path)

        try:
            response = render_to_response(path,
                              data,
                              context_instance=RequestContext(request))
        except TemplateDoesNotExist:
            return HttpResponse(status=501)

        if 'HTTP_ACCEPT'in request.META:
            response['Content-Type'] = request.META['HTTP_ACCEPT']

        return response
