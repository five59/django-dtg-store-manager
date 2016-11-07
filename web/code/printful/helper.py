from printful.models import *
from decimal import Decimal
import printful.wrapper as printfulwrapper
from master import models as mm

PRINTFUL_APIKEY = b'2fvon1ny-nmjw-vy0i:wc35-nkc6njjx6dsm'

def update_full():
    pf = printfulwrapper.PrintfulClient()
    try:
        products = pf.get('products')
        _update_products(products, pf)
    except printfulwrapper.PrintfulApiException as e:
        #Error code from the API
        print ('API exception: {} {}'.format(e.code, e.message))
    except printfulwrapper.PrintfulException as e:
        #Error while doing the request
        print ('Printful exception {}'.format(e.message))

def _update_products(js, pf):
    vendor = mm.PODVendor.objects.get(code='PF')

    for j in js:
        # BRAND
        if j['brand']:
            b, created = mm.VendorBrand.objects.get_or_create( name = j['brand'] )
            if created:
                print ("[BRAND] Created {}.".format(b.name))
        else:
            b = None

        # VendorCategory
        t, created = mm.VendorCategory.objects.get_or_create( 
          name=j['type'],
          vendor=vendor,
        )
        if created:
            print ("[VENDOR CATEGORY] Created {}.".format(t.name))

        # p = vp.master_product
        # print("[PRODUCT] {}".format(p.name))

        # Vendor Product
        vp, created = mm.VendorProduct.objects.update_or_create(
            mpn = j['id'],
            vendor = vendor,
            defaults = {
                'name': j['model'],
                'category': t,
                # 'master_product': mp,
                'image_url': j['image'],
                'brand': b,
            })
        if created:
            print("[VENDOR_PRODUCT] Created {}.".format(vp.name))

        try:
            variants = pf.get('products/{}'.format(vp.mpn))
            for v in variants['variants']:

                print("\t[VARIANT] {}".format(v['name']))

                try:
                    color_code = v['color_code'].upper().replace("#","")
                except:
                    color_code = ''

                vcolor,created = mm.VendorColor.objects.update_or_create(
                    color_code = color_code,
                    vendor = vendor,
                    defaults = {
                        'color_name': v['color'],
                    }
                )
                try:
                    master_color = mm.Color.objects.filter(hex_code=color_code)
                    master_color = master_color[0]
                    vcolor.master_color = master_color
                    vcolor.save()
                    print("\t\t[COLOR] Master Color match!")
                except:
                    master_color = None
                    print("\t\t[COLOR] Master Color not matched.")

                if not v['size']:
                    v['size'] = "None"
                try:
                    master_size = mm.Size.objects.filter()
                    master_size = master_size[0]
                    print("\t\t[SIZE] Master Size match!")
                except:
                    master_size = None
                    print("\t\t[SIZE] Master Size not matched.")

                vsize,created = mm.VendorSize.objects.update_or_create(
                    vendor_code = v['size'],
                    vendor = vendor,
                    defaults = {
                        # 'master_size': master_size,
                    }
                )

                # variant,created = mm.Variant.objects.update_or_create(
                #     product = p,
                #     title = v['name'],
                #     color = vcolor.master_color,
                #     size = vsize.master_size,
                #     defaults = {
                #         'image_url': v['image'],
                #     }
                # )

                vendorvariant,created = mm.VendorVariant.objects.update_or_create(
                    vendor_id = v['id'],
                    podvendor = vendor,
                    defaults = {
                        'vendor_product': vp,
                        'in_stock': v['in_stock'],
                        'price': v['price'],
                        'vendor_color': vcolor,
                        'vendor_size': vsize,
                    }
                )

        except printfulwrapper.PrintfulApiException as e:
            #Error code from the API
            print ('API exception: {} {}'.format(e.code, e.message))
        except printfulwrapper.PrintfulException as e:
            #Error while doing the request
            print ('Printful exception {}'.format(e.message))


def _update_products_old(js, pf):
        # ...
        if j['files']:
            for a in j['files']: # ARRAY
                ppf,created = pfPrintFile.objects.update_or_create(
                    product = p,
                    vendor_id = a['id'],
                    defaults = {
                        'title': a['title'],
                        'additional_price': a['additional_price'],
                    }
                )

        if j['dimensions']:
            for k,v in j['dimensions'].items(): # DICT
                pd,created = pfProductDimension.objects.update_or_create(
                    product = p,
                    label = k,
                    value = v,
                    defaults = {}
                )

        if j['options']:
            for a in j['options']: # ARRAY
                po,created = pfProductOption.objects.update_or_create(
                    product = p,
                    vendor_id = a['id'],
                    defaults = {
                        'title': a['title'],
                        'optiontype': a['type'],
                        'additional_price': a['additional_price'],
                    }
                )
                if a['values']:
                    for k,v in a['values'].items():
                        ov, created = pfOptionValue.objects.update_or_create(
                            option = po,
                            label = k,
                            defaults =  {
                                'datavalue': v,
                            }
                        )
