from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from .models import *
import json
import requests
from urllib.parse import urlencode
from requests.auth import HTTPBasicAuth


class pfClient:
    pfStoreObj = None
    connection = None
    base_url = "https://api.printful.com/"
    auth = None
    last_response = None
    last_response_raw = None

    def __init__(self, code=None, store=None):
        # Initialize API library
        if code and not store:
            try:
                self.pfStoreObj = pfStore.objects.get(code=code)
            except pfStore.DoesNotExist:
                raise Exception("Provided code doesn't match any known store.")
        elif store and not code:
            self.pfStoreObj = store
        else:
            raise Exception(
                "Please provide either a 'code' or a 'store' (but not both), when initializing the Printful API client.")

        if self.pfStoreObj.has_api_auth():
            self.connection = requests.Session()
            self.connection.auth = HTTPBasicAuth(
                self.pfStoreObj.consumer_key, self.pfStoreObj.consumer_secret)
            self.connection.headers['User-Agent'] = "559 Labs Printful API Wrapper (For Python3)"
            self.connection.headers['Content-Type'] = 'application/json'
            print("API session established.")
        else:
            raise pfException("API Key not found for printful. Check the admin dashboard.")

    def item_count(self):
        # Returns total available item count from the last request if it supports
        # paging (e.g order list) or nil otherwise
        if(self.last_response and 'paging' in self.last_response):
            return self.last_response['paging']['total']
        else:
            None

    def get(self, path, params=None):
        # Perform a GET request to the API
        # path - Request path (e.g. 'orders' or 'orders/123')
        # params - Additional GET parameters as a dictionary
        return self.__request('GET', path, params)

    def delete(self, path, params=None):
        # Perform a DELETE request to the API
        # path - Request path (e.g. 'orders' or 'orders/123')
        # params - Additional GET parameters as a dictionary
        return self.__request('DELETE', path, params)

    def post(self, path, data=None, params=None):
        # Perform a POST request to the API
        # path - Request path (e.g. 'orders' or 'orders/123')
        # data - Request body data as a dictionary
        # params - Additional GET parameters as a dictionary
        return self.__request('POST', path, params, data)

    def put(self, path, data=None, params=None):
        # Perform a PUT request to the API
        # path - Request path (e.g. 'orders' or 'orders/123')
        # data - Request body data as a dictionary
        # params - Additional GET parameters as a dictionary
        return self.__request('PUT', path, params, data)

    def __request(self, method, path, params=None, data=None):
        # Internal generic request wrapper

        self.last_response = None
        self.last_response_raw = None

        # Allow full URIs in requests. If only providing the route/endpoint, then
        # pre-pend the base_url.
        if path.startswith('http'):
            url = path
        else:
            url = self.base_url + path

        if(params):
            url += "?" + urlencode(params)

        if data:
            body = json.dumps(data)
        else:
            body = None

        # Make the request
        try:
            request = self.connection.request(
                method,
                url,
                # auth=self.auth,
                data=body,
            )
            self.last_response_raw = request
        except Exception as e:
            raise wcException('API request failed: %s' % e)

        if (self.last_response_raw.status_code < 200 or self.last_response_raw.status_code >= 300):
            raise pfException('Invalid API response')

        # Now try to decode everything.
        try:
            data = json.loads(self.last_response_raw.content.decode('utf-8'))
            self.last_response = data
        except ValueError as e:
            raise pfException('API response was not valid JSON.')

        return data['result']

    def update_geos(self):
        # No paging on this call.
        for c in self.get("countries"):
            cObj, cCreated = pfCountry.objects.update_or_create(
                code=c['code'],
                defaults={'name': c['name']}
            )
            print("{} {} ({})".format(
                "Created" if cCreated else "Updated",
                cObj.name, cObj.code,
            ))
            if c['states']:
                for s in c['states']:
                    sObj, sCreated = pfState.objects.update_or_create(
                        code=s['code'],
                        defaults={
                            'name': s['name'],
                            'pfcountry': cObj,
                        }
                    )
                    print("{} {} ({})".format(
                        "-- Created" if sCreated else "Updated",
                        sObj.name, sObj.code,
                    ))

    def _default_value(self, value, default_value):
        if value:
            return value
        return default_value

    def update_printfiles(self):
        limit = 100
        params = {'offset': 0, 'limit': limit, }
        files = self.get('files', params=params)
        if self.item_count() > 100:
            for page in range(1, int(self.item_count() / limit) + 1):
                params['offset'] = limit * page
                files = files + self.get('files', params=params)

        for f in files:
            fileObj, created = pfPrintFile.objects.update_or_create(
                pfstore=self.pfStoreObj,
                pid=f['id'],
                defaults={
                    'type': f['type'],
                    'hash': f['hash'],
                    'url': f['url'],
                    'filename': f['filename'],
                    'mime_type': f['mime_type'],
                    'size': self._default_value(f['size'], 0),
                    'width': self._default_value(f['width'], 0),
                    'height': self._default_value(f['height'], 0),
                    'dpi': self._default_value(f['dpi'], 0),
                    'status': self._default_value(f['status'], ""),
                    'created': self._default_value(f['created'], ""),
                    'thumbnail_url': self._default_value(f['thumbnail_url'], ""),
                    'preview_url': self._default_value(f['preview_url'], ""),
                    'visible': f['visible'],
                }
            )
            print("{} {}: {}".format(
                "Created" if created else "Updated",
                fileObj.pid,
                fileObj.filename,
            ))

        # Generic Printful exception

    def update_catalogproducts(self):
        products = self.get('products')
        # If API call was successful, then let's invalidate all local products
        pfCatalogProduct.objects.all().update(is_active=False)

        for p in products:
            productObj, created = pfCatalogProduct.objects.update_or_create(
                pid=p['id'],
                defaults={
                    'type': p['type'],
                    'brand': p['brand'],
                    'model': p['model'],
                    'image': p['image'],
                    'variant_count': p['variant_count'],
                    'is_active': True,
                },
            )
            print("{} {}: {}".format(
                "Created" if created else "Updated",
                productObj.brand,
                productObj.model,
            ))
            # Update CatalogVariants
            variants = self.get('products/{}'.format(productObj.pid))['variants']
            for v in variants:
                pfcolor, created = pfCatalogColor.objects.update_or_create(
                    label=v['color'],
                    defaults={
                        'hex_code': v['color_code'],
                    }
                )
                pfsize, created = pfCatalogSize.objects.update_or_create(
                    label=v['size'],
                    defaults={}
                )
                variantObj, created = pfCatalogVariant.objects.update_or_create(
                    pid=v['id'],
                    pfcatalogproduct=productObj,
                    defaults={
                        'name': v['name'],
                        'pfsize': pfsize,
                        'pfcolor': pfcolor,
                        'image': v['image'],
                        'price': v['price'],
                        'in_stock': v['in_stock'],
                        'is_active': True,
                    }
                )
                for x in p['files']:
                    fileObj, created = pfCatalogFileType.objects.update_or_create(
                        pid=x['id'],
                        pfcatalogvariant=variantObj,
                        defaults={
                            'title': x['title'],
                            'additional_price': x['additional_price'],
                        }
                    )
                for x in p['options']:
                    optionObj, created = pfCatalogOptionType.objects.update_or_create(
                        pid=x['id'],
                        pfcatalogvariant=variantObj,
                        defaults={
                            'title': x['title'],
                            'type': x['type'],
                            'additional_price': x['additional_price'],
                        }
                    )
                print("-- {}: {}".format(
                    "Created" if created else "Updated",
                    variantObj.name,
                ))

    def update_syncproducts(self):
        limit = 100
        params = {'offset': 0, 'limit': limit, }
        data = self.get('sync/products', params=params)
        if self.item_count() > 100:
            for page in range(1, int(self.item_count() / limit) + 1):
                params['offset'] = limit * page
                data = data + self.get('sync/products', params=params)
        for d in data:
            sProductObj, created = pfSyncProduct.objects.update_or_create(
                pid=d['id'],
                pfstore=self.pfStoreObj,
                defaults={
                    'external_id': d['external_id'],
                    'name': d['name'],
                    'variants': d['variants'],
                    'synced': d['synced'],
                }
            )
            print("{} {}: {}".format(
                "Created" if created else "Updated",
                sProductObj.pid,
                sProductObj.name,
            ))
            data_sub = self.get('sync/products/{}'.format(sProductObj.pid))
            for v in data_sub['sync_variants']:
                try:
                    cvariant = pfCatalogVariant.objects.get(pid=v['variant_id'])
                except pfCatalogVariant.DoesNotExist:
                    cvariant = None
                    print(
                        "-- {} / Couldn't find Catalog Variant #{}.".format(
                            sProductObj, v['variant_id']))

                obj, created = pfSyncVariant.objects.update_or_create(
                    pfsyncproduct=sProductObj,
                    pid=v['id'],
                    defaults={
                        'external_id': v['external_id'],
                        'name': v['name'],
                        'synced': v['synced'],
                        'pfcatalogvariant': cvariant,
                    }
                )
                # Link Options
                for linkoption in v['options']:
                    syncvariant = obj,
                    pid = linkoption['id'],
                    defaults = {
                        'value': linkoption['value'],
                    }
                # Link files
                obj.files.clear()  # Remove all links before adding again.
                for linkfile in v['files']:
                    try:
                        printfile = pfPrintFile.objects.get(pid=linkfile['id'])
                        obj.files.add(printfile)
                    except pfPrintFile.DoesNotExist as e:
                        raise pfException("PrintFile {} not found: {}".format(linkfile['id'], e))


class pfException(Exception):
    # Printful exception returned from the API
    pass


class pfAPIException(pfException):

    def __init__(self, message, code):
        Exception.__init__(self, message)
        self.code = code
        self.message = message

    def __str__(self):
        return '%i - %s' % (self.code, self.message)
