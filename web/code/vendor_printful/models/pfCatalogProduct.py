from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from .pfCatalogVariant import pfCatalogVariant
from .pfCatalogFileType import pfCatalogFileType
from .pfCatalogOptionType import pfCatalogOptionType
from .pfCatalogColor import pfCatalogColor
from .pfCatalogSize import pfCatalogSize


class pfCatalogProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    pid = models.CharField(_("Printful ID"), max_length=255, default="", blank=True, null=True)

    type = models.CharField(_("Type"), max_length=255, default="", blank=True, null=True)
    brand = models.CharField(_("Brand"), max_length=255, default="", blank=True, null=True)
    model = models.CharField(_("Model"), max_length=255, default="", blank=True, null=True)
    image = models.CharField(_("Image"), max_length=255, default="", blank=True, null=True)
    variant_count = models.IntegerField(_("Variants"), default=0)

    def __str__(self):
        if self.pid and self.brand and self.model:
            return "{} - {} ({})".format(self.brand, self.model, self.pid, )
        if self.model:
            return "{}".format(self.model)
        return _("Unnamed Catalog Product")

    class Meta:
        verbose_name = _("Catalog Product")
        verbose_name_plural = _("Catalog Products")
        ordering = ["brand", "model", "pid", ]

    def get_variants(self):
        return pfCatalogVariant.objects.filter(pfcatalogproduct=self)
    get_variants.short_description = _("Variants")

    def get_colors(self):
        # Get all color objects associated with this product's variants.
        # return pfCatalogColor.objects.filter()
        return pfCatalogColor.objects.filter(pfcatalogvariant__in=self.get_variants()).distinct()
    get_colors.short_description = _("Colors")

    def get_colors_as_string(self):
        c = self.get_colors()
        if c:
            rv = ", ".join([v.label for v in c])
        else:
            rv = "-"
        return rv
    get_colors_as_string.short_description = _("Available Colors")

    def num_colors(self):
        return self.get_colors().count()
    num_colors.short_description = _("Colors")

    def get_sizes(self):
        return pfCatalogSize.objects.filter(pfcatalogvariant__in=self.get_variants()).distinct()
    get_sizes.short_description = _("Sizes")

    def get_sizes_as_string(self):
        s = self.get_sizes()
        if s:
            rv = ", ".join([v.get_name() for v in s])
        else:
            rv = "-"
        return rv
    get_sizes_as_string.short_description = _("Available Sizes")

    def num_sizes(self):
        return self.get_sizes().count()
    num_sizes.short_description = _("Sizes")

    def get_out_of_stock(self):
        return pfCatalogVariant.objects.filter(pfcatalogproduct=self, in_stock=False)

    def num_out_of_stock(self):
        return self.get_out_of_stock().count()
    num_out_of_stock.short_description = _("Out of Stock")
