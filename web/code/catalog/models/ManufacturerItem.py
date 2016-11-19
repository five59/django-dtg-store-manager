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

    def num_colors(self):
        return c.ManufacturerVariant.objects.filter(product=self).order_by('color').values('color').distinct().count()
    num_colors.short_description = "Colors"

    def get_colors(self):
        return c.ManufacturerVariant.objects.filter(product=self).order_by('color').values('color', 'color_code').distinct()

    def num_sizes(self):
        return c.ManufacturerVariant.objects.filter(product=self).order_by('size').values('size').distinct().count()
    num_sizes.short_description = "Sizes"

    def get_sizes(self):
        return c.ManufacturerVariant.objects.filter(product=self).order_by('size').values('size').distinct()

    def num_variants(self):
        return c.ManufacturerVariant.objects.filter(product=self).count()
    num_variants.short_description = "Variants"

    def get_price_range(self):
        val = c.ManufacturerVariant.objects.filter(
            product=self).aggregate(Max('base_price'), Min('base_price'))
        if val['base_price__max'] == val['base_price__min']:
            return locale.currency(val['base_price__min'])
        return "{} to {}".format(locale.currency(val['base_price__min']), locale.currency(val['base_price__max']))

    def __str__(self):
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
                        file_name = "{}-{}-{}{}".format(self.item.brand.code,
                                                        self.item.code, self.manufacturer.code, ext)
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
