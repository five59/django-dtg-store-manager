Model Graphs
============

To Generate a model diagram graphic (somewhat) editable in Illustrator, you can use the `graph_models` command:

.. highlight:: bash

    ./manage.py graph_models -g {appnames} > ./_data/models.dot
    dot -Gsize=117,165 -Gdpi=60 -o./_data/models.svg -Tsvg ./_data/models.dot

Adjust as you need. The settings above generate a diagram that fits within an A3 sheet. It creates it as an
SVG file, which seems to be the best format for Illustrator to contend with.

./manage.py graph_models -g api_gooten > ./_data/mod1.dot
./manage.py graph_models -g app_care > ./_data/mod2.dot
./manage.py graph_models -g app_shopfeeds > ./_data/mod3.dot
./manage.py graph_models -g catalog > ./_data/mod4.dot
./manage.py graph_models -g creative > ./_data/mod5.dot
./manage.py graph_models -g outlet_woo > ./_data/mod6.dot

dot -Gsize=117,165 -Gdpi=60 -o./_data/mod1.svg -Tsvg ./_data/mod1.dot
dot -Gsize=117,165 -Gdpi=60 -o./_data/mod2.svg -Tsvg ./_data/mod2.dot
dot -Gsize=117,165 -Gdpi=60 -o./_data/mod3.svg -Tsvg ./_data/mod3.dot
dot -Gsize=117,165 -Gdpi=60 -o./_data/mod4.svg -Tsvg ./_data/mod4.dot
dot -Gsize=117,165 -Gdpi=60 -o./_data/mod5.svg -Tsvg ./_data/mod5.dot
dot -Gsize=117,165 -Gdpi=60 -o./_data/mod6.svg -Tsvg ./_data/mod6.dot
