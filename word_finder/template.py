#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from werkzeug.wrappers import Response
from jinja2 import Environment, FileSystemLoader

template_path = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)


def render_template(template_name, **context):
    t = jinja_env.get_template(template_name)
    return Response(t.render(context), mimetype='text/html')


def template(template_name):
    def renderer(func):
        def wrapper(request, *args, **kwargs):
            context = func(request, *args, **kwargs)
            if not type(context) is dict:
                return context
            return render_template(template_name, **context)
        return wrapper
    return renderer
