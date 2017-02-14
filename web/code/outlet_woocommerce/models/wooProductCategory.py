import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files

from outlet_woocommerce.api import *


class wooProductCategory(models.Model):

    DISPLAY_DEFAULT = 'default'
    DISPLAY_PRODUCTS = 'products'
    DISPLAY_SUBCATEGORIES = 'subcategories'
    DISPLAY_BOTH = 'both'
    DISPLAY_CHOICES = (
        (DISPLAY_DEFAULT, _("Default")),
        (DISPLAY_PRODUCTS, _("Products")),
        (DISPLAY_SUBCATEGORIES, _("Subcategories")),
        (DISPLAY_BOTH, _("Display Both"))
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    store = models.ForeignKey("outlet_woocommerce.wooStore", blank=True, null=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    wid = models.IntegerField(_("Woo ID"), default=0, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)
    parent = models.IntegerField(_("Parent ID"), default=0)
    description = models.TextField(_("Description"), default="", blank=True, null=True)
    display = models.CharField(_("Display"), max_length=255,
                               default=DISPLAY_DEFAULT, choices=DISPLAY_CHOICES)
    menu_order = models.IntegerField(_("Menu Order"), default=0)
    count = models.IntegerField(_("Count"), default=0)

    image_id = models.IntegerField(_("Image ID"), default=0)
    image_date_created = models.CharField(
        _("Image Created"), max_length=255, default="", blank=True, null=True)
    image_date_modified = models.CharField(
        _("Image Modified"), max_length=255, default="", blank=True, null=True)
    image_src = models.CharField(_("Image SRC"), max_length=255,
                                 default="", blank=True, null=True)
    image_name = models.CharField(_("Image Name"), max_length=255,
                                  default="", blank=True, null=True)
    image_alt = models.CharField(_("Image Alt Text"), max_length=255,
                                 default="", blank=True, null=True)

    def has_image(self):
        if self.image_src:
            return True
        return False
    has_image.short_description = _("Has Image?")

    def __str__(self):
        if self.wid and self.name:
            return "{} - {}".format(self.wid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed wooProductCategory")

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")
        ordering = ["store", "name", ]

    def _api_pull(data, store):
        # Adds or Updates an existing record
        defaults = {
            "is_active": True,
            "name": data['name'],
            "slug": data['slug'],
            "parent": data['parent'],
            "description": data['description'],
            "display": data['display'],
            "menu_order": data['menu_order'],
            "count": data['count'],
        }
        if "id" in data['image']:  # Since 'image' gets sent empty if no image.
            # WARNING May break pre-3.5 (see "Unpacking Generalizations"
            # https://www.python.org/dev/peps/pep-0448/)
            defaults = {**defaults, **{
                "image_id": data['image']['id'],
                "image_date_created": data['image']['date_created'],
                "image_date_modified": data['image']['date_modified'],
                "image_src": data['image']['src'],
                "image_name": data['image']['title'],
                "image_alt": data['image']['alt'],
            }}
        obj, created = wooProductCategory.objects.update_or_create(
            wid=data['id'],
            store=store,
            defaults=defaults,
        )
        return obj

    def api_push(self):
        # Pushes the object to the remote WooCommerce API. Handles switching
        # between Create and Update mode automatically.
        # If 'terms' then also push the associated terms.

        data = {
            "name": self.name,
            "slug": self.slug,
            "parent": self.parent,
            "description": self.description,
            "display": self.display,
            "menu_order": self.menu_order,
        }
        if self.has_image():
            data = {**data, **{"image": {
                "date_created": self.image_date_created,
                "date_modified": self.image_date_modified,
                "src": self.image_src,
                "title": self.image_name,
                "alt": self.image_alt,
            }}}

        if self.wid:  # If has a remote ID, then we know it already exists.
            self._api_update(data)
        else:  # This doesn't exist remotely, so we can create it.
            self._api_create(data)

    # API Interface Methods
    def api_pull_all(store):
        path = "wc/v1/products/categories"
        a = wcClient(store=store)
        data = a.get(path)
        wooProductCategory.objects.filter(store=store).update(is_active=False)
        while a.link_next:
            for d in data:
                attribObj = wooProductCategory._api_pull(d, store)
            if a.link_next:
                res = a.get(data.link_next)
        else:
            for d in data:
                attribObj = wooProductCategory._api_pull(d, store)

    def _api_create(self, data):
        method = "POST"
        path = "wc/v1/products/categories"
        try:
            a = wcClient(store=self.store)
            print(data)
            data = a.post(path, data)
        except Exception as e:
            raise Exception(e)
        print("Created")
        self.wid = data['id']
        if "id" in data['image']:  # Since 'image' gets sent empty if no image.
            self.image_id = data['image']['id']
        self.save()

    def _api_retrieve(self):
        method = "GET"
        path = "wc/v1/products/categories/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_update(self, data):
        method = "PUT"
        path = "wc/v1/products/categories/" + str(self.wid)
        try:
            a = wcClient(store=self.store)
            data = a.post(path, data)
        except Exception as e:
            raise Exception(e)
        self.save()

    def _api_delete(self):
        method = "DELETE"
        path = "wc/v1/products/categories/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_batch(data):
        method = 'POST'
        path = "wc/v1/products/categories/<Category_id>/terms/batch"
        raise NotImplementedError("Not Implemented (Yet) ")
