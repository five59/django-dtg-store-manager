from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from decimal import *


class pfCatalogVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_("Is Active?"), help_text=_(""), default=True)

    pid = models.CharField(_("Printful ID"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    pfsize = models.ForeignKey("vendor_printful.pfCatalogSize",
                               blank=True, null=True, verbose_name=_("Size"))
    pfcolor = models.ForeignKey("vendor_printful.pfCatalogColor",
                                blank=True, null=True, verbose_name=_("Color"))

    image = models.CharField(_("Image"), max_length=255, default="", blank=True, null=True)
    price = models.CharField(_("Price"), max_length=255, default="", blank=True, null=True)
    in_stock = models.BooleanField(_("In Stock"), default=False)

    weight = models.DecimalField(_("Weight (oz)"), default=0, blank=True,
                                 null=True, decimal_places=2, max_digits=5)
    ship_us_1 = models.DecimalField(_("US Ship 1st"), help_text=_(
        "Shipping Rate: USA, First Item"), default=0, decimal_places=2, max_digits=5)
    ship_us_2 = models.DecimalField(_("US Ship 2nd"), help_text=_(
        "Shipping Rate: USA, Additional Item"), default=0, decimal_places=2, max_digits=5)
    ship_ca_1 = models.DecimalField(_("CA Ship 1st"), help_text=_(
        "Shipping Rate: Canada, First Item"), default=0, decimal_places=2, max_digits=5)
    ship_ca_2 = models.DecimalField(_("CA Ship 2nd"), help_text=_(
        "Shipping Rate: Canada, Additional Item"), default=0, decimal_places=2, max_digits=5)
    ship_ww_1 = models.DecimalField(_("WW Ship 1st"), help_text=_(
        "Shipping Rate: Worldwide, First Item"), default=0, decimal_places=2, max_digits=5)
    ship_ww_2 = models.DecimalField(_("WW Ship 2nd"), help_text=_(
        "Shipping Rate: Worldwide, Additional Item"), default=0, decimal_places=2, max_digits=5)

    pfcatalogproduct = models.ForeignKey(
        "vendor_printful.pfCatalogProduct", verbose_name=_("Product"))

    def get_brand(self):
        return self.pfcatalogproduct.brand
    get_brand.short_description = _("Brand")

    def get_allowed_files(self):
        return pfCatalogFileType.objects.filter(pfcatalogproduct=self)
    get_allowed_files.short_description = _("Allowed Files")

    def get_allowed_options(self):
        return pfCatalogOptionType.objects.filter(pfcatalogproduct=self)
    get_allowed_options.short_description = _("Allowed Options")

    def get_sku_part(self):
        try:
            p = int(self.pid if self.pid else 0)
            c = self.pfcolor.code if self.pfcolor.code else "000"
            s = self.pfsize.code if self.pfsize.code else "000"
            rv = "{p:05d}-{c}{s}".format(p=p, c=c, s=s)
        except Exception as e:
            print("Code missing from pfColor or pfSize.", e)
            rv = "-"
        return rv
    get_sku_part.short_description = _("SKU")

    def __str__(self):
        if self.pid and self.name:
            return "{} - {}".format(self.pid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Catalog Variant")

    class Meta:
        verbose_name = _("Catalog Variant")
        verbose_name_plural = _("Catalog Variants")
        ordering = ["name", ]
