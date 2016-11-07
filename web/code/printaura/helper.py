import requests, json, io, sys
import colorsys
from master import models as mm

def sync_api():
    get_brands()
    get_colors()
    get_sizes()
    # call_listshipping()
    # call_listadditionalsettings()
    get_products()

def get_brands():
    print("--> ListBrands")

    podv = mm.PODVendor.objects.get(code='PA')

    payload = {
        "key": podv.api_key,
        "hash": podv.api_hash,
        "method": 'listbrands'
    }
    r = requests.post(podv.apibase_url, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for d in data['results']:
            obj, created = mm.VendorBrand.objects.update_or_create(
                name = d['brand_name'],
                vendor_key = d['brand_id'],
                vendor = podv,
                defaults = {}
            )
    else:
        r.raise_for_status()

def get_sizes():
    print("--> ListSizes")

    podv = mm.PODVendor.objects.get(code='PA')
    payload = {
        "key": podv.api_key,
        "hash": podv.api_hash,
        "method": 'listsizes'
    }
    r = requests.post(podv.apibase_url, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for d in data['results']:
            obj, created = mm.VendorSize.objects.update_or_create(
                vendor_code = d['size_id'],
                vendor = podv,
                defaults = {
                    'vendor_name': d['size_name'],
                    'vendor_grouping': d['size_group'],
                    # 'plus_size_charge': d['plus_size_charge'],
                }
            )
            if created:
                print("Created {}".format(obj.vendor_name))
            else:
                print("{} already exists.".format(obj.vendor_name))
    else:
        r.raise_for_status()

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'
def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]
def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)

def get_colors():
    print("--> ListColors")
    podv = mm.PODVendor.objects.get(code='PA')

    payload = {
        "key": podv.api_key,
        "hash": podv.api_hash,
        "method": 'listcolors'
    }
    r = requests.post(podv.apibase_url, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        vendor = mm.PODVendor.objects.get(code='PA')
        for d in data['results']:

            d['color_code'] = d['color_code'].upper()

            vc_obj, created = mm.VendorColor.objects.update_or_create(
                vendor = vendor,
                vendor_code = d['color_id'],
                defaults = {
                    'color_code': d['color_code'],
                    'color_group': d['color_group'],
                    'color_name': d['color_name'],
                }
            )

            # Try matching to hex code
            mc_obj = mm.Color.objects.filter(hex_code__contains=d['color_code'])
            if mc_obj.count() > 0:
                vc_obj.master_color = mc_obj[0]
                vc_obj.save()
                print("[COLOR] Matched!")
            else:
                print("[COLOR] Color not matched to master list. {}".format(vc_obj.color_code))

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

def get_products():
    print("--> GetProducts")
    podv = mm.PODVendor.objects.get(code='PA')

    payload = {
        "key": podv.api_key,
        "hash": podv.api_hash,
        "method": 'listproducts'
    }
    r = requests.post(podv.apibase_url, data=payload)
    if (r.ok):
        data = json.loads(str(r.content,'utf-8'))
        for p in data['results']:
            b = mm.VendorBrand.objects.get(vendor_key=p['brand_id'], vendor=podv)
            prod, created = mm.VendorProduct.objects.update_or_create(
                mpn = p['product_id'],
                defaults = {
                    vendor = podv,
                    'brand': b,
                    'sku': p['sku'],
                    'name': p['product_name'],
                    'description' : p['inventory_description'],
                    'material' : p['material_name'],
                    'country' : p['country'],
                }
            )
            if created:
                print("Created Product: {}".format(prod.name))
            else:
                print("Updated: {}".format(prod.name))

            for coloritem in p['colors']:
                price = "Unknown"
                print("VARIANTS")
                try:
                    print("color: {}".format(coloritem))
                    color = mm.VendorColor.objects.get(vendor_code = coloritem)
                    if color.color_group=='White':
                        price = p['price']
                    elif color.color_group=='Color':
                        price = p['color_price']
                except:
                    color = None
                    print('    ! Color {} not found for {}.'.format(coloritem, prod.name))

                for sizeitem in coloritem:
                    print("size: {}".format(sizeitem))
                    try:
                        size = mm.VendorSize.objects.get(vendor_code = sizeitem)
                    except:
                        size = None
                        print('    ! Size {} not found for {}.'.format(sizeitem, prod.name))

                    obj, created = mm.VendorVariant.objects.update_or_create(
                        podvendor = podv,
                        vendor_id = '',
                        vendor_product = prod,
                        defaults = {
                            'vendor_color': color,
                            'vendor_size': size,
                            'price': price,
                        }
                    )
    else:
        r.raise_for_status()
