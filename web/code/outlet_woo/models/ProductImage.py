from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
import uuid
from datetime import datetime
from creative import models as cr
from catalog import models as ca
from outlet_woo import models as wc


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), help_text=_(
        "Image ID (attachment ID). In write-mode used to attach pre-existing images."), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    product = models.ForeignKey(wc.Product, blank=True, null=True)

    app_added = models.DateTimeField(auto_now_add=True, help_text=_(""))
    app_last_sync = models.DateTimeField(auto_now=True, help_text=_(""))
    date_created = models.DateTimeField(_("Created"), help_text=_(
        "READONLY. The date the product was created. In the site's timezone."), blank=True, null=True)
    date_modified = models.DateTimeField(_("Modified"), help_text=_(
        "READONLY. The date the product was last modified, in the site's timezone."), blank=True, null=True)

    src = models.URLField(_("Image URL"), help_text=_("In write-mode used to upload new images."))
    alt = models.CharField(_("Alternative Text"), max_length=255, default="", blank=True, null=True)
    position = models.IntegerField(_("Image Position"), help_text=_(
        "0 means that the image is featured."), default=1)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed ProductImage")

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        ordering = ["name", "code", ]
