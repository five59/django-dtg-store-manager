from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
# from .Item import Item
from catalog import models as c


class Category(MPTTModel):
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def num_products(self):
        return c.Item.objects.filter(category=self).count()

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Category")

    def num_items(self):
        return c.Item.objects.filter(category=self).count()
    num_items.short_description = "Items"

    def get_items(self):
        return c.Item.objects.filter(category=self)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['name', 'code', ]

    class MPTTMeta:
        order_insertion_by = ['name', ]
