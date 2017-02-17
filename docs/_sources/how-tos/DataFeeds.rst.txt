Data Feeds
==========

For Facebook product catalogs and Google Merchant (amongst other outlets), its simple
to create and output a data feed. Future development may offer automatic uploads, but for
now, you can simply do it manually:

1. Create a DataFeed (under App Shop Feeds > Data Feeds). By default, the filename will
be constructed from the selected Shop and code.

2. Generate the Feed. If you have only one feed, you can do something as simple as this from the shell:

.. highlight:: python

    DataFeed.objects.all()[0].generate()

3. If you see no errors, then you can generate the file with:

.. highlight:: python

    DataFeed.objects.all()[0].output_file()

4. From here, you can upload the resulting file (saved to ./_data) to your chosen merchant.
