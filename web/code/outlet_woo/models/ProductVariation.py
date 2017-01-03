import uuid
import requests
import urllib
import os
import tempfile
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files
from creative import models as cr
from catalog import models as ca
from app_care import models as ac
from outlet_woo import models as wc

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.base import ContentFile
import math
import logging
import textwrap


class ProductVariation(models.Model):
    logger = logging.getLogger(__name__)

    TAXSTATUS_TAXABLE = 'taxable'
    TAXSTATUS_SHIPPING = 'shipping'
    TAXSTATUS_NONE = 'none'
    TAXSTATUS_CHOICES = (
        (TAXSTATUS_TAXABLE, _("Taxable")),
        (TAXSTATUS_SHIPPING, _("Shipping Only")),
        (TAXSTATUS_NONE, _("None")),
    )
    BACKORDERS_NO = 'no'
    BACKORDERS_NOTIFY = 'notify'
    BACKORDERS_YES = 'yes'
    BACKORDERS_CHOICES = (
        (BACKORDERS_NO, _("Do Not Allow")),
        (BACKORDERS_NOTIFY, _("Allow, But Notify Customer")),
        (BACKORDERS_YES, _("Allow")),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), help_text=_(""), max_length=16,
                            default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    product = models.ForeignKey(wc.Product, blank=True, null=True)
    app_added = models.DateTimeField(auto_now_add=True, help_text=_(""))
    app_last_sync = models.DateTimeField(auto_now=True, help_text=_(""))
    date_created = models.DateTimeField(_("Created"), help_text=_(
        "READONLY. The date the product was created. In the site's timezone."), blank=True, null=True)
    date_modified = models.DateTimeField(_("Modified"), help_text=_(
        "READONLY. The date the product was last modified, in the site's timezone."), blank=True, null=True)

    permalink = models.CharField(_("Permalink"), help_text=_(
        "READONLY. Product URL."), max_length=255, default="", blank=True, null=True)

    sku = models.CharField(_("SKU"), help_text=_("Unique identifier."), max_length=255,
                           default="", blank=True, null=True)

    price = models.CharField(_("Price"), help_text=_(
        "READONLY. Current product price. This is set from regular_price and sale_price."), max_length=255, default="", blank=True, null=True)
    regular_price = models.CharField(_("Regular Price"), help_text=_("Product regular price."), max_length=255,
                                     default="", blank=True, null=True)
    sale_price = models.CharField(_("Sale Price"), help_text=_("Product sale price."), max_length=255,
                                  default="", blank=True, null=True)
    date_on_sale_from = models.DateField(_("On Sale From"), help_text=_(
        "Start date of sale price. Date in the YYYY-MM-DD format."), blank=True, null=True)
    date_on_sale_to = models.DateField(_("On Sale To"), help_text=_(
        "End date of sale price. Date in the YYYY-MM-DD format."), blank=True, null=True)
    on_sale = models.BooleanField(_("On Sale?"), help_text=_(
        "READONLY. Shows if the product is on sale."), default=False)
    purchasable = models.BooleanField(_("Purchasable?"), help_text=_(
        "READONLY. Shows if the product can be bought."), default=True)

    virtual = models.BooleanField(_("Virtual?"), help_text=_(
        "If the product is virtual. Virtual products are intangible and aren’t shipped. Default is false."), default=False)
    downloadable = models.BooleanField(_("Downloadable?"), help_text=_(
        "If the product is downloadable. Downloadable products give access to a file upon purchase. Default is false."), default=False)
    download_limit = models.IntegerField(_("Download Limit"), help_text=_(
        "Amount of times the product can be downloaded, the -1 values means unlimited re-downloads. Default is -1."), default=-1)
    download_expiry = models.IntegerField(_("Download Expiry"), help_text=_(
        "Number of days that the customer has up to be able to download the product, the -1 means that downloads never expires. Default is -1."), default=-1)

    tax_status = models.CharField(_("Tax Status"), help_text=_("Tax status. Default is taxable. Options: taxable, shipping (Shipping only) and none."), max_length=15,
                                  default=TAXSTATUS_TAXABLE, choices=TAXSTATUS_CHOICES)
    tax_class = models.CharField(_("Tax Class"), help_text=_(
        "The tax class."), max_length=255, default="", null=True, blank=True)

    manage_stock = models.BooleanField(_("Manage Stock"), help_text=_(
        "Stock management at product level. Default is false."), default=False)
    stock_quantity = models.IntegerField(_("Stock Quantity"), help_text=_(
        "Stock quantity. If is a variable product this value will be used to control stock for all variations, unless you define stock at variation level."), default=0)
    in_stock = models.BooleanField(_("In Stock?"), help_text=_(
        "Controls whether or not the product is listed as “in stock” or “out of stock” on the frontend. Default is true."), default=True)
    backorders = models.CharField(_("Backorders"), help_text=_("If managing stock, this controls if backorders are allowed. If enabled, stock quantity can go below 0. Default is no. Options are: no (Do not allow), notify (Allow, but notify customer), and yes (Allow)."), max_length=255,
                                  default=BACKORDERS_NO, choices=BACKORDERS_CHOICES)
    backorders_allowed = models.BooleanField(
        _("Backorders Allowed?"), help_text=_("READONLY. Shows if backorders are allowed."), default=False)
    backordered = models.BooleanField(_("Backordered?"), help_text=_(
        "READONLY. Shows if a product is on backorder (if the product have the stock_quantity negative)."), default=False)

    weight = models.DecimalField(_("Weight"), help_text=_("Product weight in decimal format."), max_digits=10, decimal_places=2,
                                 default=0)

    product_label = models.ImageField(_("Product Label"), upload_to="outlet_woo/productlabel",
                                      # height_field="image_height",
                                      # width_field="product_label_width",
                                      blank=True, null=True, help_text="")

    # dimensions
    # shipping_class
    # shipping_class_id

    image_url = models.URLField(_("Image URL"), blank=True, null=True,
                                help_text=_("This is the URL for the primary variant image."))

    # attributes

    # FIXME This is a short-term fix. Rather than go down the attribute object
    # path, for now, we're just capturing color and size where available.
    att_color = models.CharField(_("Color"), max_length=64, null=True, blank=True, default="")
    att_color_obj = models.ForeignKey(ca.Color, null=True)
    att_size = models.CharField(_("Size"), max_length=64, null=True, blank=True, default="")
    att_size_obj = models.ForeignKey(ca.Size, null=True)

    def has_image_url(self):
        return True if self.image_url else False
    has_image_url.short_description = _("Has Image?")
    has_image_url.boolean = True

    def _add_centered_text(self, image, size, yvalue, content):
        font_path = "/code/_resources/Aller/Aller_Rg.ttf"
        font = ImageFont.truetype(font_path, size)
        draw = ImageDraw.Draw(image)
        tw, th = draw.textsize(content, font=font)
        draw.text((450 - (tw / 2), yvalue), content, (0, 0, 0), font=font)
        return image

    def _open_eps(self, filename, width=None):
        original = [float(d) for d in Image.open(filename).size]
        scale = width / original[0]
        im = Image.open(filename)

        mask = Image.new("L", im.size, color=255)
        im.putalpha(mask)

        if width is not None:
            im.load(scale=math.ceil(scale))
        if scale != 1:
            im.thumbnail([int(scale * d) for d in original], Image.ANTIALIAS)
        return im

    def _invert_image(self, image):
        return image.point(lambda p: 255 - p)

    def _create_inside_label(self):
        CARE_ICON_SIZE = 40
        CARE_ICON_PADDING = 10

        try:
            ci = ac.CareInstructions.objects.get(item=self.product.item)
            img_label_base = Image.open(self.product.shop.product_label_base.file.name)

            img_label = Image.new("RGBA", (900, 900), (255, 255, 255, 255))
            img_label.paste(img_label_base, (0, 0))

            img_label = self._add_centered_text(img_label, 46, 190, self.att_size_obj.name.upper())
            img_label = self._add_centered_text(
                img_label, 28, 265, "Made in {}".format(self.product.item.country_origin).upper())
            img_label = self._add_centered_text(
                img_label, 28, 300, self.product.item.material.upper())
            img_label = self._add_centered_text(img_label, 21, 440, self.sku.upper())

            d = ci.get_list()
            w = len(d) * (CARE_ICON_SIZE + CARE_ICON_PADDING) - CARE_ICON_PADDING
            img_care = Image.new("RGBA", (w, CARE_ICON_SIZE), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img_care)
            xpos = 0
            care_text = []
            for p in d:
                item = self._open_eps(p.icon.file, CARE_ICON_SIZE)
                care_text.append(p.name)
                width, height = item.size
                ypos = int((CARE_ICON_SIZE - height) / 2)
                img_care.paste(item, (xpos, ypos))
                xpos = xpos + CARE_ICON_SIZE + CARE_ICON_PADDING
            img_label.paste(img_care, (int(450 - (w / 2)), 372))
            care_text.append("")
            care_text = ". ".join(care_text).strip().upper()
            lines = textwrap.wrap(care_text, width=35)
            y_text = 530
            for line in lines:
                # logger.warning(line)
                img_label = self._add_centered_text(img_label, 18, y_text, line)
                y_text += 22

            img_label_io = BytesIO()
            img_label.save(img_label_io, format='PNG')
            #
            # img_inverted = img_label.convert('RGBA')
            # r,g,b,a=img_inverted.split()
            # r,g,b=map(_invert_image, (r,g,b))
            # img_inverted = Image.merge('RGBA', (r,g,b,a))
            #
            self.product_label.delete(save=False)

            self.product_label.save(
                "inside_label-{}.png".format(self.sku).replace("-", "/"),
                content=ContentFile(img_label_io.getvalue()),
                save=False,
            )
            self.save()

        except Exception as e:
            self.logger.warning("-- {} / unable to create label: {}".format(self, e))
            return False

        self.logger.info("-- Created {}".format(self.product_label.file.name))

    def _create_outside_label(self):
        try:
            img_label_base = Image.open(self.product.shop.product_label_base.file.name)

            img_label = Image.new("RGBA", (900, 900), (255, 255, 255, 255))
            img_label.paste(img_label_base, (0, 0))

            img_label = self._add_centered_text(img_label, 21, 440, self.sku.upper())

            img_label_io = BytesIO()
            img_label.save(img_label_io, format='PNG')

            self.product_label.delete(save=False)

            self.product_label.save(
                "outside_label-{}.png".format(self.sku).replace("-", "/"),
                content=ContentFile(img_label_io.getvalue()),
                save=False,
            )
            self.save()

        except Exception as e:
            self.logger.warning("-- {} / unable to create label: {}".format(self, e))
            return False

        self.logger.info("-- Created {}".format(self.product_label.file.name))

    def generate_product_label(self, recreate=False):
        self.logger.info("Creating Product Label for {} / {} / {} / {}".format(
            self.code, self.product.name, self.att_size_obj, self.att_color_obj))

        # If it already exists and we don't want to recreate it:
        if self.product_label and not recreate:
            self.logger.info('-- Skipping {}'.format(self))
            return

        if self.product.item.product_label_type == self.product.item.LABEL_INSIDE:
            self._create_inside_label()
        elif self.product.item.product_label_type == self.product.item.LABEL_OUTSIDE:
            self._create_outside_label()
        else:
            self.logger.info("No need to create.")

    def update_sku(self):
        # SKU should be:
        # [SERIES][DESIGN]-[SITE][ITEM]-[VARIANTCOLOR][VARIANTSIZE]
        r = [
            self.product.sku,
            "-",
            self.att_color_obj.code if self.att_color_obj else "",
            self.att_size_obj.code if self.att_size_obj else "",
        ]
        self.sku = "".join(r).upper().replace("-XXXXXX", "").replace("XXX", "")

    def update_meta(self):
        self.logger.info("Updating: {}".format(self))
        if self.att_color:
            obj, created = ca.Color.objects.update_or_create(
                name=self.att_color,
                brand=self.product.item.brand,
                defaults={}
            )
            self.att_color_obj = obj
            if created:
                self.logger.info("-- Color: Created {}".format(self.att_color_obj))
            else:
                self.logger.info(
                    "-- Color: Matched {} to {}".format(self.att_color, self.att_color_obj))

        if self.att_size:
            if self.att_size == 'Extra Small':
                self.att_size = 'Extra-Small'
            elif self.att_size == 'S':
                self.att_size = "Small"
            elif self.att_size == 'M':
                self.att_size = "Medium"
            elif self.att_size == 'L':
                self.att_size = 'Large'
            elif self.att_size == "Extra Large":
                self.att_size = 'Extra-Large'
            obj, created = ca.Size.objects.update_or_create(
                name=self.att_size,
                defaults={}
            )
            self.att_size_obj = obj
            if created:
                self.logger.info("-- Size: Created {}".format(self.att_size_obj))
            else:
                self.logger.info(
                    "-- Size: Matched {} to {}".format(self.att_size, self.att_size_obj))

        self.save()

    def save(self, *args, **kwargs):
        self.update_sku()
        super(ProductVariation, self).save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        if self.code:
            return "{}".format(self.code)
        return _("Unnamed Product Variation")

    class Meta:
        verbose_name = _("Product Variation")
        verbose_name_plural = _("Product Variations")
        ordering = ["name", "code", ]
