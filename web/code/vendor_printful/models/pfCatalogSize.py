from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfCatalogSize(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=3, default="", blank=True, null=True)

    label = models.CharField(_("Size"), max_length=255, default="", blank=True, null=True)
    label_clean = models.CharField(_("Clean Label"), max_length=255,
                                   default="", blank=True, null=True)

    sort_group = models.CharField(_("Sort Group"), max_length=2, default="", blank=True, null=True)
    sort_order = models.CharField(_("Sort Order"), max_length=16, default="", blank=True, null=True)

    def get_name(self):
        if self.label_clean:
            rv = self.label_clean
        elif self.label:
            rv = self.label
        else:
            rv = "-"
        return rv
    get_name.short_description = _("Name")

    def __str__(self):
        rv = []
        if self.code:
            rv.append(self.code)
        rv.append(self.get_name())
        if rv:
            return " - ".join(rv)
        else:
            return "-"

    class Meta:
        verbose_name = _("Catalog Size")
        verbose_name_plural = _("Catalog Size")
        ordering = ["sort_group", "sort_order", "label", ]
