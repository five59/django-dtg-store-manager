from django.db import models
from catalog import models as ca
from django.core.management.base import CommandError
import requests
from decimal import Decimal
import json
from woocommerce import API
from outlet_woo import models as wc


class APIInterface:

    shopObj = None

    def __init__(self, sObj):
        self.shopObj = sObj

    def do_import(self):

        if not self.shopObj.has_key:
            CommandError("There doesn't seem to be a key set for {}.".format(self.shopObj.name))

        if not self.shopObj.has_secret:
            CommandError(
                "There doesn't seem to be a 'consumer secret key' set for {}.".format(self.shopObj.name))

        apiData = API(
            url=self.shopObj.web_url,
            consumer_key=self.shopObj.consumer_key,
            consumer_secret=self.shopObj.consumer_secret,
            wp_api=True,
            version="wc/v1",
        )

        print("--> Starting Import Process")
        response = apiData.get("products")
        if not response.ok:
            CommandError("The API returned an error code.")
        shopProducts = json.loads(response.content.decode('utf-8'))

        self.shopObj.num_products = len(shopProducts)
        self.shopObj.save()
        print("--> Found {} product(s).".format(self.shopObj.num_products))

        # If that was successful, then let's invalidate all local data, by
        # swapping the is_active flag to negative.
        for p in wc.Product.objects.filter(shop=self.shopObj):
            p.is_active = False
            p.save()

        for p in shopProducts:
            sp, spCreated = wc.Product.objects.update_or_create(
                code=p['id'],
                shop=self.shopObj,
                defaults={
                    'is_active': True,
                    'name': p['name'],
                    'slug': p['slug'],
                    'permalink': p['permalink'],
                    # 'date_created': p['date_created'],
                    # 'date_modified': p['date_modified'],
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
                }
            )
            if spCreated:
                print("Item Added: {} / {}".format(sp.code, sp.name))
            else:
                print("Item Updated: {} / {}".format(sp.code, sp.name))
