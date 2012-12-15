#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.wrappers import Request
from werkzeug.exceptions import HTTPException

from .urls import url_map
import views


def dispatch(request):
    adapter = url_map.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        return getattr(views, 'on_' + endpoint)(request, **values)
    except HTTPException, e:
        return e


@Request.application
def application(request):
    return dispatch(request)
