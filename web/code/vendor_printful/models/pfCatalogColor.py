from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfCatalogColor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=3, default="", blank=True, null=True)

    label = models.CharField(_("Color"), max_length=255, default="", blank=True, null=True)
    label_clean = models.CharField(_("Clean Label"), max_length=255,
                                   default="", blank=True, null=True)

    hex_code = models.CharField(_("Color Hex Code"), max_length=255,
                                default="", blank=True, null=True)

    def __str__(self):
        rv = []
        if self.code:
            rv.append(self.code)
        if self.label_clean:
            rv.append(self.label_clean)
        elif self.label:
            rv.append(self.label)
        if rv:
            return " - ".join(rv)
        else:
            return "-"

    class Meta:
        verbose_name = _("Catalog Color")
        verbose_name_plural = _("Catalog Colors")
        ordering = ["label", ]
