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
        ignored_apps = ['admin', 'auth', 'sessions', 'contenttypes']

        for applabel, appitem in apps.all_models.items():
            if not applabel in ignored_apps:
                self.stdout.write("--> App: {}".format(applabel), ending='\n')
                for model in appitem:
                    self.stdout.write("    --> {}".format(model), ending='\n')
                    sysout = sys.stdout
                    sys.stdout = open('/code/_fixtures/{}.{}.json'.format(applabel, model), 'w')
                    result = management.call_command(dumpdata.Command(), "{}.{}".format(
                        applabel, model), indent=2, format='json')
                    sys.stdout = sysout

    def dobackup(self):
        pass
