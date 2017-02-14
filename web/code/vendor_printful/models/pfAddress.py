from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    pid = models.CharField(_("Printful ID"), max_length=255, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    company = models.CharField(_("Company"), max_length=255, default="", blank=True, null=True)
    address1 = models.CharField(_("Address 1"), max_length=255, default="", blank=True, null=True)
    address2 = models.CharField(_("Address 2"), max_length=255, default="", blank=True, null=True)
    city = models.CharField(_("City"), max_length=255, default="", blank=True, null=True)
    state = models.ForeignKey("vendor_printful.pfState")
    zip = models.CharField(_("Zip Code"), max_length=100, default="", blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=20, default="", blank=True, null=True)
    email = models.CharField(_("E-Mail"), max_length=255, default="", blank=True, null=True)

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Address")

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        ordering = ["name", ]
