from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from creative import models as c
from outlet_woo import models as wm


class Design(models.Model):
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
    series = models.ForeignKey('creative.Series', null=True, blank=True)
    artist = models.ForeignKey('creative.Artist', null=True, blank=True)
    status = models.CharField(_("Status"), choices=STATUS_CHOICES, max_length=1,
                              default=STATUS_NEW, null=True, blank=True)
    note = models.TextField(_("Note"), null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True, help_text=_(
        "This will appear in the customer-facing product listing."))

    reference_url = models.URLField(_("Reference URL"), null=True, blank=True)
    reference_note = models.CharField(_("Reference Note"), null=True, blank=True, max_length=4000)

    def status_tag(self):
        # return self.status
        STATUS_COLORS = {
            self.STATUS_NEW: '#CC3333',
            self.STATUS_INDEV: '#cc9933',
            self.STATUS_LIVE: '#009900',
            self.STATUS_DEFERRED: '#999999',
        }
        rv = "<div style='text-align: center; padding: 2px; color:#ffffff; font-size: 0.75em; background-color:{};'>{}</div>".format(
            STATUS_COLORS[self.status], self.get_status_display())
        return rv
    status_tag.short_description = "Status"
    status_tag.allow_tags = True

    # def get_product_images(self):
    #     from outlet_woo.models import Product as WooProduct
    #     from outlet_woo.models import ProductImage as WooProductImage
    #     woo = WooProductImages.objects.filter(product=WooProduct.objects.filter(design=self))
    #     return woo

    def get_an_image(self):
        from outlet_woo.models import Product as WooProduct
        try:
            woo = WooProduct.objects.filter(design=self)[0]
            return woo.get_images()[0].image
        except:
            return None

    def get_products(self):
        from outlet_woo.models import Product as WooProduct
        return WooProduct.objects.filter(design=self)

    def num_products(self):
        from outlet_woo.models import Product as WooProduct
        return WooProduct.objects.filter(design=self).count()

    def has_live_product(self, shopobj=None):
        if shopobj:
            rv = wm.Product.objects.filter(shop=shopobj, design=self, status=self.STATUS_LIVE).count()
        else:
            rv = wm.Product.objects.filter(design=self, status=self.STATUS_LIVE).count()
        if rv > 0:
            return True
        return False
    has_live_product.short_description = "Live Product?"
    has_live_product.boolean = True

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
            rv = "{}{}".format(rv, self.code)
        else:
            rv = "".join([rv, "00"])
        if self.name:
            return "{} / {}".format(rv, self.name)
        return _("Unnamed Creative")

    class Meta:
        verbose_name = _("Design")
        verbose_name_plural = _("Designs")
        ordering = ['series__code', 'code', 'name', ]
        unique_together = ('series', 'code',)
