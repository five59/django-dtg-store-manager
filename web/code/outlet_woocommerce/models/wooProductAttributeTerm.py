import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files

from .wooProductAttribute import *
from outlet_woocommerce.api import *


class wooProductAttributeTerm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    productattribute = models.ForeignKey(
        "outlet_woocommerce.wooProductAttribute", verbose_name=_("Product Attribute"), blank=True, null=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    wid = models.CharField(_("Woo ID"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)
    menu_order = models.IntegerField(_("Menu Order"), default=0)
    count = models.IntegerField(_("Count"), default=0)

    wr_tooltip = models.CharField(_("WR Tooltip"), max_length=255,
                                  default="", blank=True, null=True)
    wr_color = models.CharField(_("WR Color"), max_length=255, default="", blank=True, null=True)
    wr_label = models.CharField(_("WR Label"), max_length=255, default="", blank=True, null=True)

    def __str__(self):
        if self.wid and self.name:
            return "[{}] {}".format(self.wid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed wooProductAttributeTerm")

    class Meta:
        verbose_name = _("Product Attribute Term")
        verbose_name_plural = _("Product Attribute Terms")
        ordering = ["menu_order", "name", ]

    def get_store(self):
        return self.productattribute.store
    get_store.short_description = _("Store")

    def get_store_code(self):
        return self.productattribute.store.code
    get_store_code.short_description = _("Store")

    def api_pull(data, attribute):
        # Adds or Updates an existing record
        # FIXME WARNING There is a hack in woocommerce/includes/api/ that attaches
        # the full 'term.meta' object.
        wr_tooltip = ""
        wr_color = ""
        wr_label = ""

        if 'meta' in data:
            if 'wr_tooltip' in data['meta']:
                wr_tooltip = data['meta']['wr_tooltip'][0]
            if 'wr_color' in data['meta']:
                wr_color = data['meta']['wr_color'][0]
            if 'wr_label' in data['meta']:
                wr_label = data['meta']['wr_label'][0]
        else:
            wr_tooltip = ""
            wr_color = ""
            wr_label = ""

        obj, created = wooProductAttributeTerm.objects.update_or_create(
            wid=data['id'],
            productattribute=attribute,
            defaults={
                "is_active": True,
                "name": data['name'],
                "slug": data['slug'],
                "menu_order": data['menu_order'],
                "count": data['count'],
                "wr_tooltip": wr_tooltip,
                "wr_color": wr_color,
                "wr_label": wr_label,
            }
        )
        return obj

    def api_pull_all(store, attribute):
        path = "wc/v1/products/attributes/{}/terms".format(attribute.wid)
        a = wcClient(store=store)
        data = a.get(path)
        wooProductAttributeTerm.objects.filter(productattribute=attribute).update(is_active=False)
        while a.link_next:
            for d in data:
                attribTermObj = wooProductAttributeTerm.api_pull(d, attribute)
            if a.link_next:
                res = a.get(data.link_next)
        else:
            for d in data:
                attribTermObj = wooProductAttributeTerm.api_pull(d, attribute)

    def push_family(attribute):
        family = wooProductAttributeTerm.objects.filter(productattribute=attribute)
        if family:
            data = {
                "create": [],
                "update": [],
                "delete": []
            }

            if not attribute.store:
                raise Exception("Store not found for attribute.", attribute)

            for member in family:
                datum = {
                    "name": member.name,
                    "slug": member.slug,
                    "menu_order": member.menu_order,
                    # TODO handle termmeta (wr_tooltip, wr_color, wr_label)
                }
                if member.wid:
                    datum['id'] = member.wid
                    data['update'].append(datum)
                else:
                    data['create'].append(datum)

            wooProductAttributeTerm._api_batch(attribute, data)

    def _api_create(data):
        method = "POST"
        path = "wc/v1/products/attributes/<attribute_id>/terms"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_retrieve(data):
        method = "GET"
        path = "wc/v1/products/attributes/<attribute_id>/terms/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_list():
        method = "GET"
        path = "wc/v1/products/attributes/<attribute_id>/terms"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_update(self):
        method = "PUT"
        path = "wc/v1/products/attributes/<attribute_id>/terms/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_delete(self):
        method = "DELETE"
        path = "wc/v1/products/attributes/<attribute_id>/terms/<id>"
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_batch(attribute, data):
        method = 'POST'
        path = "wc/v1/products/attributes/{}/terms/batch".format(attribute.wid)
        print(attribute.store, attribute, data)
        try:
            a = wcClient(store=attribute.store)
            data = a.post(path, data)
            for d in data['create']:
                wooProductAttributeTerm.objects.filter(
                    name=d['name'], slug=d['slug']).update(
                        wid=d['id'], count=d['count'])
        except Exception as e:
            raise Exception(e)
