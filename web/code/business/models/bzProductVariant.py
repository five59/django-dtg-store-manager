from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from vendor_printful.models.pfCatalogVariant import pfCatalogVariant


class bzProductVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=64, default="", blank=True, null=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    bzproduct = models.ForeignKey("business.bzProduct", verbose_name=_("Product"))
    pfcatalogvariant = models.ForeignKey(
        "vendor_printful.pfCatalogVariant", verbose_name=_("Printful Variant"))

    def get_color(self):
        return self.pfcatalogvariant.pfcolor
    get_color.short_description = _("Color")

    def get_size(self):
        return self.pfcatalogvariant.pfsize
    get_size.short_description = _("Size")

    def _update_sku(self):
        sku = []
        if self.pfcatalogvariant:
            if self.pfcatalogvariant.pfcolor:
                if self.pfcatalogvariant.pfcolor.code:
                    sku.append(self.pfcatalogvariant.pfcolor.code)
                else:
                    sku.append("XXX")
            else:
                sku.append("XXX")
            if self.pfcatalogvariant.pfsize:
                if self.pfcatalogvariant.pfsize.code:
                    sku.append(self.pfcatalogvariant.pfsize.code)
                else:
                    sku.append("XXX")
            else:
                sku.append("XXX")
        rv = "{}-{}".format(self.bzproduct.code, "".join(sku))
        self.code = rv

    def save(self, *args, **kwargs):
        # Set the Code (SKU Base)
        self._update_sku()
        super(bzProductVariant, self).save(*args, **kwargs)

    def __str__(self):
        if self.code:
            return self.code
        return _("Unnamed bzProduct Variant")

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")
        ordering = ["code", ]
