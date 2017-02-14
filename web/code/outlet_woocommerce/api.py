from django.db import models
from django.core.management.base import CommandError
from decimal import Decimal
from .models import *
import json
import requests
import base64
from outlet_woocommerce.models.wooStore import wooStore


class wcClient:
    wooStoreObj = None
    connection = None
    base_url = None

    last_response = None
    last_response_raw = None

    per_page = 10
    last_page = 1
    offset = 0

    total_items, total_pages = 0, 0
    link_next, link_prev, link_first, link_last = None, None, None, None

    def __init__(self, code=None, store=None):
        if code and not store:
            try:
                self.wooStoreObj = wooStore.objects.get(code=code)
            except wooStore.DoesNotExist:
                raise Exception("Provided code doesn't match any known store.")
        elif store and not code:
            self.wooStoreObj = store
        else:
            raise Exception(
                "Please provide either a 'code' or a 'store' (but not both), when initializing the Woocommerce client.")
        if self.wooStoreObj.consumer_key and self.wooStoreObj.consumer_secret and self.wooStoreObj.base_url:
            self.connection = requests.Session()
            self.connection.verify = self.wooStoreObj.verify_ssl
            self.connection.auth = (self.wooStoreObj.consumer_key, self.wooStoreObj.consumer_secret)
            self.connection.headers['User-Agent'] = '559 Labs WooCommerce API Wrapper'
            self.connection.headers['Content-Type'] = 'application/json'
            self.base_url = "{}/wp-json/".format(self.wooStoreObj.base_url)
            print("API session established.")
        else:
            raise wcException("API Key and Secret are both required. Check the admin dashboard.")

    # Perform a GET request to the API
    # path - Request path (e.g. 'orders' or 'orders/123')
    # params - Additional GET parameters as a dictionary
    def get(self, path, params=None):
        return self.__request('GET', path, params)

    # Perform a DELETE request to the API
    # path - Request path (e.g. 'orders' or 'orders/123')
    # params - Additional GET parameters as a dictionary
    def delete(self, path, params=None):
        return self.__request('DELETE', path, params)

    # Perform a POST request to the API
    # path - Request path (e.g. 'orders' or 'orders/123')
    # data - Request body data as a dictionary
    # params - Additional GET parameters as a dictionary
    def post(self, path, data=None, params=None):
        return self.__request('POST', path, params, data)

    # Perform a PUT request to the API
    # path - Request path (e.g. 'orders' or 'orders/123')
    # data - Request body data as a dictionary
    # params - Additional GET parameters as a dictionary
    def put(self, path, data=None, params=None):
        return self.__request('PUT', path, params, data)

    # Internal generic request wrapper
    def __request(self, method, path, params=None, data=None):

        self.last_response = None
        self.last_response_raw = None

        if path.startswith('http'):
            url = path
        else:
            url = self.base_url + path
        if(params):
            params['per_page'] = self.per_page if not params['per_page'] else params['per_page']
            params['page'] = self.page if not params['page'] else params['page']
            params['offset'] = self.offset if not params['offset'] else params['offset']
            url += '?' + urllib.parse.urlencode(params)

        if data:
            # convert object to string
            body = json.dumps(data)
        else:
            body = None

        # Make the request
        try:
            request = self.connection.request(
                method,
                url,
                data=body,
            )
            self.last_response_raw = request
        except Exception as e:
            raise wcException('API request failed: %s' % e)

        if(request.status_code < 200 or request.status_code >= 300):
            raise wcAPIException(request.reason, request.status_code)

        # Try to decode the response
        try:
            data = json.loads(self.last_response_raw.content.decode("utf-8"))
            self.last_response = data

            if "X-WP-Total" in self.last_response_raw.headers:
                self.total_items = self.last_response_raw.headers['X-WP-Total']
            else:
                self.total_items = 0

            if "X-WP-TotalPages" in self.last_response_raw.headers:
                self.total_pages = self.last_response_raw.headers['X-WP-TotalPages']
            else:
                self.total_items = 1

            if "next" in self.last_response_raw.links:
                self.link_next = self.last_response_raw.links['next']['url']
            else:
                self.link_next = None

            if "prev" in self.last_response_raw.links:
                self.link_prev = self.last_response_raw.links['prev']['url']
            else:
                self.link_prev = None

            if "first" in self.last_response_raw.links:
                self.link_first = self.last_response_raw.links['first']['url']
            else:
                self.link_first = None

            if "last" in self.last_response_raw.links:
                self.link_last = self.last_response_raw.links['last']['url']
            else:
                self.link_last = None

        except ValueError as e:
            raise wcException("API response was not valid JSON", e)

        return data

    def update_products(self):
        print("- Updating Products")
        res = self.get('products')
        print("-- There are {} products. I will retrieve {} per page, so that means {} requests.".format(
            self.total_items,
            self.per_page,
            int(int(self.total_items) / int(self.per_page)) + 1,
        ))
        Product.objects.filter(store=self.wooStoreObj).update(is_active=False)

        while self.link_next:
            print("[WHILE CLAUSE : TRUE SUITE CALLED]")
            for p in res:
                Product.ingest_json(p, self.wooStoreObj)
            print("- Retrieving page {} from the API.".format(self.last_page + 1))
            if self.link_next:
                res = self.get(self.link_next)
        else:
            print("[WHILE CLAUSE : ELSE SUITE CALLED]")
            for p in res:
                Product.ingest_json(p, self.wooStoreObj)


class wcException(Exception):
    pass


class wcAPIException(wcException):

    def __init__(self, message, code):
        Exception.__init__(self, message)
        self.code = code
        self.message = message

    def __str__(self):
        return "{} - {}".format(self.code, self.message)
