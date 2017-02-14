from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class bzCreativeCollection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=3)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    bzbrand = models.ForeignKey("business.bzBrand", verbose_name=_("Brand"), null=True, blank=True)

    def __str__(self):
        rv = []
        if self.code:
            rv.append(self.code)
        if self.name:
            rv.append(self.name)
        if rv:
            return " - ".join(rv)
        else:
            return _("Unnamed Creative Collection")

    class Meta:
        verbose_name = _("Creative Collection")
        verbose_name_plural = _("Creative Collections")
        ordering = ["code", ]
