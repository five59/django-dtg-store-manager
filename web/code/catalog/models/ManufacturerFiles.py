from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog import models as c


class ManufacturerFiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    additional_price = models.DecimalField(
        _("Additional Cost"), max_digits=6, decimal_places=2, default=0)
    manufacturer_item = models.ForeignKey(c.ManufacturerItem, blank=True, null=True)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed ManufacturerFiles")

    class Meta:
        verbose_name = _("ManufacturerFiles")
        verbose_name_plural = _("ManufacturerFiles")
        ordering = ["name", "code", ]
