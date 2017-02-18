from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid


class pfStore(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=50, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    website = models.CharField(_("Website"), max_length=255, default="", blank=True, null=True)
    created = models.CharField(_("Created"), max_length=255, default="", blank=True, null=True)

    consumer_key = models.CharField(_("API Consumer Key"), max_length=64, default="", blank=True)
    consumer_secret = models.CharField(
        _("API Consumer Secret"), max_length=64, default="", blank=True)

    def has_api_auth(self):
        if self.consumer_key and self.consumer_secret:
            return True
        return False
    has_api_auth.short_description = 'Has API Auth?'
    has_api_auth.boolean = True

    def __str__(self):
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Printful Store")

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")
        ordering = ["name", "code", ]

    def sync_printful_products(self):
        """
        Syncs the Printful product library with the local database. Doesn't delete anything locally,
        but instead flags it with the is_active attribute.
        """
        from vendor_printful.api import pfClient
        if self.has_api_auth():
            a = pfClient(store=self)
            a.update_catalogproducts()
        else:
            raise Exception("API Key not found for this store. Check the admin dashboard.")

    def sync_printful_printfiles(self):
        """
        Syncs the Printful file library for this particular store. Doesn't delete anything locally,
        but instead flags it with the is_active attribute.
        """
        from vendor_printful.api import pfClient
        if self.has_api_auth():
            a = pfClient(store=self)
            a.update_printfiles()
        else:
            raise Exception("API Key not found for this store. Check the admin dashboard.")

    def sync_printful_syncproducts(self):
        """
        Syncs the 'syncproducts' between the store and the local database. These define how a particular
        SKU should be produced.
        """
        from vendor_printful.api import pfClient
        if self.has_api_auth():
            a = pfClient(store=self)
            a.update_syncproducts()
        else:
            raise Exception("API Key not found for this store. Check the admin dashboard.")

    def sync_printful_geos(self):
        """
        Syncs the pfState and pfCountry database tabales with the Printful API.
        """
        from vendor_printful.api import pfClient
        if self.has_api_auth():
            a = pfClient(store=self)
            a.update_geos()
        else:
            raise Exception("API Key not found for this store. Check the admin dashboard.")
