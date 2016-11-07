#!/usr/bin/env python
from .models import *
import json, io, sys, math, os
# from bs4 import BeautifulSoup
import requests
import shutil
from django.db import transaction


def load_google():
    filename = '/code/_data/google_product_taxonomy.csv'
    f = open(filename,'r')
    with transaction.atomic():
        with GoogleCategory.objects.disable_mptt_updates():
            for line in f:
                line = line.rstrip().split(';')
                obj, created = GoogleCategory.objects.update_or_create(
                    id = line[0],
                    long_name = line[1],
                )
                if created:
                    print("Created {}.".format(line[0]))
                else:
                    print("Updated {}.".format(line[0]))

def export_google():
    with open("/code/_data/google_product_export.csv", "w") as out:
        for item in GoogleCategory.objects.all():
            tags = item.long_name.split(' > ')
            output = "\t".join( [ str(item.id), str(item.parent), item.long_name ] )
            output = "{}\t{}{}".format(output, '\t'.join(tags), '\n' )
            out.write(output)
    out.close()

def reimport_google():
    fs = open('/code/_data/google_product_cleaned.csv','r')
    with transaction.atomic():
        with GoogleCategory.objects.disable_mptt_updates():
            for row in fs:
                try:
                    rx = str(row).replace('\n','').split('\t')
                # print(rx)
                    item = GoogleCategory.objects.get(id=int(rx[0]))
                    parent = GoogleCategory.objects.get(id=int(rx[1]))
                    item.parent = parent
                    item.save()
                    print("   OK: {} --> {}".format(item.name, parent.name))
                except:
                    print("!! Error: {} - {}".format(item.id, item.long_name))

def clean_google():
    # Do this loop with transactions and mptt updates turned off.
    # Otherwise it'll take years for it to complete.
    with transaction.atomic():
        with GoogleCategory.objects.disable_mptt_updates():
            for item in GoogleCategory.objects.all():
                tags = item.long_name.split(' > ')
                item.name = tags[len(tags)-1]
                print("-> Setting Name: {}".format(item.name))
                item.save()
    # Make sure to rebuild once everything up to date.
    GoogleCategory.objects.rebuild()

# for item in GoogleCategory.objects.all():
#     tags = item.long_name.split(" > ")
#     parent_name = tags[-2:-1]
#     parent_name = parent_name[0]
#     try:
#         # possaparents = GoogleCategory.objects.filter(name=parent_name)
#         # if possaparents.count() == 1:
#             # print("! {} is {}".format(item.name, possaparents[0]))
#         item.parent = None
#         item.save()
#         # else:
#         #     print("! {} found {}.".format(item.name, possaparents.count()))
#     except:
#         print("X Nope!")

    # for item in GoogleCategory.objects.all():
    #     tags = item.long_name.split(" > ")
    #     try:
    #         possaparents = GoogleCategory.objects.filter(name=tags[len(tags)-2])
    #         if possaparents == 1:
    #             item.parent = possaparents[0]
    #             item.save()
    #             print("{} -(PARENT)-> {}".format(item.name, item.parent.name))
    #         else:
    #             print("{} MULTIPLE PARENTS -----".format(item.name))
    #
    #     except:
    #         print("ERROR on {}".format(item.name))
    #
    # for item in GoogleCategory.objects.all():
    #     tags = item.long_name.split(' > ')
    #     try:
    #         item.parent = GoogleCategory.objects.get(name=tags[len(tags)-2])
    #         item.save()
    #         print("-> Set Parent as '{}' for '{}'.".format(item.parent, item.name))
    #     except:
    #         print("Had trouble with {}.".format(item.long_name))

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'
def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]
def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)

def load_colors():
    fns = [
        './_data/rgbto_uncoated.json',
        './_data/rgbto_coated.json',
    ]
    for filename in fns:
        f = open(filename)
        fj = json.load(f)
        for k,v in fj.items():
            try:
                rgbx = rgb(k)
            except:
                rgbx = 0, 0, 0
            c,created = Color.objects.update_or_create(
                name=v,
                defaults={
                  'pms_code':v,
                  'hex_code': k.upper(),
                  'r_value': rgbx[0],
                  'g_value': rgbx[1],
                  'b_value': rgbx[2],
                }
            )
            if created:
              print("--> Created {}".format(c.name))
            else:
              print("--> Updated {}".format(c.name))


def color_distance(c1, c2):
    (r1,g1,b1) = c1
    (r2,g2,b2) = rgb(c2)
    return math.sqrt(
        (r1-r2)**2 +
        (g1-g2)**2 +
        (b1-b2)**2
    )

def get_nearest_color(testcolor, colors):
    closest_colors = sorted(colors, key=lambda color: color_distance(color, testcolor))
    (r,g,b) = closest_colors[0]
    try:
        mc = Color.objects.filter(r_value=r, g_value=g, b_value=b)
        mc = mc[0]
        return mc
    except:
        return None

def relink_colors():
    print("--> Loading Colors")
    colors = []
    for c in Color.objects.all():
        colors.append( (c.r_value, c.g_value, c.b_value) )

    print("--> Starting VendorColor Loop")
    for vc in VendorColor.objects.all():
        print("    - Converting {}".format(vc.color_name))
        vc.master_color = get_nearest_color( vc.color_code, colors )
        vc.save()



def get_gildan_product(theProductCode):
    productDirectory = '/code/_product/gildan/'

    print("--> Gildan Product {}".format(theProductCode))

    print("    - Making request to Web site...")
    url = 'http://www.mygildan.com/store/us/browse/productDetailsPage.jsp?productId={}'.format(theProductCode)
    r = requests.get(url)
    if r.status_code == 200:
        print("    - Retrieved successfully. Now processing the soup...")
        soup = BeautifulSoup(r.content, 'html.parser')

        print('    - Soup complete. Now extracting data.')

        # Get SIZES
        size_stripper = ['\r','\t','\n']
        size_separator = '\xa0'
        sizes = soup.select('.size_list')[0].contents[0]
        for f in size_stripper:
            sizes = sizes.replace(f,'')
        sizes = sizes.strip(size_separator).split(size_separator)

        # Get COLORS
        colors = []
        colorlist = soup.select('.color_list')
        for cl in colorlist:
            for coloritem in cl.find_all('li'):
                colors.append(
                    {
                        'id': coloritem.attrs['data-color-id'],
                        'name': coloritem.attrs['data-color'],
                        'imageurl': coloritem['style'].replace('background-image: url(','http://www.mygildan.com').replace(');','')
                    }
                )

        # Get PRODUCT DETAILS
        name = ""
        n = soup.select('.details_info_name')[0].find_all('p')
        name = "{} {}".format(n[0].contents[0], n[1].contents[0])

        product = {
            'name': name,
            'sizes': sizes,
            'colors': colors
        }

        # Write the data to a file.
        productDirectory = "{}{}/".format(productDirectory, theProductCode)
        os.makedirs(os.path.dirname(productDirectory), exist_ok=True)

        with open('{}data.json'.format(productDirectory), 'w') as outfile:
            json.dump(product, outfile, sort_keys=True, indent=4)

        # Now get the IMAGES
        for c in product['colors']:
            for theNum in range(1,3):
                url = 'http://www.mygildan.com/img/products/{}/{}-{}-Alternate{}_lrg.jpg'.format(
                    theProductCode, theProductCode, c['id'], theNum)
                print("Requesting image {} for {}...".format(theNum, c['name']))
                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    with open("{}{}-{}-{}-{}.jpg".format(
                        productDirectory, theProductCode, c['id'], c['name'], theNum
                        ), 'wb') as f:
                        for chunk in r:
                            f.write(chunk)

    else:
        print("Problem")
    return product
