from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from timezone_field import TimeZoneField
import uuid

class wooImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    def __str__(self):
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed wooImage")
    class Meta:
        verbose_name = _("wooImage")
        verbose_name_plural = _("wooImage")
        ordering = ["name","code",]
