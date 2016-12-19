from django.core.management.base import CommandError
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.translation import ugettext as _
from django_extensions.db import fields as extension_fields
from django.core.paginator import Paginator
import html

from datetime import datetime
from decimal import Decimal
import json
import pytz
import requests
import urllib

from woocommerce import API

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

    def update_all_local_product_data():
        for shop in wc.Shop.objects.all():
            print("===== UPDATING {} =====".format(shop.name))
            api = APIInterface(shop)
            api.do_import()


def APIShortcut(shop_code):
    shopObj = wc.Shop.objects.get(code=shop_code)

    if not shopObj.has_key:
        CommandError("There doesn't seem to be a key set for {}.".format(shopObj.name))

    if not shopObj.has_secret:
        CommandError(
            "There doesn't seem to be a 'consumer secret key' set for {}.".format(shopObj.name))
    return API(
        url=shopObj.web_url,
        consumer_key=shopObj.consumer_key,
        consumer_secret=shopObj.consumer_secret,
        wp_api=True,
        version="wc/v1",
        timeout=20,
    )


class APIInterface:

    shopObj = None
    apiData = None

    def __init__(self, sObj):
        self.max_per_page = 50  # Max is 100
        self.shopObj = sObj
        self.apiData = self.getAPI()

    def getAPI(self):
        if not self.shopObj.has_key:
            CommandError("There doesn't seem to be a key set for {}.".format(self.shopObj.name))

        if not self.shopObj.has_secret:
            CommandError(
                "There doesn't seem to be a 'consumer secret key' set for {}.".format(self.shopObj.name))

        return API(
            url=self.shopObj.web_url,
            consumer_key=self.shopObj.consumer_key,
            consumer_secret=self.shopObj.consumer_secret,
            wp_api=True,
            version="wc/v1",
            timeout=20,
        )

    def do_import(self, only_private=False):

        print("--> Making dummy request to extract headers...")
        requestString = "products?per_page={}".format(self.max_per_page)
        if only_private:
            requestString = "".join([requestString, "&status=private"])
        response = self.apiData.get(requestString)
        if not response.ok:
            error = json.loads(response.content.decode('utf-8'))
            print("--> Error:")
            print(error)
            # print("    Code: {}".format(error.code))
            # print(" Message: {}".format(error.message))
            # print("    Data: {}".format(error.data))
            CommandError("The API returned an error code.")

        # print(response.headers)

        if response.headers['X-WP-TotalPages']:
            api_total_pages = int(response.headers['X-WP-TotalPages'])
        else:
            api_total_pages = 1

        if response.headers['X-WP-Total']:
            api_total_products = int(response.headers['X-WP-Total'])
        else:
            api_total_products = 0

        self.shopObj.num_products = api_total_products
        self.shopObj.save()

        # If that was successful, then let's invalidate all local data, by
        # swapping the is_active flag to negative.
        if not only_private:
            for p in wc.Product.objects.filter(shop=self.shopObj):
                p.is_active = False
                p.save()

        print("--> There are {} products across {} API pages.".format(api_total_products, api_total_pages))

        for page in range(1, api_total_pages + 1):
            print("\n\n--> Requesting Page {}...\n".format(page))
            response = self.apiData.get(
                "products?per_page={}&page={}".format(self.max_per_page, page))
            if not response.ok:
                error = json.loads(response.content.decode('utf-8'))
                print("--> Error:")
                print("    Code: {}".format(error.code))
                print(" Message: {}".format(error.message))
                print("    Data: {}".format(error.data))
                CommandError("The API returned an error code.")

            for p in json.loads(response.content.decode('utf-8')):

                # TODO Clean up the inbound data.
                # date_created = parse_datetime(p['date_created'])
                # pytz.timezone(self.shopObj.timezone).localize(datetime_created)
                # date_modified = parse_datetime(p['date_modified'])
                # pytz.timezone(self.shopObj.timezone).localize(datetime_modified)
                # date_on_sale_from = parse_datetrime(p['date_on_sale_from']

                sp, spCreated = wc.Product.objects.update_or_create(
                    code=p['id'],
                    shop=self.shopObj,
                    defaults={
                        'is_active': True,
                        'name': p['name'],
                        'slug': p['slug'],
                        'permalink': p['permalink'],
                        # 'date_created': date_created,
                        # 'date_modified': date_modified,
                        'product_type': p['type'],
                        'status': p['status'],
                        'featured': p['featured'],
                        'catalog_visibility': p['catalog_visibility'],
                        'description': p['description'],
                        'short_description': p['short_description'],
                        'sku': p['sku'],
                        'price': p['price'],
                        'regular_price': p['regular_price'],
                        'sale_price': p['sale_price'],
                        # 'date_on_sale_from': p['date_on_sale_from'],
                        # 'date_on_sale_to': p['date_on_sale_to'],
                        'price_html': p['price_html'],
                        'on_sale': p['on_sale'],
                        'attributes_string': json.dumps(p['attributes']),
                    }
                )

                # TODO Remove all old images.
                imStats = {'total': 0, 'added': 0}
                for i in p['images']:
                    # TODO Clean up image data
                    # date_created = parse_datetime(i['date_created'])
                    # pytz.timezone(self.shopObj.timezone).localize(datetime_created)
                    # date_modified = parse_datetime(i['date_modified'])
                    # pytz.timezone(self.shopObj.timezone).localize(datetime_modified)
                    im, imCreated = wc.ProductImage.objects.update_or_create(
                        code=i['id'],
                        product=sp,
                        defaults={
                            'name': i['name'],
                            'src': i['src'],
                            'alt': i['alt'],
                            'position': i['position'],
                            # 'date_created': date_created,
                            # 'date_modified': date_modified,
                        }
                    )
                    imStats['total'] += 1
                    if imCreated:
                        imStats['added'] += 1

                pmStats = {'total': 0, 'added': 0}
                for i in p['variations']:
                    # FIXME. Short term fix for attributes. Using local COLOR and SIZE.
                    att_color = next((x for x in i['attributes'] if x[
                                     'name'] == 'color'), None)
                    att_size = next((x for x in i['attributes'] if x[
                                    'name'] == 'size'), None)
                    att_color = att_color['option'] if att_color else None
                    att_size = att_size['option'] if att_size else None

                    if i['image']:
                        image_url = i['image'][0]['src']
                    else:
                        image_url = ""

                    if att_color:
                        try:
                            att_color_obj = ca.Color.objects.get(name=att_color)
                        except Exception as e:
                            att_color_obj = None
                            print('--> Color "{}" object not matched.'.format(att_color), e)

                    if att_size:
                        try:
                            att_size_obj = ca.Size.objects.get(name=att_size)
                        except Exception as e:
                            att_size_obj = None
                            print('--> Size "{}" object not matched.'.format(att_size), e)

                    pm, pmCreated = wc.ProductVariation.objects.update_or_create(
                        code=i['id'],
                        product=sp,
                        defaults={
                            'permalink': p['permalink'],
                            'sku': p['sku'],
                            'price': p['price'],
                            "regular_price": p['regular_price'],
                            "sale_price": p['sale_price'],
                            "on_sale": p['on_sale'],
                            "purchasable": p['purchasable'],
                            "virtual": p['virtual'],
                            "downloadable": p['downloadable'],
                            "download_limit": p['download_limit'],
                            "download_expiry": p['download_expiry'],
                            "tax_status": p['tax_status'],
                            "manage_stock": p['manage_stock'],
                            # "stock_quantity": p['stock_quantity'],
                            "in_stock": p['in_stock'],
                            "backorders": p['backorders'],
                            "backorders_allowed": p['backorders_allowed'],
                            "backordered": p['backordered'],
                            # "weight": p['weight'],
                            'att_color': att_color,
                            'att_size': att_size,
                            'image_url': image_url,
                        }
                    )
                    pmStats['total'] += 1
                    if pmCreated:
                        pmStats['added'] += 1

                if spCreated:
                    action = "Added"
                else:
                    action = "Updated"

                stats = "--> {} / {} {}\t\tImages: {} Total, {} New\t\tVariants: {} Total, {} New".format(

                    sp.code,
                    sp.name,

                    action,

                    imStats['total'],
                    imStats['added'],

                    pmStats['total'],
                    pmStats['added'],

                )
                print(stats)

    def get_attributes(self):
        response = self.apiData.get('products/attributes')
        if not response.ok:
            error = json.loads(response.content.decode('utf-8'))
            print("Error: {}".format(error))
        data = json.loads(response.content.decode('utf-8'))
        for i in data:
            pa, created = wc.ProductAttribute.objects.update_or_create(
                code=i['id'],
                shop=self.shopObj,
                defaults={
                    'name': html.unescape(i['name']),
                    'slug': i['slug'],
                    'has_archives': i['has_archives'],
                    'input_type': i['type'],
                    'order_by': i['order_by'],
                }
            )
            response = self.apiData.get('products/attributes/{}/terms'.format(pa.code))
            if not response.ok:
                error = json.loads(response.content.decode('utf-8'))
                print("Error: {}".format(error))

            termdata = json.loads(response.content.decode('utf-8'))
            for t in termdata:
                pat, patCreated = wc.ProductAttributeTerm.objects.update_or_create(
                    code=t['id'],
                    productattribute=pa,
                    defaults={
                        'name': html.unescape(t['name']),
                        'slug': t['slug'],
                        'description': t['description'],
                        'menu_order': t['menu_order'],
                        'count': t['count'],
                    }
                )
            if created:
                print("-- Added New Attribute: {}".format(pa.name))
            else:
                print("-- Updated: {}".format(pa.name))
            print("   With {} terms.".format(len(termdata)))

    def generate_attribute_terms(self):
        print("-- Google Merchant Category")
        obj = wc.Product.objects.filter(
            shop=self.shopObj).order_by().values(
            "item__googlecategory__long_name").distinct()
        pa = wc.ProductAttribute.objects.get(name="Google Merchant Category", shop=self.shopObj)
        for i in obj:
            term, created = wc.ProductAttributeTerm.objects.update_or_create(
                name=i['item__googlecategory__long_name'],
                productattribute=pa,
                defaults={}
            )

        print("-- Design")
        obj = wc.Product.objects.filter(
            shop=self.shopObj).order_by().values(
            "design__name").distinct()
        pa = wc.ProductAttribute.objects.get(name="Design", shop=self.shopObj)
        for i in obj:
            term, created = wc.ProductAttributeTerm.objects.update_or_create(
                name=i['design__name'],
                productattribute=pa,
                defaults={}
            )

        print("-- Series & Brand")
        obj = wc.Product.objects.filter(
            shop=self.shopObj).order_by().values(
            "design__series__name").distinct()
        pa = wc.ProductAttribute.objects.get(name="Series", shop=self.shopObj)
        ba = wc.ProductAttribute.objects.get(name="Brand", shop=self.shopObj)
        for i in obj:
            term, created = wc.ProductAttributeTerm.objects.update_or_create(
                name=i['design__series__name'],
                productattribute=pa,
                defaults={},
            )
            term, created = wc.ProductAttributeTerm.objects.update_or_create(
                name=" / ".join([
                    self.shopObj.name,
                    i['design__series__name'],
                ]),
                productattribute=ba,
                defaults={},
            )

        print("-- Age Group")
        pa = wc.ProductAttribute.objects.get(name="Age Group", shop=self.shopObj)
        for k, v in ca.Item.AGEGROUP_CHOICES:
            term, created = wc.ProductAttributeTerm.objects.update_or_create(
                name=v,
                productattribute=pa,
                defaults={},
            )

        print("-- Gender")
        pa = wc.ProductAttribute.objects.get(name="Gender", shop=self.shopObj)
        for k, v in ca.Item.GENDER_CHOICES:
            term, created = wc.ProductAttributeTerm.objects.update_or_create(
                name=v,
                productattribute=pa,
                defaults={},
            )

    def put_attributes(self):
        # TODO Add delete functionality
        for attribute in wc.ProductAttribute.objects.filter(shop=self.shopObj):
            data = {
                "create": [],
                "update": [],
                # "delete": [],
            }
            for t in wc.ProductAttributeTerm.objects.filter(productattribute=attribute):
                if t.code:
                    data['update'].append({
                        'id': t.code, 'name': html.escape(t.name),
                    })
                else:
                    data['create'].append({'name': html.escape(t.name)})
            response = self.apiData.post(
                'products/attributes/{}/terms/batch'.format(attribute.code), data)
            if not response.ok:
                error = json.loads(response.content.decode('utf-8'))
                print("-- Error on attribute {}:".format(attribute.name))
                print("\t{}: {}".format(error['code'], error['message']))
            print("-- Updated {} with {} additions and {} updates.".format(
                attribute.name,
                len(data['create']),
                len(data['update']),
            ))

        # attributes = json.loads(response.content.decode('utf-8'))
        #
        # for k, v in new_attributes.items():      # Loop through the local items
        #     for i in attributes:                # Loop through the remote data
        #         if i['name'] in k:              # If the remote Attribute is one that we care about
        #             v['id'] = i['id']
        #             response = self.apiData.get('products/attributes/{}/terms')
        #             if response.ok:
        #                 v['response'] = json.loads(response.content.decode('utf-8'))
        #             else:
        #                 print("--> ERROR occurred while trying to retrieve terms for {}".format(k))
        #

    def push_data(self, only_private=False):
        items_per_page = 5
        if only_private:
            print("-- Requested Private Product Update Only --")
            objs = wc.Product.objects.filter(shop=self.shopObj, status=wc.Product.STATUS_PRIVATE)
        else:
            objs = wc.Product.objects.filter(shop=self.shopObj)

        pages = Paginator(objs, items_per_page)
        print("\nThere are {} items to update, and I'll do this in {} requests.\n".format(
            pages.count, pages.num_pages))

        for pg in pages.page_range:
            console = []
            page = pages.page(pg)
            products = []
            for p in page:
                data = {
                    "id": p.code,
                    "sku": p.sku,
                    "name": p.name,
                    "attributes": p.get_attributes(),
                    "regular_price": p.regular_price,
                    "description": p.description,
                }
                # print("-- Description Length: {}".format(len(p.description)))
                variants = wc.ProductVariation.objects.filter(product=p)
                if variants:
                    print("Variant Product: {} ({}) with {} variants.".format(
                        p.sku, p.name, variants.count()))
                    data['variations'] = []
                    for v in variants:
                        if p.regular_price:
                            new_price = p.regular_price
                        else:
                            new_price = p.price
                        data['variations'].append({
                            "id": v.code,
                            "sku": v.sku,
                            "name": p.name,
                            "regular_price": new_price,
                        })
                else:
                    print("Standard Product: {} ({}).".format(p.sku, p.name))
                products.append(data)
            data = {"update": products}

            print("\nPushing {} products (page {} of {})...".format(
                self.shopObj.name,
                pg,
                pages.num_pages,
            ))
            response = self.apiData.post("products/batch", data)

            if not response.ok:
                error = json.loads(response.content.decode('utf-8'))
                print("Error:")
                print("-- Code: {}".format(error['code']))
                print("-- Message: {}".format(error['message']))
                print("-- Data: {}".format(error['data']))
                CommandError("The API returned an error code.")
            else:
                print("Success!\n")


class Catalog:

    def __init__(self):
        print("--> Catalog Instantiated")

    def generate_pdf(self):

        width, height = A3
        p = canvas.Canvas("catalog.pdf", pagesize=A3)
        p.setTitle(_("Product Catalog"))
        # p.setAuthor()

        pageContent = {
            'name': {
                'text': "",
                'x': 36,
                'y': 1118,
                'font': "Helvetica",
                'fontsize': 28,
                'fontcolor': colors.Color(0, 0, 0, alpha=1),
            },
            'sku': {
                'text': "",
                'x': 600,
                'y': 1052,
                'font': "Helvetica-Bold",
                'fontsize': 18,
                'fontcolor': colors.Color(0, 0, 0, alpha=1),
            },
            'outlet': {
                'text': '',
                'x': 600,
                'y': 1030,
                'font': "Helvetica",
                'fontsize': 18,
                'fontcolor': colors.Color(0.5, 0.5, 0.5, alpha=1),
            },
            'price': {
                'text': "",
                'x': 600,
                'y': 1008,
                'font': "Helvetica",
                'fontsize': 18,
                'fontcolor': colors.Color(1, 0.5, 0.5, alpha=1),
            },
            'sizes': {
                'text': "",
                'x': 600,
                'y': 0,
                'font': "Helvetica",
                'fontsize': 18,
                'fontcolor': colors.Color(0, 0, 0, alpha=1),
            },
            'colors': {
                'text': "",
                'x': 600,
                'y': 0,
                'font': "Helvetica",
                'fontsize': 18,
                'fontcolor': colors.Color(0, 0, 0, alpha=1),
            },
            'footer': {
                'text': "",
                'x': 36,
                'y': 36,
                'font': "Helvetica",
                'fontsize': 10,
                'fontcolor': colors.Color(0.4, 0.4, 0.4, alpha=1),
            },
        }
        img_grid_scale = 141
        img_grid_row_start = 400
        img_grid_gutter = 16
        img_grid_num_per_row = 5
        page_number = 0

        for product in wc.Product.objects.all().order_by('shop', 'sku',):
            page_number += 1
            pageContent['sku']['text'] = str(product.sku)
            pageContent['name']['text'] = str(product.name.upper())
            pageContent['price']['text'] = str("$ {}".format(product.price))
            pageContent['outlet']['text'] = str(product.shop)
            pageContent['footer']['text'] = str(
                "Page {} / Generated {}".format(page_number, datetime.now()))

            images = wc.ProductImage.objects.filter(product=product)
            if len(images) > 0:
                p.drawImage(images[0].image.path, 36, 542, width=546, height=546)
            if len(images) > 1:
                item = 0
                for img in images[1:]:  # Ignore the first, since we've displayed it.
                    if not img.image:
                        img.download_image()
                        print("--> Downloading product image.")
                    col = item % img_grid_num_per_row
                    row = int(item / img_grid_num_per_row)
                    item += 1
                    # Calulate the x/y. Remember, origin is in the BOTTOM LEFT, so 'y' should
                    # move in a negative direction.
                    x = 36 + col * (img_grid_scale + img_grid_gutter)
                    y = img_grid_row_start - row * (img_grid_scale - img_grid_gutter)
                    p.drawImage(img.image.path, x, y, width=img_grid_scale,
                                height=img_grid_scale)

            for k, v in pageContent.items():
                p.setFont(v['font'], v['fontsize'])
                p.setFillColor(v['fontcolor'])
                p.setStrokeColor(v['fontcolor'])
                p.drawString(v['x'], v['y'], str(v['text']))

            # TODO Now display sizes and colors (needs to be implemented in the models)

            p.showPage()  # Ends this page and moves to the next.

        print("--> Save")
        p.save()  # Saves the document.
