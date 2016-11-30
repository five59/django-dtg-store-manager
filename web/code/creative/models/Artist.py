from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
# from creative import models as c


class Artist(models.Model):
    """ A collection of creative """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    location = models.CharField(_("Location"), max_length=255, blank=True, null=True)

    web = models.URLField(_("Web Site"), blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=20, blank=True, null=True)
    email = models.EmailField(_("E-Mail"), blank=True, null=True)

    agreement = models.TextField(_("Agreement Notes"), blank=True, null=True, default="")
    has_agreement = models.BooleanField(_("Agreement in Place?"), default=False)

    notes = models.TextField(_("Notes"), blank=True, null=True, default="")
    description = models.TextField(_("Description"), null=True, blank=True, help_text=_(
        "This will appear in the customer-facing product listing."))

    def num_live(self):
        raise NotImplementedError
    num_live.short_description = "Live"

    def num_assigned(self):
        raise NotImplementedError
    num_assigned.short_description = "Assigned"

    def num_designs(self):
        raise NotImplementedError
    num_designs.short_description = "Total"

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Artist")

    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")
        ordering = ['name', 'code', ]
