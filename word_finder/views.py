#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.wrappers import Response
from werkzeug.utils import escape

from .template import template
from .utils import inner_redirect, json_response
from .word_finder import get_words


@template('index.html')
def on_index(request):
    if request.method == 'POST':
        letters = escape(request.form['letters'])
        if len(letters) != 25:
            return {'error': 'There has to be 25 letters'}
        return inner_redirect('game', {'letters': letters})
    return {}


@template('game.html')
def on_game(request, letters):
    if request.headers.get('X-Requested-With', None) == 'XMLHttpRequest':
        own = request.form['own']
        other = request.form['other']
        neutral = request.form['neutral']
        words = get_words({'own': own, 'other': other, 'neutral': neutral})
        return json_response(words)
    return {'letters': letters}
