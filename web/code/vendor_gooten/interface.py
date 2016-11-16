from django.db import models
from catalog import models as ca
from django.core.management.base import CommandError
import requests
from decimal import Decimal
import json


class APIInterface:

    mfgObj = None

    def __init__(self, vObj):
        self.mfgObj = vObj

    def do_import(self):

        # first, check for required parameters:
        if not self.mfgObj.api_key:
            CommandError('This API requires a key in the admin panel.')

        if not self.mfgObj.apibase_url:
            CommandError('This API requires a base URL in the admin panel.')

        print("--> Starting Import Process")

        api_method = "products/"

        querystring = {
            "recipeid": self.mfgObj.api_key,
            "languageCode": "en",
            "countryCode": "US",
            "all": "true",
        }
        headers = {
            "content-type": "application/json"
        }

        response = requests.request("GET", "".join(
            [self.mfgObj.apibase_url, api_method]), headers=headers, params=querystring)

        if not response.ok:
            CommandError("The API returned an error code.")

        products = json.loads(response.content.decode('utf-8'))['Products']

        # If that was successful, then let's invalidate all local data, by
        # swapping the is_active flag to negative. This will help to avoid
        # orphans without destroying the links to the central catalog.
        for p in ca.ManufacturerItem.objects.filter(manufacturer=self.mfgObj):
            p.is_active = False
            p.save()

        # Now, start processing the data.
        print("--> Found {} products.".format(len(products)))
        for p in products:
            if not p['IsComingSoon']:  # Skip inactive products

                vp, pcreated = ca.ManufacturerItem.objects.update_or_create(
                    code=p['Id'],
                    manufacturer=self.mfgObj,
                    defaults={
                        'name': p['Name'],
                        'category': p['Categories'][0]["Name"],
                        'is_active': True,
                    }
                )
                if pcreated:
                    print("Manufacturer Item Added: {} / {}".format(vp.code, vp.name))
                else:
                    print("Manufacturer Item Updated: {} / {}".format(vp.code, vp.name))

                # Now, we're ready to ingest the variants:
                if p['HasAvailableProductVariants']:
                    variants = None
                    querystring['productid'] = vp.code
                    response = requests.request("GET", "".join(
                        [self.mfgObj.apibase_url, "productvariants/"]), headers=headers, params=querystring)

                    if not response.ok:
                        CommandError("The API returned an error code.")

                    pvs = json.loads(response.content.decode('utf-8'))['ProductVariants']
                    # Reset all to inactive (as above for ManufacturerItem). Then, reactivate
                    # within the update command.
                    for v in ca.ManufacturerVariant.objects.filter(product=vp):
                        v.is_active = False
                        v.save()

                    print("--> Found {} variants for {}.".format(len(pvs), vp.name))
                    for v in pvs:
                        vv, vcreated = ca.ManufacturerVariant.objects.update_or_create(
                            code=v['Sku'],
                            product=vp,
                            defaults={
                                'name': v['Sku'],
                                # 'size': v['size'],
                                # 'color': v['color'],
                                # 'color_code': v['color_code'],
                                # 'image_url': v['image'],
                                # 'in_stock': v['in_stock'],
                                'is_active': True,
                                'base_price': Decimal(v['PriceInfo']['Price']),
                            },
                        )

                if vcreated:
                    print(" - Created: {} / {} {}".format(vv.code, vv.size, vv.color))
                else:
                    print(" - Updated: {} / {} {}".format(vv.code, vv.size, vv.color))
