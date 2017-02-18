import uuid
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files


class wooVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    wid = models.CharField(_("Woo ID"), max_length=64, default="",
                           blank=True, null=True, )
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    date_created = models.DateField(_("Date Created"), help_text=_(
        "READONLY. The date the product was created, in the site’s timezone."), blank=True, null=True)
    date_modified = models.DateField(_("Date Modified"), help_text=_(
        "READONLY. The date the product was last modified, in the site’s timezone."), blank=True, null=True)

    permalink = models.URLField(_("Permalink"), blank=True)
    sku = models.CharField(_("SKU"), help_text=_("Unique identifier."), max_length=255,
                           default="", blank=True, null=True)

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
