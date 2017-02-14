from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfSyncProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    pid = models.CharField(_("Printful ID"), max_length=200, default="", blank=True, null=True)
    external_id = models.CharField(_("External ID"), max_length=200,
                                   default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    variants = models.IntegerField(_("Variant Count"), default=0)
    synced = models.IntegerField(_("Synced"), default=0)

    pfstore = models.ForeignKey("vendor_printful.pfStore", verbose_name=_("Store"))

    def all_synced(self):
        if self.synced == self.variants:
            return True
        return False
    all_synced.boolean = True
    all_synced.short_description = _("All Synced?")

    def __str__(self):
        if self.pid and self.name:
            return "{} - {}".format(self.pid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Sync Product")

    class Meta:
        verbose_name = _("Sync Product")
        verbose_name_plural = _("Sync Products")
        ordering = ["name", "pid", ]
