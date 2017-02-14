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
from decimal import *
from django.db.models import Avg, Max, Min


class Utility:
    def __init__(self):
        print("--> Utility Init")

    def link_manufacturer_items(self):
        print(
            "-- NOTE: This tries to do a loose match using expected brand names and MPNs. It's not a replacement for manual matching... it should just help you speed up your matching.")
        for a in ca.ManufacturerItem.objects.all():
            try:
                code_test = a.name.split(" ")
                if len(code_test) > 0:
                    code_test = code_test[0]
                else:
                    code_test = ""
                pi = Item.objects.filter(
                    brand__name__contains=a.brand,
                    code__contains=code_test)
                a.item = pi[0]
                print("--> Updating {}".format(a))
                a.save()
            except:
                print("--> SKIPPING {} ================================".format(a))

    def link_manufacturer_colors(self):
        print(
            "-- NOTE: This tries to do a loose match using expected color names by Brand. It's not a replacement for manual matching. It should just help you speed up your matching.")
        for a in ca.ManufacturerVariant.objects.all():
            try:
                brand = ca.Brand.objects.get(name=a.product.brand)
                if a.color_code in ["#000000", "#000"]:
                    a.color_code = "#010101"
                color, created = ca.Color.objects.update_or_create(
                    name=a.color,
                    brand=brand,
                    defaults={
                        'color_string': a.color_code,
                    }
                )
                a.color_obj = color
                a.save()
                if created:
                    print("-- Created: {}".format(color.name))
                else:
                    print("-- Matched: {}".format(color.name))
            except Exception as e:
                print("-- Skipping: {} ====================".format(a))
                print(e)

    def generate_pricing_matrix(self, manufacturer_code, filename='/code/_data/finance.txt'):
        print("Generating pricing matrix file. It can be found in {}".format(filename))

        data = []
        i = ca.ManufacturerItem.objects.filter(manufacturer__code=manufacturer_code)
        for x in i:
            item = {}
            a = ca.ManufacturerVariant.objects.filter(product=x).aggregate(
                Min('base_price'),
                Max('base_price'),
                Min('shippingclass__us_item1'),
                Max('shippingclass__us_item1'),
            )
            if x.item and a['shippingclass__us_item1__max']:
                if x.item.default_retail:
                    item['a_brand'] = x.brand
                    item['a_code'] = x.item.code
                    item['a_name'] = x.item.name
                    item['a_vid'] = x.code
                    if x.item.category.get_ancestors():
                        item['a_category'] = "{} - {}".format(x.item.category.get_ancestors()[0], x.item.category)
                    else:
                        item['a_category'] = x.item.category.name

                    item['c_min'] = a['base_price__min']
                    item['c_max'] = a['base_price__max']
                    item['s_min'] = a['shippingclass__us_item1__min']
                    item['s_max'] = a['shippingclass__us_item1__max']
                    item['r'] = x.item.default_retail if x.item.default_retail else 0

                    # P = PROFIT
                    item['p_min'] = item['r'] - item['c_min']
                    item['p_max'] = item['r'] - item['c_max']
                    # M = MARKUP
                    item['m_min'] = item['p_min'] / item['c_min']
                    item['m_max'] = item['p_max'] / item['c_max']
                    # G = GROSS MARGIN
                    item['g_min'] = item['p_min'] / item['r'] if item['r'] else 0
                    item['g_max'] = item['p_max'] / item['r'] if item['r'] else 0

                    # 10% Coupon
                    item['c_edc'] = item['r'] * Decimal('0.1')
                    item['cp_min'] = item['p_min'] - item['c_edc']
                    item['cp_max'] = item['p_max'] - item['c_edc']
                    item['cm_min'] = item['cp_min'] / item['c_min']
                    item['cm_max'] = item['cp_max'] / item['c_max']
                    item['cg_min'] = item['cp_min'] / (item['r'] - item['c_edc']) if item['r'] else 0
                    item['cg_max'] = item['cp_max'] / (item['r'] - item['c_edc']) if item['r'] else 0

                    # Free Shipping
                    item['fp_min'] = item['p_min'] - Decimal(str(item['s_min']))
                    item['fp_max'] = item['p_max'] - Decimal(str(item['s_max']))
                    item['fm_min'] = item['fp_min'] / item['c_min']
                    item['fm_max'] = item['fp_max'] / item['c_max']
                    item['fg_min'] = item['fp_min'] / (item['r'] - item['s_min'])
                    item['fg_max'] = item['fp_max'] / (item['r'] - item['s_max'])

                    # $5 Shipping
                    item['vp_min'] = item['p_min'] - item['s_min'] + Decimal('5.0')
                    item['vp_max'] = item['p_max'] - item['s_max'] + Decimal('5.0')
                    item['vm_min'] = item['vp_min'] / item['c_min']
                    item['vm_max'] = item['vp_max'] / item['c_max']
                    item['vg_min'] = item['vp_min'] / (item['r'] - item['s_min'] + Decimal('5.0')) if item['r'] else 0
                    item['vg_max'] = item['vp_max'] / (item['r'] - item['s_max'] + Decimal('5.0')) if item['r'] else 0

                    data.append(item)
                else:
                    print("-- No Price: {}".format(x))
            else:
                print("-- No Item Link: {}".format(x))

        def to_percent(val):
            return "{:.0%}".format(val)

        def to_usd(val):
            return '${:,.2f}'.format(val)

        headers = [
            [  # Row 1
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                'Coupon', '', '', '', '', '', '',
                'Free Shipping', '', '', '', '', '',
                '$5 Shipping', '', '', '', '', '',
            ],
            [  # Row 2
                '', '', '', '', '', 'Cost', '', 'Shipping', '', '',
                'Profit', '', 'Markup', '', 'Margin', '', 'EDC',
                'Profit', '', 'Markup', '', 'Margin', '',
                'Profit', '', 'Markup', '', 'Margin', '',
                'Profit', '', 'Markup', '', 'Margin', '',
            ],
            [  # Row 3
                'Code', 'VID', 'Name', 'Brand', 'Category', 'Min', 'Max', 'Min', 'Max', 'Retail', 'Min', 'Max', 'Min',
                'Max', 'Min', 'Max', '', 'Min', 'Max', 'Min', 'Max', 'Min', 'Max', 'Min', 'Max', 'Min', 'Max', 'Min',
                'Max', 'Min', 'Max', 'Min', 'Max', 'Min', 'Max',
            ],
        ]

        with open(filename, mode='wt', encoding='utf-8') as f:
            for h in headers:
                f.write('\t'.join(h))
                f.write('\n')
            for d in data:
                a = [
                    str(d['a_code']),
                    str(d['a_vid']),
                    str(d['a_name']),
                    str(d['a_brand']),
                    str(d['a_category']),
                    to_usd(d['c_min']),
                    to_usd(d['c_max']),
                    to_usd(d['s_min']),
                    to_usd(d['s_max']),
                    to_usd(d['r']),
                    to_usd(d['p_min']),
                    to_usd(d['p_max']),
                    to_percent(d['m_min']),
                    to_percent(d['m_max']),
                    to_percent(d['g_min']),
                    to_percent(d['g_max']),

                    to_usd(d['c_edc']),
                    to_usd(d['cp_min']),
                    to_usd(d['cp_max']),
                    to_percent(d['cm_min']),
                    to_percent(d['cm_max']),
                    to_percent(d['cg_min']),
                    to_percent(d['cg_max']),

                    to_usd(d['fp_min']),
                    to_usd(d['fp_max']),
                    to_percent(d['fm_min']),
                    to_percent(d['fm_max']),
                    to_percent(d['fg_min']),
                    to_percent(d['fg_max']),

                    to_usd(d['vp_min']),
                    to_usd(d['vp_max']),
                    to_percent(d['vm_min']),
                    to_percent(d['vm_max']),
                    to_percent(d['vg_min']),
                    to_percent(d['vg_max']),
                ]
                f.write('\t'.join(a))
                f.write('\n')

        print("-- Wrote {} records to {}.".format(len(data), filename))