from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class bzBrand(models.Model):
    """
    Links a :model:`vendor_printful.pfStore` with a :model:`outlet_woocommerce.wooStore`.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=2)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    vendor = models.ForeignKey(
        "vendor_printful.pfStore", verbose_name=_("Vendor"), blank=True, null=True)
    outlet = models.ForeignKey(
        "outlet_woocommerce.wooStore", verbose_name=_("Outlet"), blank=True, null=True)

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Brand")

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        ordering = ["name", ]
