from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfSyncVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    pid = models.CharField(_("Printful ID"), max_length=200, default="", blank=True, null=True)
    external_id = models.CharField(_("External ID"), max_length=200,
                                   default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    synced = models.BooleanField(_("Synced"), default=False)

    pfsyncproduct = models.ForeignKey(
        "vendor_printful.pfSyncProduct", verbose_name=_("Sync Product"))
    pfcatalogvariant = models.ForeignKey(
        "vendor_printful.pfCatalogVariant", verbose_name=_("Catalog Variant"), blank=True, null=True)

    files = models.ManyToManyField("vendor_printful.pfPrintFile", blank=True)

    def get_store(self):
        return self.pfsyncproduct.pfstore
    get_store.short_description = _("Store")

    def get_store_code(self):
        return self.get_store().code
    get_store_code.short_description = _("Store")

    def __str__(self):
        if self.pid and self.name:
            return "{} - {}".format(self.pid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Sync Variant")

    class Meta:
        verbose_name = _("Sync Variant")
        verbose_name_plural = _("Sync Variants")
        ordering = ["name", "pid", ]
