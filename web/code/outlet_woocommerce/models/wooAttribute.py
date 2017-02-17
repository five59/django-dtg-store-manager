import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files

from .wooTerm import *
from outlet_woocommerce.api import *


class wooAttribute(models.Model):

    TYPE_TEXT = "text"
    TYPE_COLORPICKER = "color picker"
    TYPE_IMAGESELECT = "image select"
    TYPE_TEXTLABEL = "text label"
    TYPE_CHOICES = (
        (TYPE_TEXT, _("Basic Text")),
        (TYPE_COLORPICKER, _("Color Picker")),
        (TYPE_IMAGESELECT, _("Image Select")),
        (TYPE_TEXTLABEL, _("Text Label")),
    )

    ORDER_NAME = "name"
    ORDER_NAMENUMBER = "name_num"
    ORDER_ID = "id"
    ORDER_MENU = "menu_order"
    ORDER_CHOICES = (
        (ORDER_NAME, _("Sort by Name")),
        (ORDER_NAMENUMBER, _("Sort by Name (Number)")),
        (ORDER_ID, _("Sort by ID")),
        (ORDER_MENU, _("Sort by Custom Menu Order")),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    store = models.ForeignKey("outlet_woocommerce.wooStore", blank=True, null=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    wid = models.CharField(_("Woo ID"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)
    type = models.CharField(_("Type"), max_length=255, default="",
                            blank=True, null=True, choices=TYPE_CHOICES)
    order_by = models.CharField(_("Order By"), max_length=255, default="",
                                blank=True, null=True, choices=ORDER_CHOICES)
    has_archives = models.BooleanField(_("Has Archives?"), default=False)

    def __str__(self):
        if self.wid and self.name:
            return "[{}] {}".format(self.wid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed wooAttribute")

    class Meta:
        verbose_name = _("Product Attribute")
        verbose_name_plural = _("Product Attributes")
        ordering = ["store", "order_by", "name", ]

    def get_terms(self):
        return wooTerm.objects.filter(productattribute=self)
    get_terms.short_description = _("Terms")

    def num_terms(self):
        return self.get_terms().count()
    num_terms.short_description = _("Num Terms")

    def _api_pull(data, store):
        # Adds or Updates an existing record
        obj, created = wooAttribute.objects.update_or_create(
            wid=data['id'],
            store=store,
            defaults={
                "is_active": True,
                "name": data['name'],
                "slug": data['slug'],
                "type": data['type'],
                "order_by": data['order_by'],
                "has_archives": data['has_archives'],
            }
        )
        return obj

    def api_push(self, terms=False):
        # Pushes the object to the remote WooCommerce API. Handles switching
        # between Create and Update mode automatically.
        # If 'terms' then also push the associated terms.

        data = {
            "name": self.name,
            "slug": self.slug,
            "type": self.type,
            "order_by": self.order_by,
            "has_archives": self.has_archives,
        }
        if self.wid:  # If has a remote ID, then we know it already exists.
            self._api_update(data)
        else:  # This doesn't exist remotely, so we can create it.
            self._api_create(data)

        if terms:
            wooTerm.push_family(self)

    # API Interface Methods
    def api_pull_all(store, import_terms=True):
        path = "wc/v1/products/attributes"
        a = wcClient(store=store)
        data = a.get(path)
        wooAttribute.objects.filter(store=store).update(is_active=False)
        while a.link_next:
            for d in data:
                attribObj = wooAttribute._api_pull(d, store)
                if import_terms:
                    wooTerm.api_pull_all(store, attribObj)
            if a.link_next:
                res = a.get(data.link_next)
        else:
            for d in data:
                attribObj = wooAttribute._api_pull(d, store)
                if import_terms:
                    wooTerm.api_pull_all(store, attribObj)

    def _api_create(self, data):
        method = "POST"
        path = "wc/v1/products/attributes"
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
        path = "wc/v1/products/attributes/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_update(self, data):
        method = "PUT"
        path = "wc/v1/products/attributes/" + str(self.wid)
        try:
            a = wcClient(store=self.store)
            data = a.post(path, data)
        except Exception as e:
            raise Exception(e)
        self.save()

    def _api_delete(self):
        method = "DELETE"
        path = "wc/v1/products/attributes/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_batch(data):
        method = 'POST'
        path = "wc/v1/products/attributes/<attribute_id>/terms/batch"
        raise NotImplementedError("Not Implemented (Yet) ")
