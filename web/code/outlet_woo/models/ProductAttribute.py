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


class ProductAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), help_text=_(""), max_length=16,
                            default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)
    has_archives = models.BooleanField(_("Has Archives?"), default=False)
    input_type = models.CharField(_("Type"), max_length=32, default="text", blank=True, null=True)
    order_by = models.CharField(_("Order By"), max_length=64, default="", blank=True, null=True)
    shop = models.ForeignKey(wc.Shop, blank=True, null=True)
    app_added = models.DateTimeField(auto_now_add=True, help_text=_(""))
    app_last_sync = models.DateTimeField(auto_now=True, help_text=_(""))

    def exists_on_server(self):
        if self.code:
            return True
        return False
    exists_on_server.boolean = True

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        if self.code:
            return "{}".format(self.code)
        return _("Unnamed Product Attribute")

    class Meta:
        verbose_name = _("Product Attribute")
        verbose_name_plural = _("Product Attributes")
        ordering = ["name", "code", ]
