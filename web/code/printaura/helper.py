import requests, json, io, sys
from django.conf import settings
from .models import *
import colorsys

def sync_api():
    call_listbrands()
    call_listcolors()
    call_listsizes()
    call_listshipping()
    call_listadditionalsettings()
    call_listproducts()

def call_listbrands():
    print("--> ListBrands")
    payload = {
        "key": settings.API_KEY,
        "hash": settings.API_HASH,
        "method": 'listbrands'
    }
    r = requests.post(settings.API_URL, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for d in data['results']:
            obj, created = Brand.objects.update_or_create(
                aura_id = d['brand_id'],
                defaults = {
                    'name': d['brand_name']
                }
            )
    else:
        r.raise_for_status()

def call_listsizes():
    print("--> ListSizes")
    payload = {
        "key": settings.API_KEY,
        "hash": settings.API_HASH,
        "method": 'listsizes'
    }
    r = requests.post(settings.API_URL, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for d in data['results']:
            obj, created = Size.objects.update_or_create(
                aura_id = d['size_id'],
                defaults = {
                    'name': d['size_name'],
                    'group': d['size_group'],
                    'plus_size_charge': d['plus_size_charge']
                }
            )
    else:
        r.raise_for_status()

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'
def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]
def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)

def call_listcolors():
    print("--> ListColors")

    payload = {
        "key": settings.API_KEY,
        "hash": settings.API_HASH,
        "method": 'listcolors'
    }
    r = requests.post(settings.API_URL, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for d in data['results']:
            c = rgb(d['color_code'])
            c = colorsys.rgb_to_hsv(c[0],c[1],c[2])
            obj, created = Color.objects.update_or_create(
                aura_id = d['color_id'],
                defaults = {
                    'name': d['color_name'],
                    'code': d['color_code'],
                    'group': d['color_group'],
                    'color_hue': c[0],
                    'color_brightness': c[2],
                }
            )
    else:
        r.raise_for_status()

def call_listshipping():
    print("--> ListShipping")
    payload = {
        "key": settings.API_KEY,
        "hash": settings.API_HASH,
        "method": 'listshipping'
    }
    r = requests.post(settings.API_URL, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for k,v in data['results'].items():
            for d in v:
                s_obj, created = ShippingOption.objects.update_or_create(
                    aura_id = d['shipping_id'],
                    defaults = {
                        'name': d['shipping_option_name'],
                    }
                )

                g_obj, created = ProductGroup.objects.update_or_create(
                    aura_id = d['shipping_group'],
                    defaults = {
                        'name': d['shipping_name'],
                    }
                )

                sz_obj, created = ShippingZone.objects.update_or_create(
                    name = d['shipping_zone'],
                    defaults = {
                    }
                )

                obj, created = Shipping.objects.update_or_create(
                    option = s_obj,
                    group = g_obj,
                    defaults = {
                        'company': d['shipping_company'],
                        'zone': sz_obj,
                        'first_item_price': d['first_item_price'],
                        'additional_item_price': d['additional_item_price'],
                        }
                    )
    else:
        r.raise_for_status()

def call_listadditionalsettings():
    print("--> ListAdditionalSettings")
    payload = {
        "key": settings.API_KEY,
        "hash": settings.API_HASH,
        "method": 'listadditionalsettings'
    }
    r = requests.post(settings.API_URL, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for k,v in data['results'].items():
            obj, created = AdditionalSettings.objects.update_or_create(
                name = k,
                defaults = {
                    'value': v
                }
            )
    else:
        r.raise_for_status()

def call_listproducts():
    print("--> ListProducts")
    payload = {
        "key": settings.API_KEY,
        "hash": settings.API_HASH,
        "method": 'listproducts'
    }
    r = requests.post(settings.API_URL, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for p in data['results']:
            b = Brand.objects.get(aura_id=p['brand_id'])
            s = ProductGroup.objects.get(aura_id=p['shipping_id'])
            if p['country'] != '':
                c, created = Country.objects.update_or_create(
                    name=p['country'],
                    defaults={}
                    )
            else:
                c = None
            prod, create = Product.objects.update_or_create(
                aura_id = p['product_id'],
                defaults = {
                    'name': p['product_name'],
                    'sku': p['sku'],
                    'brand': b,
                    'country': c,
                    'productgroup': s,
                    'price': p['price'],
                    'color_price': p['color_price'],
                    'inventory_description': p['inventory_description'],
                    'size_chart_image_url': p['size_chart_image_url'],
                    'material_name': p['material_name'],
                }
            )
            for coloritem in p['colors']:
                for sizeitem in coloritem:
                    try:
                        color = Color.objects.get(aura_id = coloritem)
                    except:
                        color = None
                        print('    ! Color {} not found for {}.'.format(coloritem, prod.name))
                    # try:
                    #     size = Size.objects.get(aura_id = sizeitem)
                    # except:
                    #     size = None
                    #     print('    ! Size {} not found for {}.'.format(sizeitem, prod.name))

                    obj, created = ProductVariant.objects.update_or_create(
                        product = prod,
                        color = color,
                        # size = size,
                        defaults = {}
                    )
    else:
        r.raise_for_status()
