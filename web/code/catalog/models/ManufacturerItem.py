from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog import models as c
from django.db.models import Avg, Max, Min
import locale
import requests
import urllib
import tempfile
from django.core import files
import os
from colour import Color as libColor
from decimal import *


class ManufacturerItem(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Vendor Code"), max_length=64, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    manufacturer = models.ForeignKey(c.Manufacturer, blank=True, null=True)

    item = models.ForeignKey(c.Item, blank=True, null=True)

    brand = models.CharField(_("Brand"), max_length=255, default="", blank=True, null=True)
    category = models.CharField(_("Category"), max_length=255, default="", blank=True, null=True)

    image_url = models.URLField(_("Image URL"), blank=True, null=True)

    is_active = models.BooleanField(_("Is Active?"), default=False, blank=True)
    dt_added = models.DateTimeField(_("Date Added"), auto_now_add=True, null=True, blank=True)
    dt_updated = models.DateTimeField(_("Last Updated"), auto_now=True, null=True, blank=True)

    def _colorstep(color, repetitions=1):
        lum = math.sqrt(.241 * color['r'] + .691 * color['g'] + .068 * color['b'])
        h, s, v = colorsys.rgb_to_hsv(color['r'], color['g'], color['b'])
        h2 = int(h * repetitions)
        lum2 = int(lum * repetitions)
        v2 = int(v * repetitions)
        return (h2, lum, v2)

    # TODO Sorted Colors. Not an easy task.
    # def get_sorted_colors(self):
    #     # First, get the colors for this item
    #     colors = c.ManufacturerVariant.objects.filter(product=self).order_by(
    #         'color').values('color', 'color_code').distinct()
    #     # Now, hash out the rgb values, based on the hex code and assigned to ordered array
    #     sortedcolors = []
    #     for x in colors:
    #         tmpColor = libColor(x['color_code'])
    #         vr, vg, vb = tmpColor.get_rgb()
    #         sortedcolors.append({
    #             'r': vr,
    #             'g': vg,
    #             'b': vb,
    #             'color_code': x['color_code'],
    #             'color': x['color']
    #         })
    #     # Do the sorting step-by-step
    #     sorted(sortedcolors, key=lambda color: self._colorstep(sortedcolors, 8))
    #     return sortedcolors

    def get_master_category(self):
        if self.item:
            return self.item.category
        return None
    get_master_category.short_description = "Master Category"

    def num_colors(self):
        return c.ManufacturerVariant.objects.filter(product=self).order_by('color').values('color').distinct().count()
    num_colors.short_description = "Colors"

    def get_colors(self):
        coldata = c.ManufacturerVariant.objects.filter(product=self).order_by('color').values(
            'color_obj__name', 'color_obj__hex_code', 'color_obj__sortorder').distinct()
        try:
            rv = sorted(coldata, key=lambda k: k['color_obj__sortorder'])
        except:
            rv = None
        return rv

    def num_sizes(self):
        return c.ManufacturerVariant.objects.filter(product=self).order_by('size').values('size').distinct().count()
    num_sizes.short_description = "Sizes"

    def get_sizes(self):
        return c.ManufacturerVariant.objects.filter(product=self).order_by('size').values('size').distinct()

    def get_variants(self):
        return c.ManufacturerVariant.objects.filter(product=self)
    get_variants.short_description = "Variants"

    def num_variants(self):
        return self.get_variants().count()
    num_variants.short_description = "Variants"

    def get_price_min(self):
        rv = c.ManufacturerVariant.objects.filter(product=self).aggregate(Min('base_price'))
        return rv['base_price__min']

    def get_price_range(self):
        val = c.ManufacturerVariant.objects.filter(
            product=self).aggregate(Max('base_price'), Min('base_price'))
        if val['base_price__max'] == val['base_price__min']:
            return locale.currency(val['base_price__min'])
        return "{} to {}".format(locale.currency(val['base_price__min']), locale.currency(val['base_price__max']))
    get_price_range.short_description = 'Price Range'

    # def get_profit(self):
    #     rv = self.item.default_retail - self.get_price_min()
    #     return rv
    # get_profit.short_description = 'Profit'
    #
    # def get_profit_str(self):
    #     return'${:,.2f}'.format(self.get_profit())
    # get_profit_str.short_description = 'Profit'
    #
    # def get_profit_margin(self):
    #     rv = self.get_profit() / self.item.default_retail
    #     return "{0:.0f}%".format(rv*100)
    # get_profit_margin.short_description = 'Margin'
    #
    # def get_profit_coupon10(self):
    #     rv = self.get_profit() - (
    #         self.item.default_retail * Decimal('0.1')
    #     )
    #     return rv
    # get_profit_coupon10.short_description="10% Coupon Profit"
    #
    # def get_profit_coupon10_str(self):
    #     return '${:,.2f}'.format(self.get_profit_coupon10())
    # get_profit_coupon10_str.short_description = '10% Coupon Profit'
    #
    # def get_edc_coupon10(self):
    #     rv = self.item.default_retail * Decimal('0.1')
    #     return '${:,.2f}'.format(rv)
    # get_edc_coupon10.short_description = 'Effective Discount 10%'
    #
    # def get_profit_margin_coupon10(self):
    #     rv = self.get_profit_coupon10() / self.item.default_retail
    #     return "{0:.0f}%".format(rv * 100)
    # get_profit_margin_coupon10.short_description='10% Coupon Margin'

    def __str__(self):
        if self.item:
            return "{}".format(self.item)
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Manufacturer Item")

    def download_image(self):
        if self.item:
            if not self.item.image:
                if self.image_url:
                    print("--> Attempting download of linked image for {}.".format(self.name))
                    request = requests.get(self.image_url, stream=True)
                    if request.status_code == requests.codes.ok:
                        path = urllib.parse.urlparse(self.image_url).path
                        ext = os.path.splitext(path)[1]
                        file_name = "mfg_item/{}/{}/{}{}".format(
                            self.item.brand.code,
                            self.item.code,
                            self.manufacturer.code,
                            ext
                        )
                        lf = tempfile.NamedTemporaryFile()
                        for block in request.iter_content(1024 * 8):
                            if not block:
                                break
                            lf.write(block)
                        self.item.image.save(file_name, files.File(lf))

    def save(self, *args, **kwargs):
        self.download_image()
        super(ManufacturerItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Manufacturer Item")
        verbose_name_plural = _("Manufacturer Items")
        ordering = ["name", "code", ]
