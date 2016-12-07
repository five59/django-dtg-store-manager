from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog import models as c
from django.db.models import Avg, Max, Min
import locale
import requests
import urllib
import tempfile
from django.core import files
import os
from .ManufacturerItem import ManufacturerItem


class ManufacturerItemDimension(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    manufacturer_item = models.ForeignKey(ManufacturerItem, null=True, blank=True)
    is_active = models.BooleanField(_("Is Active?"), default=False, blank=True)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Manufacturer Item Dimension")

    class Meta:
        verbose_name = _("Manufacturer Item Dimension")
        verbose_name_plural = _("Manufacturer Item Dimension")
        ordering = ["name", "code", ]
