from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django_extensions.db import fields as extension_fields
import uuid
from creative import models as cr
from catalog import models as ca


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    creative = models.ForeignKey(cr.Creative, verbose_name=_("Creative"), blank=True, null=True)
    item = models.ForeignKey(ca.Item, verbose_name=_("Item"), blank=True, null=True)
    sales_channel = models.ForeignKey(
        cr.SalesChannel, verbose_name=_("Sales Channel"), null=True, blank=True)

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Product")

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Product")
        ordering = ["name", "code", ]
