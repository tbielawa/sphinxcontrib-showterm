#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import re
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

""" the showterm sphinx extension

* Simple Usage - Embed a video, use all defaults

.. showterm:: 7b5f8d42ba021511e627e

* Custom Usage - Use a private/third-party showterm server

.. showterm:: 7b5f8d42ba021511e627e
   :showtermurl: https://showterm.example.com

* Custom Usage - Specify a width and height

.. showterm:: 7b5f8d42ba021511e627e
   :width: 800
   :height: 600
"""

# Configuration parameter defaults

DEFAULT_SHOWTERM_URL = "https://showterm.io"
DEFAULT_TERMSHOW_WIDTH = '640px'
DEFAULT_TERMSHOW_HEIGHT = '480px'
DEFAULT_TERMSHOW_SPEED = 'slow'

def showterm_url(baseurl, id, speed=None):
    if speed is not None:
        speed = "#%s" % speed
    else:
        speed = ''
    return "{base}/{id}{speed}".format(
        base=baseurl,
        id=id,
        speed=speed)

def speed_opt(argument):
    return directives.choice(argument, ('slow', 'fast', 'stop'))

def get_size(d, key):
    if key not in d:
        return None
    m = re.match("(\d+)(|%|px)$", d[key])
    if not m:
        raise ValueError("invalid size %r" % d[key])
    return int(m.group(1)), m.group(2) or "px"


def css(d):
    return "; ".join(sorted("%s: %s" % kv for kv in d.iteritems()))


class showterm(nodes.General, nodes.Element):
    pass


def visit_showterm_node(self, node):
    width = node["width"]
    height = node["height"]
    showtermurl = node["showtermurl"]
    speed = node["speed"]

    style = {
        "width": width,
        "height": height,
        "border": "0",
    }
    attrs = {
        "src": showterm_url(showtermurl, node['id'], speed),
        "style": css(style),
        "class": "showterm showterm-%s" % node['id'],
    }
    self.body.append(self.starttag(node, "iframe", **attrs))
    self.body.append("</iframe>")


def depart_showterm_node(self, node):
    pass


class Showterm(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    # These are the legal options for this directive. Keys are the
    # option names, values are functions which assert a condition the
    # option must meet and which may possibly transform the input
    # value into a an expected Python type.
    #
    # `directives.unchanged` asserts no conditions and performs no
    # transformations, "Returns the text argument, unchanged. Returns
    # an empty string ("") if no argument is found."
    #
    # http://docutils.sourceforge.net/docs/howto/rst-directives.html#option-conversion-functions
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "speed": speed_opt,
        "showtermurl": directives.unchanged,
    }

    def run(self):
        config = self.state.document.settings.env.config
        showtermurl = self.options.get("showtermurl", config.showtermurl)
        width = self.options.get("width", config.showtermwidth)
        height = self.options.get("height", config.showtermheight)
        speed = self.options.get("speed", config.showtermspeed)

        return [showterm(id=self.arguments[0], showtermurl=showtermurl,
                         width=width, height=height, speed=speed)]


def setup(app):
    # Default showterm url, change this (in your conf.py!) if you run
    # your own private showterm server. If the parameter changes
    # between builds then the entire HTML document will be rebuilt
    app.add_config_value('showtermurl', DEFAULT_SHOWTERM_URL, 'html')

    # Default width and height
    app.add_config_value('showtermwidth', DEFAULT_TERMSHOW_WIDTH, 'html')
    app.add_config_value('showtermheight', DEFAULT_TERMSHOW_HEIGHT, 'html')

    # Default speed to play (or not) the termshow at. 'slow' is
    # actually the same as specifying no speed at all (it's the
    # default "real-time" speed)
    app.add_config_value('showtermspeed', DEFAULT_TERMSHOW_SPEED, 'html')

    app.add_node(showterm, html=(visit_showterm_node, depart_showterm_node))
    app.add_directive("showterm", Showterm)
"""
possible future params:
title - to add a title element
caption - short little bit below the cap
"""
