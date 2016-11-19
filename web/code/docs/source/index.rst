.. Django DTG Store Manager documentation master file, created by
   sphinx-quickstart on Thu Nov 17 06:27:17 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django DTG Store Manager's documentation!
====================================================

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

To Generate a model graph (somewhat) editable in Illustrator:

$ ./manage.py graph_models -g creative catalog outlet_woo product > models.dot
$ dot -Gsize=117,165 -Gdpi=60 -omodels.svg -Tsvg models.dot
