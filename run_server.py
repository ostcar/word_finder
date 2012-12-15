#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication
from werkzeug.wsgi import SharedDataMiddleware

from word_finder.wsgi import application
from word_finder.settings import DEBUG, SERVE_STATIC


if SERVE_STATIC:
    application = SharedDataMiddleware(application, {'/static': os.path.join(
        os.path.dirname(__file__), 'word_finder', 'static')})

if DEBUG:
    application = DebuggedApplication(application, evalex=True)

run_simple('localhost', 8000, application, use_reloader=True)
