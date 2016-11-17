from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
import uuid
from creative import models as cr
from catalog import models as ca
from outlet_woo import models as wc
import pytz
import datetime
from django.utils import timezone
from timezone_field import TimeZoneField


class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    web_url = models.URLField(_("Website"), default="", blank=True, null=True)
    consumer_key = models.CharField(_("Consumer Key"), max_length=43, blank=True, null=True)
    consumer_secret = models.CharField(_("Consumer Secret"), max_length=43, blank=True, null=True)
    timezone = TimeZoneField(default='America/New_York')
    num_products = models.IntegerField(_("Product Count"), default=0)
    last_sync = models.DateTimeField(auto_now=True)
    added = models.DateTimeField(auto_now_add=True)

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
        return _("Unnamed Shop")

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shop")
        ordering = ["name", "code", ]
