from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from creative import models as c


class Series(models.Model):
    """ A collection of creative """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    creative_lead = models.ForeignKey(c.Artist, null=True, blank=True,
                                      verbose_name=_("Creative Lead"))
    sales_channel = models.ForeignKey(c.SalesChannel, blank=True, null=True,
                                      verbose_name=_("Sales Channel"))
    note = models.TextField(_("Note"), blank=True, null=True)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Series")

    class Meta:
        verbose_name = _("Series")
        verbose_name_plural = _("Series")
        ordering = ['name', 'code', ]
