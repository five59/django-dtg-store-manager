from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
# from catalog import models as c


class Color(models.Model):
    PMSFAM_UNCOATED = 'U'
    PMSFAM_COATED = 'C'
    PMSFAM_METALLIC = 'M'
    PMSFAM_NEON = 'N'
    PMSFAM_CHOICES = (
        (PMSFAM_UNCOATED, 'Uncoated'),
        (PMSFAM_COATED, 'Coated'),
        (PMSFAM_METALLIC, 'Metallic'),
        (PMSFAM_NEON, 'Neon'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=64, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    pms_code = models.CharField(_("PMS Code"), max_length=64, default="", blank=True, null=True)
    pms_family = models.CharField(_("PMS Family"), max_length=1,
                                  default="", blank=True, null=True, choices=PMSFAM_CHOICES)
    hex_code = models.CharField(_("HEX Code"), max_length=64, default="", blank=True, null=True,
                                help_text="The 6-digit hexidecimal code for this colour. Do not include the hash tag.")
    r_value = models.IntegerField(_("Red Value"), default=0, help_text="Scale of 0-255")
    g_value = models.IntegerField(_("Green Value"), default=0, help_text="Scale of 0-255")
    b_value = models.IntegerField(_("Blue Value"), default=0, help_text="Scale of 0-255")

    def save(self, *args, **kwargs):
        _NUMERALS = '0123456789abcdefABCDEF'
        _HEXDEC = {v: int(v, 16) for v in (x + y for x in _NUMERALS for y in _NUMERALS)}
        LOWERCASE, UPPERCASE = 'x', 'X'

        def rgb(triplet):
            return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]

        def triplet(rgb, lettercase=LOWERCASE):
            return format(rgb[0] << 16 | rgb[1] << 8 | rgb[2], '06' + lettercase)

        if self.hex_code:
            try:
                self.r_value, self.g_value, self.b_value = rgb(self.hex_code)
            except:
                self.r_value, self.g_value, self.b_value = [0, 0, 0]

        super(Color, self).save(*args, **kwargs)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Color")

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")
        ordering = ['name', 'code', ]
