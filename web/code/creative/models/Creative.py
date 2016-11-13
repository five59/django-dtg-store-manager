from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from .Artist import Artist
from .Series import Series


class Creative(models.Model):
    """ () """
    STATUS_NEW = "N"
    STATUS_INDEV = "V"
    STATUS_LIVE = "L"
    STATUS_DEFERRED = "D"
    STATUS_CHOICES = (
        (STATUS_NEW, "New"),
        (STATUS_INDEV, "In Development"),
        (STATUS_LIVE, "Live"),
        (STATUS_DEFERRED, "Deferred"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    series = models.ForeignKey(Series, null=True, blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=True)
    status = models.CharField(_("Status"), choices=STATUS_CHOICES, max_length=1,
                              default=STATUS_NEW, null=True, blank=True)
    note = models.TextField(_("Note"), null=True, blank=True)

    def status_tag(self):
        # return self.status
        STATUS_COLORS = {
            self.STATUS_NEW: '#CC3333',
            self.STATUS_INDEV: '#cc9933',
            self.STATUS_LIVE: '#009900',
            self.STATUS_DEFERRED: '#999999',
        }
        rv = "<div style='text-align: center; padding: 2px; color:#ffffff; background-color:{};'>{}</div>".format(
            STATUS_COLORS[self.status], self.get_status_display())
        return rv
    status_tag.short_description = "Status"
    status_tag.allow_tags = True

    def __str__(self):
        rv = ""
        try:
            if self.series.code:
                rv = "{}-".format(self.series.code)
            else:
                rv = "000-"
        except:
            pass
        if self.code:
            rv = "{}{} / ".format(rv, self.code)
        else:
            rv = "".join([rv, "00"])
        if self.name:
            return "{}{}".format(rv, self.name)
        return _("Unnamed Creative")

    class Meta:
        verbose_name = _("Creative")
        verbose_name_plural = _("Creative")
        ordering = ['series__code', 'code', 'name', ]
        # ordering = ['name', 'code', ]
