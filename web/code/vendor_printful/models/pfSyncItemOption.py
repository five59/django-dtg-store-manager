from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfSyncItemOption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    pid = models.CharField(_("Printful ID"), max_length=200, default="", blank=True, null=True)
    value = models.CharField(_("Value"), max_length=255, default="", blank=True, null=True)

    pfsyncvariant = models.ForeignKey("vendor_printful.pfSyncVariant")

    def __str__(self):
        if self.pid and self.name:
            return "{} - {}".format(self.pid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Sync Product")

    class Meta:
        verbose_name = _("Sync Item Option")
        verbose_name_plural = _("Sync Item Options")
        ordering = ["pid", ]
