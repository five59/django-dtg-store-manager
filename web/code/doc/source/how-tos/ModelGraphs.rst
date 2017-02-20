Model Graphs
============

To Generate a model diagram graphic (somewhat) editable in Illustrator, you can use the `graph_models` command:

.. code-block:: bash

   $ ./manage.py graph_models -g {appnames} > ./_data/models.dot
   $ dot -Gsize=117,165 -Gdpi=60 -o./_data/models.svg -Tsvg ./_data/models.dot

If you'd like to shorten it, simply do:

.. code-block:: bash

   $ ./manage.py graph_models -g -A -o models.png

Adjust as you need. The bash commands below generate a diagram that fits within an A3 sheet. It creates it as an
SVG file, which seems to be the best format for Illustrator.

.. code-block:: bash

   $ ./manage.py graph_models -g business > ./_data/bz.dot
   $ ./manage.py graph_models -g outlet_woocommerce > ./_data/wc.dot
   $ ./manage.py graph_models -g vendor_printful > ./_data/pf.dot

   $ dot -Gsize=117,165 -Gdpi=60 -o./_data/bz.svg -Tsvg ./_data/bz.dot
   $ dot -Gsize=117,165 -Gdpi=60 -o./_data/wc.svg -Tsvg ./_data/wc.dot
   $ dot -Gsize=117,165 -Gdpi=60 -o./_data/pf.svg -Tsvg ./_data/pf.dot

I prefer having separate diagrams for each app, but you can also combine them into a single chart like this:

.. code-block:: bash

   $ ./manage.py graph-models -g business outlet_woocommerce vendor_printful > ./_data/all.dot
   $ dot -Gsize=117,165 -Gdpi=60 -o./_data/all.svg -Tsvg ./_data/all.dot
