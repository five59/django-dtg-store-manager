from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
from .pfState import pfState
import uuid


class pfCountry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=50, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Country")

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ["name", "code", ]

    def get_states(self):
        return pfState.objects.filter(pfcountry=self)
    get_states.short_description = _("States")

    def num_states(self):
        return self.get_states().count()
    num_states.short_description = _("State Count")
