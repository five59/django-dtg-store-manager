import uuid
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files


class wooVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wid = models.CharField(_("Woo ID"), max_length=64, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)
    description = models.TextField(_("Description"), default="", blank=True, null=True)
    count = models.IntegerField(_("Count"), default=0)

    def __str__(self):
        if self.wid and self.name:
            return "{} - {}".format(self.wid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed wooVariant")

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")
        ordering = ["name", "wid", ]
