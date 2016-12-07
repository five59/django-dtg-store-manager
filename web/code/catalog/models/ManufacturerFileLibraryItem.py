from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from .Manufacturer import Manufacturer

class ManufacturerFileLibraryItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)
    hashvalue = models.CharField(_("Hash"), max_length=64, default="", blank=True, null=True)
    url = models.URLField(_("URL"), default="", blank=True, null=True)
    filename = models.CharField(_("Filename"), max_length=128, default="", blank=True, null=True)
    mime_type = models.CharField(_("MIME Type"), max_length=64, default="", blank=True, null=True)
    size = models.IntegerField(_("Size"), default=0)
    width = models.IntegerField(_("Width"), default=0)
    height = models.IntegerField(_("Height"), default=0)
    dpi = models.IntegerField(_("DPI"), default=0)
    status = models.CharField(_("Status"), max_length=12, default="", blank=True, null=True)
    created = models.CharField(_("Created Stamp"), max_length=64, default="", blank=True, null=True)
    thumbnail_url = models.URLField(_("Thumbnail URL"), default="", blank=True, null=True)
    preview_url = models.URLField(_("Preview URL"), default="", blank=True, null=True)
    visible = models.BooleanField(_("Visible?"), default=False)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed File Library Item")
    class Meta:
        verbose_name = _("File Library Item")
        verbose_name_plural = _("File Library Item")
        ordering = ["name","code",]
