from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog.models.Brand import Brand
from colour import Color as libColor


class Color(models.Model):
    PMSFAM_UNCOATED = 'U'
    PMSFAM_COATED = 'C'
    PMSFAM_METALLIC = 'M'
    PMSFAM_NEON = 'N'
    PMSFAM_TPX = "X"
    PMSFAM_UNKNOWN = "Z"
    PMSFAM_CHOICES = (
        (PMSFAM_UNCOATED, 'Uncoated'),
        (PMSFAM_COATED, 'Coated'),
        (PMSFAM_METALLIC, 'Metallic'),
        (PMSFAM_NEON, 'Neon'),
        (PMSFAM_TPX, "TPX"),
        (PMSFAM_UNKNOWN, "Unknown"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=64, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    # slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    brand = models.ForeignKey(Brand, verbose_name=_("Brand"), blank=True, null=True)

    pms_code = models.CharField(_("PMS Code"), max_length=64, default="", blank=True, null=True)
    pms_family = models.CharField(_("PMS Family"), max_length=1,
                                  default=PMSFAM_UNKNOWN, blank=True, null=True, choices=PMSFAM_CHOICES)

    color_string = models.CharField(_("Color String"), max_length=64, default="", blank=True, null=True,
                                    help_text=_("Temporary string for inputting a color value. On save, it is transformed into the various color values automagically."))

    hex_code = models.CharField(_("HEX Code"), max_length=64, default="", blank=True, null=True,
                                help_text="The 6-digit hexidecimal code for this colour. Do not include the hash tag.")

    r_value = models.IntegerField(_("Red Value"), default=0, help_text="Scale of 0-255")
    g_value = models.IntegerField(_("Green Value"), default=0, help_text="Scale of 0-255")
    b_value = models.IntegerField(_("Blue Value"), default=0, help_text="Scale of 0-255")

    c_value = models.IntegerField(_("Cyan Value"), default=0, help_text="Scale of 0-100")
    m_value = models.IntegerField(_("Magenta Value"), default=0, help_text="Scale of 0-100")
    y_value = models.IntegerField(_("Yellow Value"), default=0, help_text="Scale of 0-100")
    k_value = models.IntegerField(_("Black Value"), default=0, help_text="Scale of 0-100")

    def show_vals(self):
        print("=================\nRGB: {} {} {} \nCMYK: {} {} {} {}\nHEX: {}\n".format(
            self.r_value, self.g_value, self.b_value,
            self.c_value, self.m_value, self.y_value, self.k_value,
            self.hex_code,
        ))

    def cmyk_to_rgb(self):
        print("--> CMYK_TO_RGB")
        cmyk = (
            self.c_value / 100,
            self.m_value / 100,
            self.y_value / 100,
            self.k_value / 100
        )
        rgb = (
            int(255 * (1 - cmyk[0]) * (1 - cmyk[3])),
            int(255 * (1 - cmyk[1]) * (1 - cmyk[3])),
            int(255 * (1 - cmyk[2]) * (1 - cmyk[3])),
        )
        self.r_value, self.g_value, self.b_value = rgb
        self.show_vals()

    def rgb_to_cmyk(self):
        print("--> RGB_TO_CMYK")

        r = self.r_value / 255
        g = self.g_value / 255
        b = self.b_value / 255

        k = 1 - max(r, g, b)
        c = int((1 - r - k) / (1 - k) * 100)
        m = int((1 - g - k) / (1 - k) * 100)
        y = int((1 - b - k) / (1 - k) * 100)
        self.c_value, self.m_value, self.y_value, self.k_value = c, m, y, k
        self.show_vals()

    def transcode_color(self):
        if not self.color_string:
            return

        # Clear out values:
        self.r_value, self.g_value, self.b_value,
        self.c_value, self.m_value, self.y_value, self.k_value,
        self.hex_code = None

        elementCount = len(self.color_string.split(","))

        # Do we have a HEX Code?
        if self.color_string[:1] == "#":
            print("--> Saw Hex Code")
            self.hex_code = self.color_string[1:]
            tmpColor = libColor(self.color_string)
            rgb = tmpColor.get_rgb()
            self.r_value, self.g_value, self.b_value = rgb[0] * 255, rgb[1] * 255, rgb[2] * 255
            self.rgb_to_cmyk()

        # Do we have an RGB Code?
        elif elementCount == 3:
            print("--> Saw RGB Code")
            colorArray = list(map(int, self.color_string.split(",")))
            self.r_value, self.g_value, self.b_value = colorArray
            self.rgb_to_cmyk()
            imgColor = libColor(rgb=(self.r_value / 255, self.g_value / 255, self.b_value / 255))
            self.hex_code = imgColor.get_hex()[1:]

        # Do we have a CMYK Code?
        elif elementCount == 4:
            colorArray = list(map(int, self.color_string.split(",")))
            self.c_value, self.m_value, self.y_value, self.k_value = colorArray
            self.cmyk_to_rgb()
            imgColor = libColor(rgb=(self.r_value / 255, self.g_value / 255, self.b_value / 255))
            self.hex_code = imgColor.get_hex()[1:]

        else:
            pass  # Do we need error handling here?

        # Now we can clear out the temporary field.
        self.color_string = None

    def get_rgb_str(self):
        return "({0:0>3},{1:0>3},{2:0>3})".format(self.r_value, self.g_value, self.b_value)
    get_rgb_str.short_description = _("RGB")

    def get_cmyk_str(self):
        return "({0:0>3},{1:0>3},{2:0>3},{3:0>3})".format(self.c_value, self.m_value, self.y_value, self.k_value)
    get_cmyk_str.short_description = _("CMYK")

    def save(self, *args, **kwargs):
        self.transcode_color()
        if not self.name:
            self.name = _("Unnamed Color")
        if self.name == "":
            self.name = _("Unnamed Color")
        super(Color, self).save(*args, **kwargs)

    def __str__(self):
        return "".join([
            "{} / ".format(self.code) if self.code else "",
            str(self.name),
        ])

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")
        ordering = ['code', ]
        unique_together = (("code", "brand"),)
