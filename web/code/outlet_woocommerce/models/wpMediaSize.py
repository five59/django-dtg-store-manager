from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from timezone_field import TimeZoneField
import uuid


class wpMediaSize(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    file = models.CharField(_("File"), max_length=255, default="", blank=True, null=True)
    mime_type = models.CharField(_("MIME Type"), max_length=255, default="", blank=True, null=True)
    width = models.IntegerField(_("Width"), default=0)
    height = models.IntegerField(_("Height"), default=0)
    source_url = models.URLField(_("Source URL"), default="", blank=True, null=True)

    wpmedia = models.ForeignKey("outlet_woocommerce.wpMedia", verbose_name=_("Media"))

    def __str__(self):
        rv = []
        if self.wpmedia:
            if self.wpmedia.title:
                rv.append(self.wpmedia.title)
        if self.name:
            rv.append(self.name)
        if self.file:
            rv.append(self.file)

        if rv:
            return " - ".join(rv)
        else:
            return _("Unnamed wpMediaSize")

    class Meta:
        verbose_name = _("Media Size")
        verbose_name_plural = _("Media Sizes")
        ordering = ["name", "file", ]
