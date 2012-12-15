#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from werkzeug.utils import redirect
from werkzeug.wrappers import Response

from .urls import url_map
from .settings import DOMAIN


def inner_redirect(url_name, values):
    adapter = url_map.bind(DOMAIN)
    return redirect(adapter.build(url_name, values))


def json_response(data):
    return Response(json.dumps(data))
