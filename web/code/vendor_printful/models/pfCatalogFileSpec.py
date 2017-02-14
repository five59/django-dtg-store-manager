from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfCatalogFileSpec(models.Model):
    COLORSYSTEM_RGB = 'R'
    COLORSYSTEM_CMYK = 'Y'
    COLORSYSTEM_CHOICES = (
        (COLORSYSTEM_RGB, "RGB"),
        (COLORSYSTEM_CMYK, "CMYK"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(_("Name"), max_length=5, default="", blank=True, null=True)
    note = models.TextField(_("Note"), default="", blank=True, null=True)
    width = models.IntegerField(_("Width"), default=0)
    height = models.IntegerField(_("Height"), default=0)

    width_in = models.DecimalField(_("Width (in)"), default=0, decimal_places=2, max_digits=4)
    height_in = models.DecimalField(_("Height (in)"), default=0, decimal_places=2, max_digits=4)

    ratio = models.CharField(_("Ratio"), max_length=32, default="", blank=True, null=True)
    colorsystem = models.CharField(_("Color System"), max_length=1,
                                   default="R", choices=COLORSYSTEM_CHOICES)

    def __str__(self):
        rv = []
        if self.name:
            rv.append(self.name)
        if self.width and self.height:
            rv.append(self.get_dimensions())

        if rv:
            return " - ".join(rv)
        return _("Unnamed Print File")

    def get_dimensions(self, dpi=300):
        return '{}" x {}" @ {}dpi'.format(
            str(int(self.width / dpi * 100) / 100),
            str(int(self.height / dpi * 100) / 100),
            dpi,
        )
    get_dimensions.short_description = _("Dimensions")

    def save(self, *args, **kwargs):
        # Adjust width/heights
        if not self.width and self.width_in:
            self.width = self.width_in * 300
        if not self.width_in and self.width:
            self.width_in = self.width / 300

        if not self.height and self.height_in:
            self.height = self.height_in * 300
        if not self.height_in and self.height:
            self.height_in = self.height / 300

        # Set ratio
        if self.ratio == "":
            if self.width and self.height:
                self.ratio = str(self.width / self.height)
        # Adjust width and height
        super(pfCatalogFileSpec, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("File Spec")
        verbose_name_plural = _("File Specs")
        ordering = ["name", "width", "height", ]
