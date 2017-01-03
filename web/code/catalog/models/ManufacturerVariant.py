from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog import models as c


class ManufacturerVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=150, default="", blank=True, null=True)
    product = models.ForeignKey(c.ManufacturerItem, null=True, blank=True)

    # This is a transient value that is calculated on save from the associated product.
    manufacturer = models.ForeignKey(c.Manufacturer, null=True, blank=True)

    name = models.CharField(_("Name"), max_length=150, default="",
                            blank=True, null=True, help_text="")
    size = models.CharField(_("Size"), max_length=64, default="", blank=True, null=True)
    color = models.CharField(_("Color"), max_length=64, default="", blank=True, null=True)
    color_code = models.CharField(_("Color Code"), max_length=64, default="", blank=True, null=True)
    color_obj = models.ForeignKey(c.Color, blank=True, null=True)

    image_url = models.URLField(_("Image URL"), null=True, blank=True)
    in_stock = models.BooleanField(_("In Stock?"), default=False)

    base_price = models.DecimalField(_("Base Price"), max_digits=6, decimal_places=2, default=0)

    is_active = models.BooleanField(_("Is Active?"), default=False)
    dt_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dt_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    shipping_us = models.DecimalField(
        _("Shipping (US)"), help_text=_("Domestic Shipping. Cost for the first item."), max_digits=6, decimal_places=2, default=0)
    shipping_ca = models.DecimalField(
        _("Shipping (CA)"), help_text=_("Shipping to Canada. Cost for the first item."), max_digits=6, decimal_places=2, default=0)
    shipping_ww = models.DecimalField(
        _("Shipping (WW)"), help_text=_("Global Shipping (ex US/CA). Cost for the first item."), max_digits=6, decimal_places=2, default=0)

    shipping_us_addl = models.DecimalField(
        _("Shipping (US) Addl"), help_text=_("Cost for subsequent items after the first."), max_digits=6, decimal_places=2, default=0)
    shipping_ca_addl = models.DecimalField(
        _("Shipping (CA) Addl"), help_text=_("Cost for subsequent items after the first."), max_digits=6, decimal_places=2, default=0)
    shipping_ww_addl = models.DecimalField(
        _("Shipping (WW) Addl"), help_text=_("Cost for subsequent items after the first."), max_digits=6, decimal_places=2, default=0)

    weight = models.DecimalField(
        _("Weight (oz)"), max_digits=6, decimal_places=2, default=0)

    @property
    def price(self):
        return "${}".format(self.price)

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Manufacturer Variant")

    class Meta:
        verbose_name = _("Manufacturer Variant")
        verbose_name_plural = _("Manufacturer Variants")
        ordering = ["name", "code", ]

    def save(self, *args, **kwargs):
        # Manage the transient value here so that we can filter on it, since we
        # can't filter calculated values.
        if self.product:
            self.manufacturer = self.product.manufacturer
        else:
            self.manufacturer = None

        super(ManufacturerVariant, self).save(*args, **kwargs)
