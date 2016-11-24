from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from catalog import models as c
# from .Item import Item


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    image_height = models.CharField(blank=True, null=True, default="", max_length=100)
    image_width = models.CharField(blank=True, null=True, default="", max_length=100)
    image = models.ImageField(_("Brand Logo"), upload_to="brand/",
                              blank=True, null=True,
                              height_field='image_height', width_field="image_width")

    consumer_url = models.URLField(_("Consumer URL"), default="", blank=True, null=True)
    wholesale_url = models.URLField(_("Wholesale URL"), default="", blank=True, null=True)

    product_base_url = models.URLField(_("Item URL Base"), default="", blank=True, null=True,
                                       help_text="The URL that points to a specific product ID on the brand's website. Replace the ID with '{}'")

    description = models.TextField(_("Description"), blank=True, default="")

    def num_vendors(self):
        raise NotImplementedError

    def has_logo(self):
        if self.image:
            return True
        return False
    has_logo.boolean = True
    has_logo.short_description = _("Logo?")

    def has_description(self):
        if self.description:
            return True
        return False
    has_description.boolean = True
    has_description.short_description = _("Description?")

    def get_num_products(self):
        return c.Item.objects.filter(brand=self).count()

    def get_products(self):
        return c.Item.objects.filter(brand=self)

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Brand")

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        ordering = ["code", "name", ]
