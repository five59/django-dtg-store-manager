import sys
import io, json
import warnings
from collections import OrderedDict
from django.apps import apps
from django.core import serializers
from django.core import management
from django.db import DEFAULT_DB_ALIAS, router
from django.core.management.utils import parse_apps_and_model_labels
from django.core.management.commands import dumpdata
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = (
        "Does a full json backup of your data.",
        )

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        the_apps = ['master','printaura','printful','catalog',]

        for app in the_apps:
            self.stdout.write("--> Dumping {} app...".format(app), ending='')
            sysout = sys.stdout
            sys.stdout = open('/code/_backup/{}.json'.format(app),'w')
            result = management.call_command(dumpdata.Command(), app, indent=2, format='json')
            sys.stdout = sysout
            self.stdout.write( self.style.SUCCESS("OK"), ending='\n')

    def dobackup(self):
        pass
