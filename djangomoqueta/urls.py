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


from django.conf.urls import patterns, url
from views import GeneralMockingView

urlpatterns = patterns('',
    # Default mocking
    url(r'^', GeneralMockingView.as_view(), name='Mocks-GeneralMocking'),
)
