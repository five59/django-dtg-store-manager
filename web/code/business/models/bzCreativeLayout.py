from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class bzCreativeLayout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=2)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    bzcreativecollection = models.ForeignKey(
        "business.bzCreativeCollection", verbose_name=_("Creative Collection"), )

    def __str__(self):
        rv = []
        if self.code:
            rv.append(self.code)
        if self.name:
            rv.append(self.name)
        if rv:
            return " - ".join(rv)
        else:
            return _("Unnamed Creative Layout")

    class Meta:
        verbose_name = _("Creative Layout")
        verbose_name_plural = _("Creative Layouts")
        ordering = ["code", ]
