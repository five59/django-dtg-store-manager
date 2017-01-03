from django.db import models
from catalog import models as ca
from django.core.management.base import CommandError
import requests
from decimal import Decimal
import json
from . import models as gm


class APIInterface:

    mfgObj = None

    def __init__(self, code):
        try:
            self.mfgObj = ca.Manufacturer.objects.get(code=code)
        except Exception as e:
            print(e)

    def do_import(self):

        # first, check for required parameters:
        if not self.mfgObj.api_key:
            CommandError('This API requires a key in the admin panel.')

        if not self.mfgObj.apibase_url:
            CommandError('This API requires a base URL in the admin panel.')

        print("Importing data from {} ()".format(self.mfgObj.name, self.mfgObj.code))

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
        for p in gm.Product.objects.all():
            p.is_active = False
            p.save()

        # Now, start processing the data.
        print("-- Found {} products.".format(len(products)))

        for p in products:
            # Create (or update) the product
            p_obj, p_created = gm.Product.objects.update_or_create(
                id=p['Id'],
                defaults={
                    'is_active': True,
                    'id': p['Id'],
                    'uid': p['UId'],
                    'name': p['Name'],
                    'is_featured': p['IsFeatured'],
                    'is_coming_soon': p['IsComingSoon'],
                    'is_coming_soon': p['IsComingSoon'],
                    'has_available_product_variants': p['HasAvailableProductVariants'],
                    'has_product_templates': p['HasProductTemplates'],
                    'description': p['ShortDescription'],
                    'max_zoom': p['MaxZoom'],
                    'priceinfo_price': p['PriceInfo']['Price'],
                    'priceinfo_currencycode': p['PriceInfo']['CurrencyCode'],
                    'priceinfo_currencydigits': p['PriceInfo']['CurrencyDigits'],
                    'priceinfo_currencyformat': p['PriceInfo']['CurrencyFormat'],
                    'priceinfo_formattedprice': p['PriceInfo']['FormattedPrice'],
                    'retailprice_price': p['RetailPrice']['Price'],
                    'retailprice_currencycode': p['RetailPrice']['CurrencyCode'],
                    'retailprice_currencydigits': p['RetailPrice']['CurrencyDigits'],
                    'retailprice_currencyformat': p['RetailPrice']['CurrencyFormat'],
                    'retailprice_formattedprice': p['RetailPrice']['FormattedPrice'],
                })
            if p_created:
                rv = 'Created'
            else:
                rv = 'Updated'
            print("-- {} {} / {}".format(rv, p_obj.id, p_obj.name))

            # Reset and then Attach to Categories
            print("---- Categories: {} Found".format(len(p['Categories'])))
            p_obj.categories.clear()
            for c in p['Categories']:
                c_obj, c_created = gm.ProductCategory.objects.update_or_create(
                    id=c['Id'],
                    defaults={
                        'name': c['Name'],
                    }
                )
                p_obj.categories.add(c_obj)

            # Info Array
            # print("---- Info:")
            gm.ProductInfo.objects.filter(product=p_obj).delete()
            for i in p['Info']:
                ctype, created = gm.ContentType.objects.update_or_create(
                    name=i['ContentType'],
                    defaults={},
                )

                i_obj = gm.ProductInfo.objects.create(
                    product=p_obj,
                    content_type=ctype,
                    index=i['Index'],
                )
                if 'Key' in i:
                    i_obj.info_key = i['Key']
                    i_obj.save()

                gm.InfoContent.objects.filter(productinfo=i_obj).delete()
                for content in i['Content']:
                    gm.InfoContent.objects.create(
                        text=content,
                        productinfo=i_obj,
                    )

            # Images
            for i in gm.ProductImage.objects.filter(product=p_obj):
                i.is_active = False
                i.save()
            for i in p['Images']:
                imgobj, created = gm.ProductImage.objects.update_or_create(
                    id=i['Id'],
                    index=i['Index'],
                    url=i['Url'],
                    is_active=True,
                    product=p_obj,
                )
                imgobj.imagetypes.clear()
                for it in i['ImageTypes']:
                    it_obj, created = gm.ImageType.objects.update_or_create(
                        name=it,
                        defaults={},
                    )
                    imgobj.imagetypes.add(it_obj)

            # Variants
            if p_obj.has_available_product_variants:
                api_method = "productvariants/"
                querystring['productId'] = p_obj.id
                response = requests.request("GET", "".join(
                    [self.mfgObj.apibase_url, api_method]), headers=headers, params=querystring)
                if not response.ok:
                    CommandError("The API returned an error code.")

                variants = json.loads(response.content.decode('utf-8'))['ProductVariants']

                # Reset all to inactive (as above). Then, reactivate
                # within the update command.
                for v in gm.Variant.objects.filter(product=p_obj):
                    v.is_active = False
                    v.save()

                print("---- Found {} variants.".format(len(variants)))

                # Remove this now before the loop.
                del querystring['productId']

                for v in variants:
                    v_obj, created = gm.Variant.objects.update_or_create(
                        sku=v['Sku'],
                        product=p_obj,
                        defaults={
                            'is_active': True,
                            'has_templates': v['HasTemplates'],
                            'max_images': v['MaxImages'],
                            'priceinfo_price': v['PriceInfo']['Price'],
                            'priceinfo_currencycode': v['PriceInfo']['CurrencyCode'],
                            'priceinfo_currencydigits': v['PriceInfo']['CurrencyDigits'],
                            'priceinfo_currencyformat': v['PriceInfo']['CurrencyFormat'],
                            'priceinfo_formattedprice': v['PriceInfo']['FormattedPrice'],
                        },
                    )

                    # Option
                    gm.VariantOption.objects.filter(variant=v_obj).delete()
                    for vo in v['Options']:
                        logval = []
                        at_obj, at_cr = gm.Attribute.objects.update_or_create(
                            option_id=vo['OptionId'],
                            name=vo['Name'],
                            defaults={},
                        )
                        if at_cr:
                            logval.append("Created attribute {}".format(at_obj))

                        va_obj, va_cr = gm.AttributeValue.objects.update_or_create(
                            attribute=at_obj,
                            value_id=vo['ValueId'],
                            defaults={
                                'sort_value': vo['SortValue'] if 'SortValue' in vo else "",
                                'image_url': vo['ImageUrl'] if 'ImageUrl' in vo else "",
                                'image_type': vo['ImageType'] if 'ImageType' in vo else "",
                                'value': vo['Value'] if 'Value' in vo else "",
                            },
                        )
                        if va_cr:
                            logval.append("Created value {}".format(va_obj))

                        vo_obj = gm.VariantOption.objects.create(
                            variant=v_obj,
                            value=va_obj,
                        )
                        print("-- {} {}".format(vo_obj.variant.sku, " / ".join(logval)))

                    # VariantTemplates
                    api_method = "producttemplates/"
                    querystring['sku'] = v_obj.sku
                    response = requests.request("GET", "".join(
                        [self.mfgObj.apibase_url, api_method]), headers=headers, params=querystring)
                    if not response.ok:
                        CommandError("The API returned an error code.")

                    # print(json.dumps(json.loads(response.content.decode('utf-8'))))
                    try:
                        templates = json.loads(response.content.decode('utf-8'))['Options']
                        gm.VariantTemplate.objects.filter(variant=v_obj).update(is_active=False)
                        for t in templates:
                            t_obj, created = gm.VariantTemplate.objects.update_or_create(
                                variant=v_obj,
                                name=t['Name'],
                                defaults={
                                    'image_url': t['ImageUrl'],
                                    'is_default': t['IsDefault'],
                                    'is_active': True,
                                }
                            )
                            # Delete any existing TemplateSpaces. This should also remove relevant
                            # SpaceLayers
                            gm.TemplateSpace(variant_template=t_obj).delete()
                            for s in t['Spaces']:
                                s_obj = gm.TemplateSpace.objects.create(
                                    variant_template=t_obj,
                                    id=s['Id'],
                                    index=s['Index'] if 'Index' in s else 0,
                                    final_x1=s['FinalX1'] if 'FinalX1' in s else 0,
                                    final_x2=s['FinalX2'] if 'FinalX2' in s else 0,
                                    final_y1=s['FinalY1'] if 'FinalY1' in s else 0,
                                    final_y2=s['FinalY2'] if 'FinalY2' in s else 0,
                                )
                                for sl in s['Layers']:
                                    # layertype object
                                    lt_obj, created = gm.LayerType.objects.update_or_create(
                                        name=sl['Type'],
                                        defaults={},
                                    )
                                    l_obj = gm.SpaceLayer.objects.create(
                                        layer_type=lt_obj,
                                        templatespace=s_obj,
                                        id=sl['Id'],
                                        x1=sl['X1'],
                                        x2=sl['X2'],
                                        y1=sl['Y1'],
                                        y2=sl['Y2'],
                                        include_in_print=sl[
                                            'IncludeInPrint'] if 'IncludeInPrint' in sl else False,
                                        zIndex=sl['ZIndex'] if 'ZIndex' in sl else 0,
                                    )
                                print(
                                    "---- Added Template {} with {} spaces".format(t_obj.name, len(t['Spaces'])))
                    except Exception as e:
                        print(e)
