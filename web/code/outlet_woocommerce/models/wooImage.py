from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from timezone_field import TimeZoneField
import uuid


class wooImage(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    wid = models.CharField(_("Woo ID"), max_length=16, default="",
                           blank=True, null=True, help_text=_("Image ID (attachment ID). In write-mode used to attach pre-existing images."))
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    date_created = models.DateField(_("Date Created"), help_text=_(
        "READONLY. The date the product was created, in the site’s timezone."), blank=True, null=True)
    date_modified = models.DateField(_("Date Modified"), help_text=_(
        "READONLY. The date the product was last modified, in the site’s timezone."), blank=True, null=True)
    src = models.URLField(_("Source"), blank=True, null=True, help_text=_(
        "Image URL. In write-mode used to upload new images."))
    alt = models.CharField(_("Alt"), max_length=255, default="", blank=True, null=True)
    position = models.IntegerField(_("Position"), default=0, help_text=_(
        "Image position. 0 means that the image is featured."))

    def __str__(self):
        if self.wid and self.name:
            return "{} - {}".format(self.wid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed wooImage")

    class Meta:
        verbose_name = _("Image Association")
        verbose_name_plural = _("Image Associations")
        ordering = ["name", "wid", ]
