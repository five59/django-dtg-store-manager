from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from timezone_field import TimeZoneField
import uuid


class wooStore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True,
                            help_text=_("Generally, a two-character uppercase code. Used in SKUs."))
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    base_url = models.URLField(_("Base URL"), default="", blank=True, null=True, help_text=_(
        "Include the schema and FQDN only (e.g., 'https://example.com'). No trailing slash."))
    consumer_key = models.CharField(_("Consumer Key"), max_length=43, blank=True, null=True)
    consumer_secret = models.CharField(_("Consumer Secret"), max_length=43, blank=True, null=True)
    timezone = TimeZoneField(default='America/New_York')
    verify_ssl = models.BooleanField(_("Verify SSL?"), default=True, help_text=_(
        "Uncheck this if you are using a self-signed SSL certificate to disable ssl verification."))
    # num_products = models.IntegerField(_("Product Count"), default=0)
    # product_label_base = models.ImageField(_("Product Label Base"), blank=True, null=True, help_text=_(
    #     "Should be 900x900 pixels (3\"x3\" @ 300dpi)"))

    # def get_product(self):
    #     rv = wm.Product.objects.filter(store=self, status=wm.Product.STATUS_PUBLISH)

    def has_key(self):
        if self.has_key:
            return True
        return False
    has_key.short_description = "Has Key?"
    has_key.boolean = True

    def has_secret(self):
        if self.consumer_secret:
            return True
        return False
    has_secret.short_description = "Has Secret?"
    has_secret.boolean = True

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed wooStore")

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")
        ordering = ["name", "code", ]
