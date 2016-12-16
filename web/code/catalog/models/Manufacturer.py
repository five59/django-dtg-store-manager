from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
# from catalog import models as c


class Manufacturer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    consumer_url = models.URLField(_("Consumer URL"), blank=True, null=True)
    dashboard_url = models.URLField(_("Admin Dashboard URL"), blank=True, null=True)
    apibase_url = models.URLField(_("API Base URL"), blank=True, null=True)

    api_key = models.CharField(_("API Key"), max_length=64, default="", blank=True)
    api_hash = models.CharField(_("API Hash"), max_length=96, default="", blank=True)
    api_key_base64 = models.CharField(_("Base64 Key"), max_length=64, default="", blank=True)

    notes = models.TextField(_("Notes"), default="", blank=True, null=True)

    def has_key(self):
        if self.api_key:
            return True
        return False
    has_key.short_description = 'Has API Key?'
    has_key.boolean = True

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Manufacturer")

    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")
        ordering = ['name', 'code', ]
