from django.db import models
from catalog import models as ca
from django.core.management.base import CommandError
from .wrapper import PrintfulClient, PrintfulException, PrintfulApiException
from decimal import Decimal


class APIInterface:

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
        p_count = 0
        p_total = len(products)
        for p in products:
            p_count += 1
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
                print("\n{} of {} Created: \t{} / {}.".format(p_count, p_total, vp.code, vp.name))
            else:
                print("\n{} of {} Updated: \t{} / {}.".format(p_count, p_total, vp.code, vp.name))

            # Import Dimensions
            if p['dimensions']:
                # First, flush the is_active field
                for f in ca.ManufacturerItemDimension.objects.filter(manufacturer_item=vp):
                    f.is_active = False
                    f.save()
                counter = 0
                for code, name in p['dimensions'].items():
                    counter += 1
                    pd, pdcreated = ca.ManufacturerItemDimension.objects.update_or_create(
                        manufacturer_item=vp,
                        code=code,
                        defaults={
                            'name': name,
                            'is_active': True,
                        }
                    )
                print("-- Created/updated {} dimensions.".format(counter))
            else:
                print('-- No dimensions specified.')

            # Import File Specs
            if p['files']:
                # First, flush the is_active field
                for f in ca.ManufacturerItemFile.objects.filter(manufacturer_item=vp):
                    f.is_active = False
                    f.save()
                counter = 0
                for f in p['files']:
                    counter += 1
                    if not f['additional_price']:
                        f['additional_price'] = 0
                    pd, pdcreated = ca.ManufacturerItemFile.objects.update_or_create(
                        manufacturer_item=vp,
                        code=f['id'],
                        defaults={
                            'name': f['title'],
                            'additional_price': f['additional_price'],
                            'is_active': True,
                        }
                    )
                print("-- Created/updated {} file specs.".format(counter))
            else:
                print("-- No files specified.")

            # Import Options #TODO

            # Now, we're ready to ingest the variants:
            variants = None
            try:
                variants = api.get('products/{}'.format(vp.code))
            except PrintfulApiException as e:
                print ('API exception: {} {}'.format(e.code, e.message))
            except PrintfulException as e:
                print ('Printful exception {}'.format(e.message))

            # Reset all to inactive (as above for ManufacturerItem). Then, reactivate
            # within the update command.
            for v in ca.ManufacturerVariant.objects.filter(product=vp):
                v.is_active = False
                v.save()

            c_counter = 0
            u_counter = 0
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
                        'in_stock': v['in_stock'],
                        'is_active': True,
                        'base_price': Decimal(v['price']),
                    },
                )
                if vcreated:
                    c_counter += 1
                else:
                    u_counter += 1
            print("-- Updated {} variants, and created {}.".format(u_counter, c_counter))

    def get_filelibrary(self):
        print("Importing File Library")
        ITEMS_PER_PAGE = 100

        if not self.mfgObj.api_key:
            CommandError('This API requires a key.')
        api = PrintfulClient(self.mfgObj)
        thefiles = None
        try:
            # First do a quick one to see what the total is.
            params = {
                'offset': 0,
                'limit': 1,
            }
            thefiles = api.get('files', params=params)
        except PrintfulApiException as e:
            print ('API exception:', e)
        except PrintfulException as e:
            print("Printful Exception: ", e)

        for i in ca.ManufacturerFileLibraryItem.objects.filter(manufacturer=self.mfgObj):
            i.is_active = False
            i.save()

        for offset in range(0, api.item_count(), ITEMS_PER_PAGE):
            print("Getting items {} to {} of {}...".format(
                offset, offset + ITEMS_PER_PAGE, api.item_count()))
            try:
                params = {
                    'offset': offset,
                    'limit': ITEMS_PER_PAGE,
                }
                thefiles = api.get('files', params=params)
            except PrintfulApiException as e:
                print ('API exception:', e)
            except PrintfulException as e:
                print("Printful Exception: ", e)

            c_counter = 0
            u_counter = 0
            for i in thefiles:
                fli, created = ca.ManufacturerFileLibraryItem.objects.update_or_create(
                    code=i['id'],
                    manufacturer=self.mfgObj,
                    defaults={
                        "is_active": True,
                        "name": i['type'],
                        "hashvalue": i['hash'],
                        "url": i['url'],
                        "filename": i['filename'],
                        "mime_type": i['mime_type'],
                        "size": i['size'],
                        "width": i['width'],
                        "height": i['height'],
                        "dpi": i["dpi"],
                        "status": i["status"],
                        "created": i["created"],
                        "thumbnail_url": i["thumbnail_url"],
                        "preview_url": i["preview_url"],
                        "visible": i["visible"],
                    }
                )
                if created:
                    c_counter += 1
                else:
                    u_counter += 1
            print("-- Page: Added {} files, and updated {}.".format(c_counter, u_counter))
