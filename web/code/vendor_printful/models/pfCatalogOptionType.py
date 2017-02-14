from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfCatalogOptionType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    pid = models.CharField(_("Printful ID"), max_length=255, default="", blank=True, null=True)
    title = models.CharField(_("Title"), max_length=255, default="", blank=True, null=True)
    type = models.CharField(_("Type"), max_length=255, default="", blank=True, null=True)
    additional_price = models.CharField(
        _("Additional Price"), max_length=100, default="", blank=True, null=True)

    pfcatalogvariant = models.ForeignKey("vendor_printful.pfCatalogVariant")

    def __str__(self):
        if self.pid and self.title:
            return "{} - {}".format(self.pid, self.title)
        if self.title:
            return "{}".format(self.title)
        return _("Unnamed Catalog File Type")

    class Meta:
        verbose_name = _("Catalog Option Type")
        verbose_name_plural = _("Catalog Option Types")
        ordering = ["title", "pid", ]
