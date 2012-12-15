#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.routing import Map, Rule, NotFound, RequestRedirect

url_map = Map([
    Rule('/', endpoint='index'),
    Rule('/game/<string(length=25):letters>/', endpoint='game'),
])
