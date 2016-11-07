import sys
import io, json
import warnings
from collections import OrderedDict
from django.apps import apps
from django.core import serializers
from django.core import management
from django.db import DEFAULT_DB_ALIAS, router
from django.core.management.utils import parse_apps_and_model_labels
from django.core.management.commands import loaddata
from django.core.management.base import BaseCommand, CommandError

# parse_apps_and_model_labels has been purged from the 1.10.3 release of Django.
# Not sure why, but in the meantime you have to add it back to the package.

class Command(BaseCommand):
    help = (
        "Does a full json restore of your data.",
        )

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        the_apps = ['catalog','printful','printaura','master',]
        for app in the_apps:
            self.stdout.write("--> Restoring {} app...".format(app), ending='')
            result = management.call_command(loaddata.Command(), '/code/_backup/{}.json'.format(app) )

    def dobackup(self):
        pass
