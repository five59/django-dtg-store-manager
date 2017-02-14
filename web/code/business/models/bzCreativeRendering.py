from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class bzCreativeRendering(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    bzcreativedesign = models.ForeignKey("business.bzCreativeDesign", verbose_name=_("Design"))
    bzcreativelayout = models.ForeignKey("business.bzCreativeLayout", verbose_name=_("Layout"),  on_delete=models.SET_NULL,
                                         blank=True, null=True, )
    pfcatalogfilespec = models.ForeignKey(
        'vendor_printful.pfCatalogFileSpec', verbose_name=_("Spec"),  on_delete=models.SET_NULL, blank=True, null=True)
    pfprintfile = models.ForeignKey("vendor_printful.pfPrintFile", verbose_name=_("Print File"),  on_delete=models.SET_NULL,
                                    blank=True, null=True, )

    def __str__(self):
        rv = []
        if self.bzcreativedesign:
            rv.append(self.bzcreativedesign.code)
        if self.bzcreativelayout:
            rv.append(self.bzcreativelayout.code)
        if self.pfcatalogfilespec:
            rv.append(self.pfcatalogfilespec.name)
        if rv:
            return "-".join(rv)
        else:
            return _("Unnamed Creative Rendering")

    class Meta:
        verbose_name = _("Creative Rendering")
        verbose_name_plural = _("Creative Renderings")
        # ordering = ["code", ]
