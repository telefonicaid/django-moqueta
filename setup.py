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


#!/usr/bin/env python


import os
from setuptools import find_packages
from distutils.core import setup

basepath = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(basepath, 'requirements.txt')) as f:
    required = f.read().splitlines()

packages = find_packages(basepath)

# http://bugs.python.org/issue8876
if hasattr(os, 'link'):
    delattr(os, 'link')

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]

setup(
    name='djangomoqueta',
    version='0.1.0',
    author='Juan Fabio Garcia Solero',
    description=('Deploy your RESTful web mocks in an easy way.'),
    license='MIT License',
    keywords='REST JSON mocks',
    include_package_data=True,
    packages=get_packages('djangomoqueta'),
    install_requires=required,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: Affero General Public License (GPL) version 3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
