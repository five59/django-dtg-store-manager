from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfState(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=50, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    pfcountry = models.ForeignKey("vendor_printful.pfCountry", verbose_name=_("Country"))

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed State")

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")
        ordering = ["name", "code", ]
