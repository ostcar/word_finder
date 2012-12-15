#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


with open('README.rst') as file:
    long_description = file.read()

setup(
    name='word_finder',
    description='Solve a iPhone game',
    long_description=long_description,
    version='0.1',
    url='http://github.com/ostcar/word_finder/',
    author='Oskar Hahn',
    author_email='mail@oshahn.de',
    license='Z-Lib',
    packages=find_packages(),
    include_package_data = True,
    classifiers = [
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha'
        'Environment :: Web Environment',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: zlib/libpng License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    setup_requires=[
        'versiontools >= 1.6',
    ],
    install_requires=[
        'Werkzeug==0.8.3',
        'Jinja2==2.6'
    ],
)
