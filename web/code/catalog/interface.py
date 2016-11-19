from django.core.management.base import CommandError
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.translation import ugettext as _
from django_extensions.db import fields as extension_fields

from datetime import datetime
from decimal import Decimal
import json
import pytz
import requests
import urllib

from reportlab.lib import colors
from reportlab.lib.pagesizes import A3
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Image

from catalog import models as ca
from creative import models as cr
from outlet_woo import models as wc

from pprint import pprint


class Utility:

    def __init__(self):
        print("--> Utility Init")

    def link_manufacturer_items(self):
        print("--> NOTICE: This tries to do a loose match using expected brand names and MPNs. It's not a replacement for manual matching... it should just help you speed up your matching.")
        for a in ca.ManufacturerItem.objects.all():
            try:
                code_test = a.name.split(" ")
             if len(code_test) > 0:
                 code_test = code_test[0]
             else:
                 code_test = ""
             pi = Item.objects.filter(
                 brand__name__contains=a.brand,
                 code__contains=code_test
             )
             a.item = pi[0]
             print("--> Updating {}".format(a))
             a.save()
         except:
             print("--> SKIPPING {} ================================".format(a))
