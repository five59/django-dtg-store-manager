from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog import models as c


class VendorVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    product = models.ForeignKey(c.VendorItem, null=True, blank=True)
    name = models.CharField(_("Name"), max_length=150, default="",
                            blank=True, null=True, help_text="")
    size = models.CharField(_("Size"), max_length=64, default="", blank=True, null=True)
    color = models.CharField(_("Size"), max_length=64, default="", blank=True, null=True)
    color_code = models.CharField(_("Size"), max_length=64, default="", blank=True, null=True)

    image_url = models.URLField(_("Image URL"), null=True, blank=True)
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)

    is_active = models.BooleanField(_("Is Active?"), default=False)
    dt_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dt_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    @property
    def price(self):
        return "${}".format(self.price)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Vendor Variant")

    class Meta:
        verbose_name = _("Vendor Variant")
        verbose_name_plural = _("Vendor Variants")
        ordering = ["name", "code", ]
