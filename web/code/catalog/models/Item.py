from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
# from .Brand import Brand
# from .Category import Category
# from .GoogleCategory import GoogleCategory
from catalog import models as c


class Item(models.Model):
    AGEGROUP_NEWBORN = 'N'
    AGEGROUP_INFANT = 'I'
    AGEGROUP_TODDLER = 'T'
    AGEGROUP_KIDS = 'K'
    AGEGROUP_ADULT = 'A'
    AGEGROUP_CHOICES = (
        (AGEGROUP_NEWBORN, 'Newborn'),
        (AGEGROUP_INFANT, 'Infant'),
        (AGEGROUP_TODDLER, 'Toddler'),
        (AGEGROUP_KIDS, 'Kids'),
        (AGEGROUP_ADULT, 'Adult'),
    )
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_UNISEX = "U"
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_UNISEX, 'Unisex'),
    )
    SIZETYPE_NONE = "N"
    SIZETYPE_REGULAR = "R"
    SIZETYPE_PETITE = "T"
    SIZETYPE_PLUS = "L"
    SIZETYPE_BIGANDTALL = "B"
    SIZETYPE_MATERNITY = "M"
    SIZETYPE_CHOICES = (
        (SIZETYPE_NONE, 'None'),
        (SIZETYPE_REGULAR, 'Regular'),
        (SIZETYPE_PETITE, 'Petite'),
        (SIZETYPE_PLUS, 'Plus'),
        (SIZETYPE_BIGANDTALL, 'Big and Tall'),
        (SIZETYPE_MATERNITY, 'Maternity'),
    )
    SIZESYSTEM_US = 'US'
    SIZESYSTEM_UK = 'UK'
    SIZESYSTEM_EU = 'EU'
    SIZESYSTEM_DE = 'DE'
    SIZESYSTEM_FR = 'FR'
    SIZESYSTEM_JP = 'JP'
    SIZESYSTEM_CN = 'CN'
    SIZESYSTEM_IT = 'IT'
    SIZESYSTEM_BR = 'BR'
    SIZESYSTEM_MEX = 'MEX'
    SIZESYSTEM_AU = 'AU'
    SIZESYSTEM_CHOICES = (
        (SIZESYSTEM_US, 'US - United States'),
        (SIZESYSTEM_UK, 'UK - United Kingdom'),
        (SIZESYSTEM_EU, 'EU - European Union'),
        (SIZESYSTEM_DE, 'DE - Germany'),
        (SIZESYSTEM_FR, 'FR - France'),
        (SIZESYSTEM_JP, 'JP - Japan'),
        (SIZESYSTEM_CN, 'CN - China'),
        (SIZESYSTEM_IT, 'IT - Italy'),
        (SIZESYSTEM_BR, 'BR - Brazil'),
        (SIZESYSTEM_MEX, 'MEX - Mexico'),
        (SIZESYSTEM_AU, 'AU - Australia'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=64, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    brand = models.ForeignKey(c.Brand, blank=True, null=True)
    category = models.ForeignKey(c.Category, blank=True, null=True)
    googlecategory = TreeForeignKey(c.GoogleCategory, verbose_name=_(
        "Google Category"), blank=True, null=True)

    age_group = models.CharField(_("Age Group"), max_length=1,
                                 default=AGEGROUP_ADULT, blank=False, choices=AGEGROUP_CHOICES)
    gender = models.CharField(_("Gender"), max_length=1,
                              default=GENDER_UNISEX, blank=False, choices=GENDER_CHOICES)
    material = models.CharField(_("Material"), max_length=200, default="",
                                blank=True, null=True, help_text="")
    pattern = models.CharField(_("Pattern"), max_length=100, default="",
                               blank=True, null=True, help_text="")
    size_type = models.CharField(_("Size Type"), max_length=1,
                                 default=SIZETYPE_REGULAR, blank=True, choices=SIZETYPE_CHOICES)
    size_system = models.CharField(_("Size System"), max_length=3,
                                   default=SIZESYSTEM_US, blank=False, choices=SIZESYSTEM_CHOICES)

    description = models.TextField(_("Description"), default="",
                                   blank=True, null=True, help_text="")

    link = models.URLField(_("Item URL"), default="", blank=True, null=True, help_text="")
    mobile_link = models.URLField(_("Mobile URL"), default="", blank=True, null=True, help_text="")

    image_height = models.CharField(_("Image Height"), default="0", max_length=10)
    image_width = models.CharField(_("Image Width"), default="0", max_length=10)
    image = models.ImageField(_("Item Image"), upload_to="product",
                              height_field="image_height", width_field="image_width", blank=True, null=True, help_text="")

    additional_image_height = models.CharField(
        _("Additional Image Height"), default="0", max_length=10)
    additional_image_width = models.CharField(
        _("Additional Image Width"), default="0", max_length=10)
    additional_image = models.ImageField(_("Additional Image"),  upload_to="product_additional",
                                         height_field="additional_image_height", width_field="additional_image_width",
                                         blank=True, null=True, help_text="")

    def num_vendors(self):
        return c.ManufacturerItem.objects.filter(item=self).count()
    num_vendors.short_description = "Vendors"

    def __str__(self):
        rv = [
            self.brand.code if self.brand else "ZZ",
            self.code if self.code else "0000",
            " / ",
            self.name if self.name else _("Unnamed Item")
        ]
        return "".join(rv)

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        ordering = ["brand__code", "code", "name", ]
