import sys
import io
import json
import warnings
from collections import OrderedDict
from django.apps import apps
from django.core import serializers
from django.core import management
from django.db import DEFAULT_DB_ALIAS, router
from django.core.management.utils import *
from django.core.management.base import BaseCommand, CommandError
from catalog.models import *
from importlib import import_module


class Command(BaseCommand):
    help = "Perform an update from the remote API. Requires the API code specified in the Manufacturer model."

    missing_arg_message = "You must provide an API code so that we know which API to connect to."

    def add_arguments(self, parser):
        parser.add_argument(
            'manufacturer_code', help='Code for the requested manufacturer (stored in the admin).')

    def handle(self, *args, **options):
        mf_option = options.pop('manufacturer_code')
        try:
            manufacturer = Manufacturer.objects.get(code=mf_option.upper())
            self.stdout.write("--> Ingest from {}.".format(manufacturer))
        except:
            raise CommandError('Manufacturer code "{}" does not exist.'.format(mf_option))

        # TODO Refactor this to eliminate hard-coded vendors.
        if manufacturer.code == "PA":
            slug = "printaura"
        elif manufacturer.code == "PF":
            slug = "printful"
        elif manufacturer.code == "GT":
            slug = "gooten"
        else:
            CommandError('Invalid vendor module specified.')

        # Now we're ready to load up the appropriate vendor module, and call the
        # Main interface, APIInterface().

        mod_name = "".join(["vendor_", slug, ".interface"])
        vMod = import_module(mod_name)
        importer = vMod.APIInterface(manufacturer)
        importer.do_import()
