# -*- coding: utf-8 -*-
from django.contrib import admin
# from .forms import *
from django.utils.translation import ugettext as _
from django.db import models
import uuid
from outlet_woo import models as wm
import csv
from django.core import serializers
from django.utils import timezone

# import argparse
# from apiclient.discovery import build
# from oauth2client.service_account import ServiceAccountCredentials
# import httplib2
# from oauth2client import client
# from oauth2client import file
# from oauth2client import tools


class DataFeed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    shop = models.ForeignKey(wm.Shop)
    date_added = models.DateTimeField(auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now=True)
    date_lastgenerated = models.DateTimeField(_("Last Generated"), blank=True, null=True)

    def _remove_html_tags(self, text):
        """Remove html tags from a string"""
        import re
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def get_num_items(self):
        return DataFeedItem.objects.filter(feed=self).count()
    get_num_items.short_description = _("Item Count")

    def generate(self):
        print(DataFeedItem.objects.filter(feed=self).delete())
        products = wm.Product.objects.filter(shop=self.shop, status=wm.Product.STATUS_PUBLISH)
        print("{} Products found for {}.".format(products.count(), self.shop.name))

        for p in products:
            category = [_.name for _ in p.item.category.get_ancestors()]
            category.append(p.item.category.name)
            category = " &gt; ".join(category)
            if p.product_type == p.PRODUCTTYPE_VARIABLE:
                productvariants = wm.ProductVariation.objects.filter(product=p)
                for pv in productvariants:
                    theName = p.name
                    theColor = pv.att_color_obj
                    permalink = p.permalink
                    permalink_params = []
                    if theColor:
                        theColor = theColor.name
                        theName = "{} in {}".format(theName, theColor)
                        permalink_params.append('attribute_color={}'.format(theColor))
                    else:
                        theColor = "White"
                    theSize = pv.att_size_obj
                    if theSize:
                        theSize = theSize.name
                        theName = "{} {}".format(theName, theSize)
                        permalink_params.append('attribute_size={}'.format(theSize))
                    else:
                        theSize = "One Size"

                    if permalink_params:
                        permalink = "{}?{}".format(permalink, "&".join(permalink_params))

                    dfi, created = DataFeedItem.objects.update_or_create(
                        identifier=pv.sku,
                        feed=self,
                        defaults={
                            'title': theName,
                            'description': self._remove_html_tags(p.description).replace("\n", " "),
                            'link': permalink,
                            'image_link': pv.image_url,
                            'availability': 'in stock',
                            'price': "{} USD".format(pv.price),
                            'google_product_category': p.item.googlecategory.long_name,
                            'product_type': category,
                            'brand': " / ".join([p.shop.name, p.design.series.name]),
                            'mpn': pv.sku,
                            'condition': 'new',
                            'item_group_id': p.sku,
                            'color': theColor,
                            'gender': p.item.get_gender_display(),
                            'material': p.item.material,
                            'age_group': p.item.get_age_group_display(),
                            'size': theSize,
                            'shipping_label': p.item.get_item_code(),
                        },
                    )
                    # print("-- Added VARIANT Product: {}".format(dfi.title))
                print("-- Added {} variants for {}.".format(productvariants.count(), p.name))
            elif p.product_type == p.PRODUCTTYPE_SIMPLE:
                dfi, created = DataFeedItem.objects.update_or_create(
                    identifier=p.sku,
                    feed=self,
                    defaults={
                        'title': p.name,
                        'description': self._remove_html_tags(p.description).replace("\n", " "),
                        'link': p.permalink,
                        'image_link': p.get_main_image().src,
                        'availability': 'in stock',
                        'price': "{} USD".format(p.price),
                        'google_product_category': p.item.googlecategory.long_name,
                        'product_type': category,
                        'brand': " / ".join([p.shop.name, p.design.series.name]),
                        'mpn': p.sku,
                        'condition': 'new',
                        'item_group_id': p.sku,
                        'color': 'White',
                        'gender': p.item.get_gender_display(),
                        'material': p.item.material,
                        'age_group': 'Adult',  # p.item.get_age_group_display()
                        'size': 'One Size',
                        'shipping_label': p.item.get_item_code(),
                    },
                )
                print("-- Added Product: {}".format(dfi.title))
            else:
                print("-- {} / Unsupported product type ({}).".format(p.name, p.product_type))
        self.date_lastgenerated = timezone.now()
        self.save()

    def output_file(self, filename=""):
        if not filename:
            filename = "./_data/{}.csv".format(self.code)
        queryset = DataFeedItem.objects.filter(feed=self)
        print("Writing {} products to file {}.".format(queryset.count(), filename))
        opts = queryset.model._meta
        model = queryset.model

        # field_names = [field.name for field in opts.fields]
        field_names = [
            'identifier', 'title', 'description', 'link', 'image_link',
            'availability', 'price', 'google_product_category', 'product_type',
            'brand', 'mpn', 'condition', 'item_group_id', 'color', 'gender',
            'material', 'age_group', 'size', 'shipping_label']
        header_row = [
            'id', 'title', 'description', 'link', 'image_link',
            'availability', 'price', 'google_product_category', 'product_type',
            'brand', 'mpn', 'condition', 'item_group_id', 'color', 'gender',
            'material', 'age_group', 'size', 'shipping_label']
        print("-- Identified these fieldnames: {}".format(field_names))

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header_row)
            for obj in queryset:
                datarow = [getattr(obj, field) for field in field_names]
                print(datarow[0], datarow[1])
                writer.writerow(datarow)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed DataFeed")

    class Meta:
        verbose_name = _("Data Feed")
        verbose_name_plural = _("Data Feeds")
        ordering = ["name", "code", ]


class DataFeedItem(models.Model):
    AVAILABILITY_INSTOCK = 'i'
    AVAILABILITY_OUTOFSTOCK = 'o'
    AVAILABILITY_PREORDER = 'p'
    AVAILABILITY_CHOICES = (
        (AVAILABILITY_INSTOCK, 'in stock'),
        (AVAILABILITY_OUTOFSTOCK, 'out of stock'),
        (AVAILABILITY_PREORDER, 'preorder'),
    )
    CONDITION_NEW = 'n'
    CONDITION_REFURBISHED = 'r'
    CONDITION_USED = 'u'
    CONDITION_CHOICES = (
        (CONDITION_NEW, 'New'),
        (CONDITION_REFURBISHED, 'Refurbished'),
        (CONDITION_USED, 'Used'),
    )

    BOOLEAN_YES = 'yes'
    BOOLEAN_NO = 'no'
    CHOICE_BOOLEAN = (
        (BOOLEAN_YES, True),
        (BOOLEAN_NO, False),
    )
    AGEGROUP_NEWBORN = 'N'
    AGEGROUP_INFANT = 'I'
    AGEGROUP_TODDLER = 'T'
    AGEGROUP_KIDS = 'K'
    AGEGROUP_ADULT = 'A'
    AGEGROUP_CHOICES = (
        (AGEGROUP_NEWBORN, 'Newborn'),
        (AGEGROUP_INFANT, 'Infant'),
        (AGEGROUP_TODDLER, 'Toddler'),
        (AGEGROUP_KIDS, 'Kids'),
        (AGEGROUP_ADULT, 'Adult'),
    )
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_UNISEX = "U"
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_UNISEX, 'Unisex'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    feed = models.ForeignKey(DataFeed)

    identifier = models.CharField(max_length=50, default="", blank=True, null=True)
    title = models.CharField(max_length=150, default="", blank=True, null=True)
    description = models.CharField(max_length=5000, default="", blank=True, null=True)
    link = models.URLField(blank=True)
    image_link = models.URLField(blank=True)
    availability = models.CharField(max_length=70, blank=True, null=True)
    price = models.CharField(max_length=50, default='', blank=True, null=True)
    google_product_category = models.CharField(max_length=500, default='', blank=True, null=True)
    product_type = models.CharField(max_length=750, default='', blank=True, null=True)
    brand = models.CharField(max_length=70, default='', blank=True, null=True)
    mpn = models.CharField(max_length=70, default='', blank=True, null=True)
    condition = models.CharField(max_length=70, default='', blank=True, null=True)
    item_group_id = models.CharField(max_length=50, default="", blank=True, null=True)
    color = models.CharField(max_length=100, default="", blank=True, null=True)
    gender = models.CharField(max_length=70, default="", blank=True, null=True)
    material = models.CharField(max_length=200, default="", blank=True, null=True)
    age_group = models.CharField(max_length=70, default="", blank=True, null=True)
    size = models.CharField(max_length=100, default="", blank=True, null=True)
    shipping_label = models.CharField(max_length=100, default="", blank=True, null=True)

    def __str__(self):
        if self.identifier:
            return "{}".format(self.identifier)
        return _("Unnamed DataFeedItem")

    class Meta:
        verbose_name = _("Data Feed Item")
        verbose_name_plural = _("Data Feed Items")
        ordering = ["feed", "identifier", ]


# class gCredential(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
#     name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
#
#     client_id = models.CharField(_("Client ID"), max_length=64, blank=True, null=True)
#     client_secret = models.CharField(_("Client ID"), max_length=64, blank=True, null=True)
#     scope = models.CharField(_("Scope"), max_length=500, blank=True, null=True)
#
#
#
#     def __str__(self):
#         if self.code and self.name:
#             return "[{}] {}".format(self.code, self.name)
#         if self.name:
#             return "{}".format(self.name)
#         return _("Unnamed gCredential")
#
#     class Meta:
#         verbose_name = _("Google Credential")
#         verbose_name_plural = _("Google Credentials")
#         ordering = ["name","code",]
