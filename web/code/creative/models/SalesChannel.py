from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
# from creative import models as c


class SalesChannel(models.Model):
    """ () """
    CATEGORY_UNKNOWN = 'X'
    CATEGORY_WEBSHOP = 'W'
    CATEGORY_MARKETPLACE = 'M'
    CATEGORY_RETAIL = 'R'
    CATEGORY_LICENSE = 'L'
    CATEGORY_CHOICES = (
        (CATEGORY_UNKNOWN, 'Unknown'),
        (CATEGORY_WEBSHOP, 'Web Shop'),
        (CATEGORY_MARKETPLACE, 'Marketplace'),
        (CATEGORY_RETAIL, 'Retail'),
        (CATEGORY_LICENSE, 'License'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    web_url = models.URLField(_("URL"), blank=True, null=True)
    category = models.CharField(_("Category"), max_length=1, blank=True,
                                default=CATEGORY_UNKNOWN, choices=CATEGORY_CHOICES)
    description = models.TextField(_("Description"), blank=True, default="")

    logo_hires_height = models.IntegerField(default=0)
    logo_hires_width = models.IntegerField(default=0)
    logo_hires = models.ImageField(_("Press-Ready Logo"), height_field="logo_hires_height",
                                   width_field="logo_hires_width", blank=True, null=True)

    def has_hires_logo(self):
        if self.logo_hires:
            return True
        return False
    has_hires_logo.boolean = True
    has_hires_logo.short_description = _("Has High Res Logo?")

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Outlet")

    class Meta:
        verbose_name = _("Sales Channel")
        verbose_name_plural = _("Sales Channels")
        ordering = ['name', 'code', ]
