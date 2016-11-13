from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog import models as c


class VendorItem(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Vendor Code"), max_length=64, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    manufacturer = models.ForeignKey(c.Manufacturer, blank=True, null=True)

    brand = models.CharField(_("Brand"), max_length=255, default="", blank=True, null=True)
    category = models.CharField(_("Category"), max_length=255, default="", blank=True, null=True)

    image_url = models.URLField(_("Image URL"), blank=True, null=True)

    is_active = models.BooleanField(_("Is Active?"), default=False, blank=True)
    dt_added = models.DateTimeField(_("Date Added"), auto_now_add=True, null=True, blank=True)
    dt_updated = models.DateTimeField(_("Last Updated"), auto_now=True, null=True, blank=True)

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Vendor Item")

    class Meta:
        verbose_name = _("Vendor Item")
        verbose_name_plural = _("Vendor Items")
        ordering = ["name", "code", ]
