import uuid
import requests
import urllib
import os
import tempfile
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files
from creative import models as cr
from catalog import models as ca
from outlet_woo import models as wc

class ProductAttributeTerm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)
    description = models.TextField(_("Description"), default="", blank=True)
    menu_order = models.IntegerField(_("Menu Order"), default=0)
    count = models.IntegerField(_("Count (RO)"), default=0)
    productattribute = models.ForeignKey(wc.ProductAttribute, blank=True, null=True)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Product Attribute Term")
    class Meta:
        verbose_name = _("Product Attribute Term")
        verbose_name_plural = _("Product Attribute Terms")
        ordering = ["name","code",]
