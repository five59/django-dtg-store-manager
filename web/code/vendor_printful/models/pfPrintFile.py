from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from business.models.bzCreativeCollection import bzCreativeCollection
from business.models.bzCreativeDesign import bzCreativeDesign
from business.models.bzCreativeLayout import bzCreativeLayout
from business.models.bzCreativeRendering import bzCreativeRendering
from vendor_printful.models.pfCatalogFileSpec import pfCatalogFileSpec


class pfPrintFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    pid = models.IntegerField(_("Printful ID"), default=0)
    type = models.CharField(_("Type"), max_length=255, default="", blank=True, null=True)
    hash = models.CharField(_("Hash"), max_length=255, default="", blank=True, null=True)
    url = models.CharField(_("URL"), max_length=255, default="", blank=True, null=True)
    filename = models.CharField(_("Filename"), max_length=255, default="", blank=True, null=True)
    mime_type = models.CharField(_("MIME Type"), max_length=255, default="", blank=True, null=True)
    size = models.IntegerField(_("Size"), default=0)
    width = models.IntegerField(_("Width"), default=0)
    height = models.IntegerField(_("Height"), default=0)
    dpi = models.IntegerField(_("DPI"), default=0)
    status = models.CharField(_("Status"), max_length=255, default="", blank=True, null=True)
    created = models.CharField(_("Created"), max_length=255, default="", blank=True, null=True)
    thumbnail_url = models.CharField(
        _("Thumbnail URL"), max_length=255, default="", blank=True, null=True)
    preview_url = models.CharField(_("Preview URL"), max_length=255,
                                   default="", blank=True, null=True)
    visible = models.BooleanField(_("Visible"), default=False)

    pfstore = models.ForeignKey("vendor_printful.pfStore",
                                verbose_name=_("Store"), blank=True, null=True)
    pfcatalogfilespec = models.ForeignKey(
        "vendor_printful.pfCatalogFileSpec", on_delete=models.SET_NULL,
        verbose_name=_("File Spec"), blank=True, null=True)

    def get_dimensions(self, dpi=300):
        return '{}" x {}" @ {}dpi'.format(
            str(int(self.width / dpi * 100) / 100),
            str(int(self.height / dpi * 100) / 100),
            dpi,
        )
    get_dimensions.short_description = _("Dimensions")

    def get_thumb_html(self):
        if self.thumbnail_url:
            rv = "<img src='{}' style='border: 1px solid #ccc;' />".format(self.thumbnail_url)
        else:
            rv = ""
        return rv
    get_thumb_html.short_description = "Thumbnail"
    get_thumb_html.allow_tags = True

    def clean_all(blank_only=True):
        if blank_only:
            pCollection = pfPrintFile.objects.filter(pfcatalogfilespec=None)
        else:
            pCollection = pfPrintFile.objects.all()

        print("- Loose spec matching...")
        for p in pCollection:
            try:
                p.pfcatalogfilespec = pfCatalogFileSpec.objects.get(width=p.width, height=p.height)
                p.save()
            except Exception as e:
                print("-- Whoops: {}".format(e))

        print("- Loose rendering matching...")
        for p in pCollection:
            try:
                if len(p.filename) == 14:
                    # Match codes
                    objCollection = bzCreativeCollection.objects.get(code=p.filename[0:3])
                    objFileSpec = pfCatalogFileSpec.objects.get(name=p.filename[4:6])
                    objLayout = bzCreativeLayout.objects.get(code=p.filename[6:7])
                    objDesign = bzCreativeDesign.objects.get(code=p.filename[8:10])
                    obj, created = bzCreativeRendering.objects.update_or_create(
                        bzcreativedesign=objDesign,
                        bzcreativelayout=objLayout,
                        pfcatalogfilespec=objFileSpec,
                        pfprintfile=p,
                        defaults={}
                    )
                    print("{} {}".format(
                        "Created" if created else "Updated",
                        obj,
                    ))
                else:
                    print("-- Whoops: {} is the wrong length.".format(p.filename))
            except Exception as e:
                print("-- Whoops: {}".format(e))

    def __str__(self):
        if self.pid and self.filename:
            return "{} - {}".format(self.pid, self.filename)
        if self.filename:
            return "{}".format(self.filename)
        return _("Unnamed Print File")

    class Meta:
        verbose_name = _("Print File")
        verbose_name_plural = _("Print Files")
        ordering = ["pid", "type", ]
