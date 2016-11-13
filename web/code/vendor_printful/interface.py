from django.db import models
from catalog import models as ca
from django.core.management.base import CommandError
from .wrapper import PrintfulClient, PrintfulException, PrintfulApiException
from decimal import Decimal


class PrintfulInterface:

    mfgObj = None

    def __init__(self, vObj):
        self.mfgObj = vObj

    def do_import(self):

        print("--> Starting Import Process")

        # This one only requires a key, not a hash:
        if not self.mfgObj.api_key:
            CommandError('This API requires a key.')
        api = PrintfulClient(self.mfgObj)

        # First, try making a call.
        products = None
        try:
            products = api.get('products')
            print("There are {} products.".format(len(products)))
        except PrintfulApiException as e:
            print ('API exception: {} {}'.format(e.code, e.message))
        except PrintfulException as e:
            print ('Printful exception {}'.format(e.message))

        # If that was successful, then let's invalidate all local data, by
        # swapping the is_active flag to negative. This will help to avoid
        # orphans without destroying the links to the central catalog.
        for p in ca.ManufacturerItem.objects.filter(manufacturer=self.mfgObj):
            p.is_active = False
            p.save()

        # Now, start processing the data.
        for p in products:
            vp, pcreated = ca.ManufacturerItem.objects.update_or_create(
                code=p['id'],
                manufacturer=self.mfgObj,
                defaults={
                    'name': p['model'],
                    'brand': p['brand'],
                    'category': p['type'],
                    'image_url': p['image'],
                    'is_active': True,
                }
            )
            if pcreated:
                print("Manufacturer Item Added: {} / {}".format(vp.code, vp.name))
            else:
                print("Manufacturer Item Updated: {} / {}".format(vp.code, vp.name))

            # Now, we're ready to ingest the variants:
            variants = None
            try:
                variants = api.get('products/{}'.format(vp.code))
                print("  There are {} variants.".format(len(variants['variants'])))
            except PrintfulApiException as e:
                print ('API exception: {} {}'.format(e.code, e.message))
            except PrintfulException as e:
                print ('Printful exception {}'.format(e.message))

            # Reset all to inactive (as above for ManufacturerItem). Then, reactivate
            # within the update command.
            for v in ca.ManufacturerVariant.objects.filter(product=vp):
                v.is_active = False
                v.save()

            for v in variants['variants']:
                vv, vcreated = ca.ManufacturerVariant.objects.update_or_create(
                    code=v['id'],
                    product=vp,
                    defaults={
                        'name': v['name'],
                        'size': v['size'],
                        'color': v['color'],
                        'color_code': v['color_code'],
                        'image_url': v['image'],
                        # 'price': Decimal(v['price']),
                        'in_stock': v['in_stock'],
                        'is_active': True,
                    },
                )
                if vcreated:
                    print(" - Created: {} / {} {}".format(vv.code, vv.size, vv.color))
                else:
                    print(" - Updated: {} / {} {}".format(vv.code, vv.size, vv.color))
