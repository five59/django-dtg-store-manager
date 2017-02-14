from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog import models as c


class ShippingClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Vendor Code"), max_length=64, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    manufacturer = models.ForeignKey('catalog.Manufacturer', blank=True, null=True)

    us_item1 = models.DecimalField(_("First Item (US)"), help_text=_("Domestic Shipping. Cost for the first item."),
                                   max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    ca_item1 = models.DecimalField(_("First Item (CA)"), help_text=_("Shipping to Canada. Cost for the first item."),
                                   max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    ww_item1 = models.DecimalField(_("First Item (WW)"), help_text=_("Global Shipping (ex US/CA). Cost for the first item."),
                                   max_digits=5, decimal_places=2, default=0, blank=True, null=True)

    us_addl = models.DecimalField(_("Additional Item (US)"), help_text=_("Cost for subsequent items after the first."),
                                  max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    ca_addl = models.DecimalField(_("Additional Item (CA)"), help_text=_("Cost for subsequent items after the first."),
                                  max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    ww_addl = models.DecimalField(_("Additional Item (WW)"), help_text=_("Cost for subsequent items after the first."),
                                  max_digits=5, decimal_places=2, default=0, blank=True, null=True)

    def num_items(self):
        return c.ManufacturerVariant.objects.filter(shippingclass=self).count()
    num_items.short_description = 'Item Count'

    def __str__(self):
        # return ("{} / {} / {}".format(self.us_item1, self.ca_item1, self.ww_item1))
        rv = [
            self.code if self.code else "XX",
            # self.name if self.name else "Unnamed Item",
            '${:,.2f}'.format(self.us_item1) if self.us_item1 else "?.??",
            '${:,.2f}'.format(self.ca_item1) if self.ca_item1 else "?.??",
            '${:,.2f}'.format(self.ww_item1) if self.ww_item1 else "?.??",
        ]
        return " / ".join(rv)

    class Meta:
        verbose_name = _("Shipping Class")
        verbose_name_plural = _("Shipping Classes")
        ordering = ('code',)