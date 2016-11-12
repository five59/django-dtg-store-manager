from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django_extensions.db import fields as extension_fields
import uuid
from creative.models import *
from catalog.models import *
from .Product import Product


class Variant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    color = models.ForeignKey(Color, null=True, blank=True)
    size = models.ForeignKey(Size, null=True, blank=True)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Variant")

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variant")
        ordering = ["code", "product", ]
