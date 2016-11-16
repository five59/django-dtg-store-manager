from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
import uuid
from datetime import datetime
from creative import models as cr
from catalog import models as ca
from outlet_woo import models as wc


class Product(models.Model):
    PRODUCTTYPE_SIMPLE = "simple"
    PRODUCTTYPE_GROUPED = 'grouped'
    PRODUCTTYPE_EXTERNAL = 'external'
    PRODUCTTYPE_VARIABLE = 'variable'
    PRODUCTTYPE_CHOICES = (
        (PRODUCTTYPE_SIMPLE, _("Simple")),
        (PRODUCTTYPE_GROUPED, _("Grouped")),
        (PRODUCTTYPE_EXTERNAL, _("External")),
        (PRODUCTTYPE_VARIABLE, _("Variable")),
    )
    STATUS_DRAFT = 'draft',
    STATUS_PENDING = 'pending'
    STATUS_PRIVATE = 'private'
    STATUS_PUBLISH = 'publish'
    STATUS_CHOICES = (
        (STATUS_DRAFT, _("Draft")),
        (STATUS_PENDING, _("Pending")),
        (STATUS_PRIVATE, _("Private")),
        (STATUS_PUBLISH, _("Publish")),
    )
    VISIBILITY_VISIBLE = 'visible'
    VISIBILITY_CATALOG = 'catalog'
    VISIBILITY_SEARCH = 'search'
    VISIBILITY_HIDDEN = 'hidden'
    VISIBILITY_CHOICES = (
        (VISIBILITY_VISIBLE, _("Visible")),
        (VISIBILITY_CATALOG, _("Catalog Only")),
        (VISIBILITY_SEARCH, _("Search Only")),
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
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = models.CharField(_("Slug"), max_length=255, default="", blank=True, null=True)

    app_added = models.DateTimeField(auto_now_add=True)
    app_last_sync = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey(wc.Shop, blank=True, null=True)
    is_active = models.BooleanField(_("Is Active?"), default=False)

    permalink = models.CharField(_("Permalink"), max_length=255, default="", blank=True, null=True)

    date_created = models.DateTimeField(_("Created"), blank=True, null=True)
    date_modified = models.DateTimeField(_("Modified"), blank=True, null=True)

    product_type = models.CharField(_("Type"), max_length=15,
                                    default=PRODUCTTYPE_SIMPLE, choices=PRODUCTTYPE_CHOICES)
    status = models.CharField(_("Status"), max_length=15,
                              default=STATUS_PUBLISH, choices=STATUS_CHOICES)
    featured = models.BooleanField(_("Featured?"), default=False)
    catalog_visibility = models.CharField(
        _("Visibility"), max_length=10, default=VISIBILITY_VISIBLE, choices=VISIBILITY_CHOICES)
    description = models.TextField(_("Description"))
    short_description = models.TextField(_("Short Description"))
    sku = models.CharField(_("SKU"), max_length=255, default="", blank=True, null=True)

    price = models.CharField(_("Price"), max_length=255, default="", blank=True, null=True)
    regular_price = models.CharField(_("Regular Price"), max_length=255,
                                     default="", blank=True, null=True)
    sale_price = models.CharField(_("Sale Price"), max_length=255,
                                  default="", blank=True, null=True)
    date_on_sale_from = models.DateField(_("On Sale From"), blank=True, null=True)
    date_on_sale_to = models.DateField(_("On Sale To"), blank=True, null=True)
    price_html = models.CharField(_("Price HTML"), max_length=1000,
                                  default="", blank=True, null=True)

    on_sale = models.BooleanField(_("On Sale?"), default=False)
    purchasable = models.BooleanField(_("Purchasable?"), default=True)
    total_sales = models.IntegerField(_("Total Sales"), default=0)
    virtual = models.BooleanField(_("Virtual?"), default=False)

    downloadable = models.BooleanField(_("Downloadable?"), default=False)
    download_limit = models.IntegerField(_("Download Limit"), default=-1)
    download_expiry = models.IntegerField(_("Download Expiry"), default=-1)
    download_type = models.CharField(_("Download Type"), max_length=15,
                                     default=DOWNLOADTYPE_STANDARD, choices=DOWNLOADTYPE_CHOICES)
    external_url = models.URLField(_("External URL"), default="", null=True, blank=True)
    button_text = models.CharField(_("Button Text"), max_length=255, default="", null=True, blank=True, help_text=_(
        "Product external button text. Only for external products."))

    tax_status = models.CharField(_("Tax Status"), max_length=15,
                                  default=TAXSTATUS_TAXABLE, choices=TAXSTATUS_CHOICES)
    tax_class = models.CharField(_("Tax Class"), max_length=255, default="", null=True, blank=True)

    manage_stock = models.BooleanField(_("Manage Stock"), default=False)
    stock_quantity = models.IntegerField(_("Stock Quantity"), default=0)
    in_stock = models.BooleanField(_("In Stock?"), default=True)
    backorders = models.CharField(_("Backorders"), max_length=255,
                                  default=BACKORDERS_NO, choices=BACKORDERS_CHOICES)
    backorders_allowed = models.BooleanField(_("Backorders Allowed?"), default=False)
    backordered = models.BooleanField(_("Backordered?"), default=False)
    sold_individually = models.BooleanField(_("Sold Individually?"), default=False)
    weight = models.DecimalField(_("Weight"), max_digits=10, decimal_places=2,
                                 default=0, help_text=_("Product weight in decimal format."))
    shipping_required = models.BooleanField(_("Requires Shipping?"), default=False)
    shipping_taxable = models.BooleanField(_("Taxable Shipping?"), default=False)
    reviews_allowed = models.BooleanField(_("Reviewed Allowed?"), default=True)
    average_rating = models.CharField(
        _("Average Rating"), max_length=15, default="", null=True, blank=True)
    rating_count = models.IntegerField(_("Rating Count"), default=0)
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=_("Parent"))
    purchase_note = models.CharField(
        _("Purchase Note"), max_length=255, default="", null=True, blank=True)
    menu_order = models.IntegerField(_("Menu Order"), default=0)

    #==FOREIGN KEYS==
    # shipping_class	string	Shipping class slug. Shipping classes are used by certain shipping methods to group similar products.
    # shipping_class_id	integer	Shipping class ID. READ-ONLY
    # downloads	array	List of downloadable files. See Downloads properties.
    # dimensions	object	Product dimensions. See Dimensions properties.
    # related_ids	array	List of related products IDs (integer). READ-ONLY
    # upsell_ids	array	List of up-sell products IDs (integer). Up-sells are products which you recommend instead of the currently viewed product, for example, products that are more profitable or better quality or more expensive.
    # cross_sell_ids	array	List of cross-sell products IDs. Cross-sells are products which you promote in the cart, based on the current product.
    # categories	array	List of categories. See Categories properties.
    # tags	array	List of tags. See Tags properties.
    # images	array	List of images. See Images properties
    # attributes	array	List of attributes. See Attributes properties.
    # default_attributes	array	Defaults variation attributes, used only for variations and pre-selected attributes on the frontend. See Default Attributes properties.
    # variations	array	List of variations. See Variations properties
    # grouped_products	array	List of grouped products ID, only for group type products. READ-ONLY

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Product")

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Product")
        ordering = ["name", "code", ]
