showterm
########

A Sphinx extension to embed termshows from `showterm.io
<https://showterm.io/>`_ into your `Sphinx <http://sphinx-doc.org/>`_
documentation.

What?
#####

This extension embeds an iframe in your generated documentation which
plays back a terminal capture (i.e., everything visually that happened
in a command line shell). Terminal captures are created with the
``showterm`` utility and are uploaded to showterm.io:

Usage is very simple. Once you've uploaded a termshow, copy the
termshow ID from the URL and paste it into the ``.. showterm::``
directive::

    .. showterm:: 7b5f8d42ba021511e627e

The showterm extension allows you to specify a private showterm
server, termshow width and height, and default playback speed.

Examples/Documentation
######################

**Please** visit us on `readthedocs
<http://sphinxcontrib-showterm.rtfd.org/>`_ for full documentation,
usage examples, and extra configuration options.
