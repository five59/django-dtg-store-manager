from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from creative import models as c


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
    series = models.ForeignKey(c.Series, null=True, blank=True)
    artist = models.ForeignKey(c.Artist, null=True, blank=True)
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
