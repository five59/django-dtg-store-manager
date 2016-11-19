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
# from django.core.management.utils import parse_apps_and_model_labels
from django.core.management.commands import dumpdata
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = (
        "Does a full json backup of your data.",
    )

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ignored_apps = ['admin', 'sessions', 'contenttypes']

        for applabel, appitem in apps.all_models.items():
            if not applabel in ignored_apps:
                for model in appitem:
                    self.stdout.write(
                        "--> Exporting data from {}.{}...".format(applabel, model), ending='')
                    sysout = sys.stdout
                    sys.stdout = open('/code/_fixtures/{}.{}.json'.format(applabel, model), 'w')
                    result = management.call_command(dumpdata.Command(), "{}.{}".format(
                        applabel, model), indent=2, format='json')
                    sys.stdout = sysout
                    self.stdout.write("OK!", ending='\n')

    def dobackup(self):
        pass
