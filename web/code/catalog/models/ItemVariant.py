from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from .Item import Item
from .Color import Color
from .Size import Size


class ItemVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    product = models.ForeignKey(Item, null=True, blank=True)

    name = models.CharField(_("Name"), max_length=150, default="",
                            blank=True, null=True, help_text="")

    image_url = models.URLField(_("Image URL"), null=True, blank=True)

    image_height = models.CharField(_("Image Height"), default="0", max_length=10)
    image_width = models.CharField(_("Image Width"), default="0", max_length=10)
    image = models.ImageField(_("Item Image"), upload_to="product",
                              height_field="image_height", width_field="image_width", blank=True, null=True, help_text="")
    link = models.URLField(_("Item URL"), default="", blank=True, null=True, help_text="")

    color = models.ForeignKey(Color, blank=True, null=True)
    size = models.ForeignKey(Size, blank=True, null=True)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Item Variant")

    class Meta:
        verbose_name = _("Item Variant")
        verbose_name_plural = _("Item Variants")
        ordering = ["name", "code", ]
