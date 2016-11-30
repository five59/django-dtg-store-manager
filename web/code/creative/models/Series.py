from django.db import models
from django.utils.translation import ugettext as _
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
    description = models.TextField(_("Description"), null=True, blank=True, help_text=_(
        "This will appear in the customer-facing product listing."))

    def get_designs(self):
        return c.Design.objects.filter(series=self)

    def num_designs(self):
        return c.Design.objects.filter(series=self).count()
    num_designs.short_description = 'Designs'

    def percent_designs_live(self):
        total_designs = c.Design.objects.filter(series=self).count()
        if total_designs == 0:
            percent = 0
        else:
            live_designs = c.Design.objects.filter(series=self, status=c.Design.STATUS_LIVE).count()
            percent = live_designs / total_designs * 100
        if percent == 100:
            return "100%"
        return "{:.2f}%".format(percent)
    percent_designs_live.short_description = "Percent Live"

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Series")

    class Meta:
        verbose_name = _("Series")
        verbose_name_plural = _("Series")
        ordering = ['name', 'code', ]
