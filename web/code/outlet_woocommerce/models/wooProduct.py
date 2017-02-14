import uuid
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from datetime import datetime
from django.core import files

from outlet_woocommerce.api import *


class wooProduct(models.Model):

    TYPE_SIMPLE = "simple"
    TYPE_GROUPED = "grouped"
    TYPE_EXTERNAL = "external"
    TYPE_VARIABLE = "variable"
    TYPE_CHOICES = (
        (TYPE_SIMPLE, _("Simple")),
        (TYPE_GROUPED, _("Grouped")),
        (TYPE_EXTERNAL, _("External")),
        (TYPE_VARIABLE, _("Variable"))
    )

    STATUS_DRAFT = "draft"
    STATUS_PENDING = "pending"
    STATUS_PRIVATE = "private"
    STATUS_PUBLISH = "publish"
    STATUS_CHOICES = (
        (STATUS_DRAFT, _('Draft')),
        (STATUS_PENDING, _("Pending")),
        (STATUS_PRIVATE, _("Private")),
        (STATUS_PUBLISH, _("Published")),
    )

    VISIBILITY_VISIBLE = "visible"
    VISIBILITY_CATALOG = "catalog"
    VISIBILITY_SEARCH = "search"
    VISIBILITY_HIDDEN = "hidden"
    VISIBILITY_CHOICES = (
        (VISIBILITY_VISIBLE, _("Visible in Catalog and Search")),
        (VISIBILITY_CATALOG, _("Only in Catalog")),
        (VISIBILITY_SEARCH, _("Only in Search")),
        (VISIBILITY_HIDDEN, _("Hidden")),
    )

    DOWNLOADTYPE_STANDARD = 'standard'
    DOWNLOADTYPE_APPLICATION = 'application'
    DOWNLOADTYPE_MUSIC = 'music'
    DOWNLOADTYPE_CHOICES = (
        (DOWNLOADTYPE_STANDARD, _("Standard Product")),
        (DOWNLOADTYPE_APPLICATION, _("Application/Software")),
        (DOWNLOADTYPE_MUSIC, _("Music")),
    )
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
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    woostore = models.ForeignKey("outlet_woocommerce.wooStore",
                                 verbose_name=_("Store"), blank=True, null=True)

    wid = models.CharField(_("Woo ID"), max_length=16, default="",
                           blank=True, null=True, )
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)
    permalink = models.URLField(_("Permalink"), blank=True)
    date_created = models.DateField(_("Date Created"), help_text=_(
        "READONLY. The date the product was created, in the site’s timezone."), blank=True, null=True)
    date_modified = models.DateField(_("Date Modified"), help_text=_(
        "READONLY. The date the product was last modified, in the site’s timezone."), blank=True, null=True)
    type = models.CharField(_("Type"), help_text=_("Product type. Default is simple. In general, do not change this."), max_length=15,
                            default=TYPE_SIMPLE, choices=TYPE_CHOICES)
    status = models.CharField(_("Status"), help_text=_("Product status (post status). Default is publish."), max_length=15,
                              default=STATUS_PUBLISH, choices=STATUS_CHOICES)
    featured = models.BooleanField(_("Featured?"), help_text=_(
        "Featured product. Default is false."), default=False)
    catalog_visibility = models.CharField(
        _("Visibility"), help_text=_("Catalog visibility. Default is visible. Options: visible (Catalog and search), catalog (Only in catalog), search (Only in search) and hidden (Hidden from all)."), max_length=10, default=VISIBILITY_VISIBLE, choices=VISIBILITY_CHOICES)
    description = models.TextField(_("Description"), help_text=_(
        "Product description."), null=True, blank=True)
    short_description = models.TextField(
        _("Short Description"), help_text=_("Product short description."), null=True, blank=True)
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
    price_html = models.CharField(_("Price HTML"), help_text=_("READONLY. Price formatted in HTML."), max_length=1000,
                                  default="", blank=True, null=True)
    on_sale = models.BooleanField(_("On Sale?"), help_text=_(
        "READONLY. Shows if the product is on sale."), default=False)
    purchasable = models.BooleanField(_("Purchasable?"), help_text=_(
        "READONLY. Shows if the product can be bought."), default=True)
    total_sales = models.IntegerField(_("Total Sales"), help_text=_(
        "READONLY. Amount of sales."), default=0)
    virtual = models.BooleanField(_("Virtual?"), help_text=_(
        "If the product is virtual. Virtual products are intangible and aren’t shipped. Default is false."), default=False)

    downloadable = models.BooleanField(_("Downloadable?"), help_text=_(
        "If the product is downloadable. Downloadable products give access to a file upon purchase. Default is false."), default=False)
    # TODO downloads
    download_limit = models.IntegerField(_("Download Limit"), help_text=_(
        "Amount of times the product can be downloaded, the -1 values means unlimited re-downloads. Default is -1."), default=-1)
    download_expiry = models.IntegerField(_("Download Expiry"), help_text=_(
        "Number of days that the customer has up to be able to download the product, the -1 means that downloads never expires. Default is -1."), default=-1)
    download_type = models.CharField(_("Download Type"), help_text=_("Download type, this controls the schema on the front-end. Default is standard. Options: 'standard' (Standard Product), application (Application/Software) and music (Music)."), max_length=15,
                                     default=DOWNLOADTYPE_STANDARD, choices=DOWNLOADTYPE_CHOICES)

    external_url = models.URLField(_("External URL"), help_text=_("Product external URL. Only for external products."),
                                   default="", null=True, blank=True)
    button_text = models.CharField(_("Button Text"), help_text=_("Product external button text. Only for external products."),
                                   max_length=255, default="", null=True, blank=True)

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
    sold_individually = models.BooleanField(_("Sold Individually?"), help_text=_(
        "Allow one item to be bought in a single order. Default is false."), default=False)

    weight = models.DecimalField(_("Weight"), help_text=_("Product weight in decimal format."), max_digits=10, decimal_places=2,
                                 default=0)
    shipping_required = models.BooleanField(_("Requires Shipping?"), help_text=_(
        "READONLY. Shows if the product need to be shipped."), default=False)
    shipping_taxable = models.BooleanField(_("Taxable Shipping?"), help_text=_(
        "READONLY. Shows whether or not the product shipping is taxable."), default=False)
    # TODO shipping_class
    # TODO shipping_class_id
    reviews_allowed = models.BooleanField(_("Reviewed Allowed?"), help_text=_(
        "Allow reviews. Default is true."), default=True)
    average_rating = models.CharField(
        _("Average Rating"), help_text=_("READONLY. Reviews average rating."), max_length=15, default="", null=True, blank=True)
    rating_count = models.IntegerField(_("Rating Count"), help_text=_(
        "READONLY. Amount of reviews that the product have."), default=0)

    parent = models.ForeignKey('self', verbose_name=_(
        "Parent"), help_text=_("Product parent."), null=True, blank=True)
    purchase_note = models.CharField(
        _("Purchase Note"), help_text=_("Optional note to send the customer after purchase."), max_length=255, default="", null=True, blank=True)

    menu_order = models.IntegerField(_("Menu Order"), help_text=_(
        "Menu order, used to custom sort products."), default=0)

    # COLLECTIONS

    # TODO dimensions
    # TODO categories
    # TODO tags
    # TODO images
    # TODO attributes
    # TODO default_attributes
    # TODO variations
    # TODO related_ids
    # TODO upsell_ids
    # TODO cross_sell_ids
    # TODO grouped_products

    def __str__(self):
        if self.wid and self.name:
            return "{} - {}".format(self.wid, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Product")

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["name", "wid", ]
