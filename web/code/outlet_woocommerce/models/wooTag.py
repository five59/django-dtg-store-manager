import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files

from outlet_woocommerce.api import *


class wooTag(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    store = models.ForeignKey("outlet_woocommerce.wooStore", blank=True, null=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    wid = models.IntegerField(_("Woo ID"), default=0)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)
    description = models.TextField(_("Description"), default="", blank=True, null=True)
    count = models.IntegerField(_("Count"), default=0)

    def __str__(self):
        if self.wid and self.name:
            return "{} - {}".format(self.wid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed wooTag")

    class Meta:
        verbose_name = _("Product Tag")
        verbose_name_plural = _("Product Tags")
        ordering = ["store", "name", ]

    def _api_pull(data, store):
        # Adds or Updates an existing record
        obj, created = wooTag.objects.update_or_create(
            wid=data['id'],
            store=store,
            defaults={
                "is_active": True,
                "name": data['name'],
                "slug": data['slug'],
                "description": data['description'],
                "count": data['count'],
            }
        )
        return obj

    def api_push(self):
        # Pushes the object to the remote WooCommerce API. Handles switching
        # between Create and Update mode automatically.
        # If 'terms' then also push the associated terms.

        data = {
            "name": self.name,
            "slug": self.slug,
            "description": self.description,
        }
        if self.wid:  # If has a remote ID, then we know it already exists.
            self._api_update(data)
        else:  # This doesn't exist remotely, so we can create it.
            self._api_create(data)

    # API Interface Methods
    def api_pull_all(store):
        path = "wc/v1/products/tags"
        a = wcClient(store=store)
        data = a.get(path)
        wooTag.objects.filter(store=store).update(is_active=False)
        while a.link_next:
            for d in data:
                attribObj = wooTag._api_pull(d, store)
            if a.link_next:
                res = a.get(data.link_next)
        else:
            for d in data:
                attribObj = wooTag._api_pull(d, store)

    def _api_create(self, data):
        method = "POST"
        path = "wc/v1/products/tags"
        try:
            a = wcClient(store=self.store)
            data = a.post(path, data)
        except Exception as e:
            raise Exception(e)
        print("Created")
        self.wid = data['id']
        self.save()

    def _api_retrieve(self):
        method = "GET"
        path = "wc/v1/products/tags/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_update(self, data):
        method = "PUT"
        path = "wc/v1/products/tags/" + str(self.wid)
        try:
            a = wcClient(store=self.store)
            data = a.post(path, data)
        except Exception as e:
            raise Exception(e)
        self.save()

    def _api_delete(self):
        method = "DELETE"
        path = "wc/v1/products/tags/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_batch(data):
        method = 'POST'
        path = "wc/v1/products/tags/<tag_id>/terms/batch"
        raise NotImplementedError("Not Implemented (Yet) ")
