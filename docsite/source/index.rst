.. highlight:: rest


.. default-domain:: rst


Sphinx Showterm
###############

A Sphinx extension to embed termshows from `showterm.io
<https://showterm.io/>`_ into your `Sphinx <http://sphinx-doc.org/>`_
documentation.


.. toctree::
   :maxdepth: 2
   :numbered:


Example
*******

Below is the example termshow from the `showterm.io homepage
<https://showterm.io/>`_. It is embedded in this document using the
``showterm`` extension.:

.. showterm:: 7b5f8d42ba021511e627e


Usage
*****

.. rst:directive:: .. showterm:: showterm_id

   The :rst:dir:`showterm` directive requires one argument:
   ``showterm_id``, the ID of your termshow.

   For example, *the example* termshow on the showterm.io homepage is
   ``7b5f8d42ba021511e627e``. We could embed it in a reST document
   like this::

      .. showterm:: 7b5f8d42ba021511e627e

   The showterm.io service can also be `ran privately
   <https://github.com/ConradIrwin/showterm.io>`_. If you're running
   your own showterm server you can set the showterm domain with the
   ``showtermurl`` flag option. For example, if your showterm domain
   were ``https://showterm.example.com``::

      .. showterm:: 7b5f8d42ba021511e627e
         :showtermurl: https://showterm.example.com

   .. note:: Trailing slashes in the ``showtermurl`` are
             insignificant. All URLs are normalized prior to document
             rendering.

   It's OK if we're not running the showterm service at the root
   location of our domain. We can include the location in the option
   argument too. For example, if our showterm service is running under
   ``https://utils.example.com/showterm/``::

      .. showterm:: 7b5f8d42ba021511e627e
         :showtermurl: https://utils.example.com/showterm/
