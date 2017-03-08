from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models

from django.core.urlresolvers import reverse

from django.db.models import *
from django.db import models as models

from django.utils.translation import ugettext_lazy as _

from django_extensions.db import fields as extension_fields
from django_extensions.db.fields import AutoSlugField

from timezone_field import TimeZoneField
import uuid
from decimal import *

from pyPrintful import pyPrintful
from django.core.exceptions import ObjectDoesNotExist

from storemanager.logger import *
logger = StyleAdapter(logging.getLogger("project"))


class commonBusinessModel(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = DateTimeField(auto_now_add=True, verbose_name=_("Added"))
    date_updated = DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        abstract = True


class bzBrand(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=2)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)

    # Relationship Fields
    vendor = ForeignKey('business.pfStore', blank=True, null=True, )
    outlet = ForeignKey('business.wooStore', blank=True, null=True,)

    class Meta:
        ordering = ('code',)
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        elif self.name:
            return "{}".format(self.name)
        return _("Unknown Brand")

    def get_absolute_url(self):
        return reverse('business:app_store_brand_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:app_store_brand_update', args=(self.pk,))


class bzCreativeCollection(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=3)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)

    # Relationship Fields
    bzbrand = ForeignKey('business.bzBrand', verbose_name=_("Brand"))

    class Meta:
        ordering = ('code',)
        verbose_name = _("Creative Collection")
        verbose_name_plural = _("Creative Collections")

    def __str__(self):
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        elif self.name:
            return "{}".format(self.name)
        return _("Unknown Collection")

    def get_absolute_url(self):
        return reverse(
            'business:business_bzcreativecollection_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse(
            'business:business_bzcreativecollection_update', args=(self.pk,))

    def get_designs(self):
        return bzCreativeDesign.objects.filter(bzcreativecollection=self)
    get_designs.short_description = _("Designs")

    def num_designs(self):
        return self.get_designs().count()
    num_designs.short_description = _("Designs")

    def get_layouts(self):
        return bzCreativeLayout.objects.filter(bzcreativecollection=self)
    get_designs.short_description = _("Layouts")

    def num_layouts(self):
        return self.get_layouts().count()
    num_layouts.short_description = _("Layouts")


class bzCreativeDesign(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=2)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)

    # Relationship Fields
    bzcreativecollection = ForeignKey(
        'business.bzCreativeCollection', verbose_name=_("Collection"))

    class Meta:
        ordering = ('bzcreativecollection__code', 'code',)
        verbose_name = _("Creative Design")
        verbose_name_plural = _("Creative Designs")

    def __str__(self):
        rv = []
        if self.bzcreativecollection:
            if self.bzcreativecollection.code:
                rv.append(self.bzcreativecollection.code + "-")
        if self.code:
            rv.append(self.code)

        if self.bzcreativecollection:
            if self.bzcreativecollection.code:
                rv.append(" / " + self.bzcreativecollection.name)
        if self.name:
            rv.append(" / " + self.name)

        if rv:
            return "".join(rv)
        return _("Unknown Design")

    def get_absolute_url(self):
        return reverse('business:business_bzcreativedesign_detail',
                       args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_bzcreativedesign_update',
                       args=(self.pk,))

    def get_products(self):
        return bzProduct.objects.filter(bzDesign=self)
    get_products.short_description = _("Products")

    def num_products(self):
        return self.get_products().count()
    num_products.short_description = _("Products")


class bzCreativeLayout(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=2)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)

    # Relationship Fields
    bzcreativecollection = ForeignKey(
        'business.bzCreativeCollection', verbose_name=_("Collection"))

    class Meta:
        ordering = ('bzcreativecollection__code', 'code',)
        verbose_name = _("Creative Layout")
        verbose_name_plural = _("Creative Layouts")

    def __str__(self):
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        elif self.name:
            return "{}".format(self.name)
        return _("Unknown Design")

    def get_absolute_url(self):
        return reverse('business:business_bzcreativelayout_detail',
                       args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_bzcreativelayout_update',
                       args=(self.pk,))

    def get_products(self):
        return bzProduct.objects.filter(bzLayout=self)
    get_products.short_description = _("Products")

    def num_products(self):
        return self.get_products().count()
    num_products.short_description = _("Products")


class bzCreativeRendering(commonBusinessModel):

    # Fields

    # Relationship Fields
    bzcreativedesign = ForeignKey(
        'business.bzCreativeDesign', verbose_name=_("Design"))
    bzcreativelayout = ForeignKey(
        'business.bzCreativeLayout', verbose_name=_("Layout"))

    class Meta:
        ordering = ('bzcreativedesign__code', 'bzcreativelayout__code',)
        verbose_name = _("Creative Rendering")
        verbose_name_plural = _("Creative Renderings")

    def __str__(self):
        if self.bzcreativedesign and self.bzcreativelayout:
            return "{} - {}".format(self.bzcreativedesign.code,
                                    self.bzcreativelayout.code)
        return _("Unknown Rendering")

    def get_absolute_url(self):
        return reverse('business:business_bzcreativerendering_detail',
                       args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_bzcreativerendering_update',
                       args=(self.pk,))


class bzProduct(commonBusinessModel):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_CHOICES = (
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLIC, "Public"),
    )
    # Fields
    code = CharField(_("Code"), max_length=64,
                     default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    status = CharField(_("Status"), max_length=32,
                       default=STATUS_DRAFT, choices=STATUS_CHOICES)

    # Relationship Fields
    bzDesign = ForeignKey('business.bzCreativeDesign',
                          verbose_name=_("Design"))
    bzLayout = ForeignKey('business.bzCreativeLayout',
                          verbose_name=_("Layout"), null=True, blank=True)
    pfProduct = ForeignKey('business.pfCatalogProduct',
                           verbose_name=_("Vendor Product"),
                           blank=True, null=True, )
    wooProduct = ForeignKey('business.wooProduct',
                            verbose_name=_("Outlet Product"),
                            blank=True, null=True, )
    pfSyncProduct = ForeignKey('business.pfSyncProduct',
                               verbose_name=_("Sync Product"),
                               blank=True, null=True, )

    class Meta:
        ordering = ('code',)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        elif self.name:
            return "{}".format(self.name)
        return _("Unknown Product")

    def get_absolute_url(self):
        return reverse('business:business_bzproduct_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_bzproduct_update', args=(self.pk,))

    def get_variants(self):
        return bzProductVariant.objects.filter(bzproduct=self)
    get_variants.short_description = _("Variants")

    def num_variants(self):
        return self.get_variants().count()
    num_variants.short_description = _("Variants")


class bzProductVariant(commonBusinessModel):

    # Fields
    code = CharField(verbose_name=_("Code"), max_length=64,
                     default="", blank=True, null=True)
    is_active = BooleanField(verbose_name=_("Is Active"), default=True)

    # Relationship Fields
    bzproduct = ForeignKey('business.bzProduct', verbose_name=_("Product"))
    pfcatalogvariant = ForeignKey(
        'business.pfCatalogVariant', verbose_name=_("Vendor Variant"), )
    pfcolor = ForeignKey('business.pfCatalogColor',
                         verbose_name=_("Color"), blank=True, null=True, )
    pfsize = ForeignKey('business.pfCatalogSize',
                        verbose_name=_("Size"), blank=True, null=True, )
    price = DecimalField(_("Price"), max_digits=5,
                         decimal_places=2, default=Decimal("0"))

    class Meta:
        ordering = ('bzproduct', 'pfsize', 'pfcolor',)
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        rv = []
        if self.bzproduct.code:
            rv.append(self.bzproduct.code)
        if self.bzproduct:
            rv.append(self.bzproduct.name)
        return " - ".join(rv)

    def get_absolute_url(self):
        return reverse('business:business_bzproductvariant_detail',
                       args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_bzproductvariant_update',
                       args=(self.pk,))


class wooAttribute(commonBusinessModel):
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

    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    wid = CharField(_("WP ID"), max_length=16,
                    default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    slug = CharField(_("Slug"), max_length=255,
                     default="", blank=True, null=True)
    type = CharField(_("Type"), max_length=255, default="",
                     blank=True, null=True, choices=TYPE_CHOICES)
    has_archives = BooleanField(_("Has Archives?"), default=False)

    # Relationship Fields
    store = ForeignKey('business.wooStore', blank=True, null=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Attribute")
        verbose_name_plural = _("WP Attributes")

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('business:business_wooattribute_detail',
                       args=(self.slug,))

    def get_update_url(self):
        return reverse('business:business_wooattribute_update',
                       args=(self.slug,))


class wooCategory(commonBusinessModel):
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
    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    wid = IntegerField(_("WP ID"), default=0, blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    slug = CharField(_("Slug"), max_length=255,
                     default="", blank=True, null=True)
    parent = IntegerField(_("Parent ID"), default=0)
    description = TextField(
        _("Description"), default="", blank=True, null=True)
    display = CharField(_("Display"), max_length=255,
                        default=DISPLAY_DEFAULT, choices=DISPLAY_CHOICES)
    count = IntegerField(_("Count"), default=0)
    image_id = IntegerField(_("Image ID"), default=0)
    image_date_created = CharField(_("Image Created"), max_length=255,
                                   default="", blank=True, null=True)

    # Relationship Fields
    store = ForeignKey('business.wooStore', blank=True, null=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Category")
        verbose_name_plural = _("WP Categories")

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('business:business_woocategory_detail',
                       args=(self.slug,))

    def get_update_url(self):
        return reverse('business:business_woocategory_update',
                       args=(self.slug,))


class wooImage(commonBusinessModel):

    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    wid = CharField(_("WP ID"), max_length=16, default="", blank=True,
                    null=True, help_text=_(
        "Image ID (attachment ID). In write-mode used to attach pre-existing images."))
    date_created = DateField(_("Date Created"), help_text=_(
        "READONLY. The date the product was created, in the sites timezone."),
        blank=True, null=True)
    alt = CharField(_("Alt"), max_length=255,
                    default="", blank=True, null=True)
    position = IntegerField(_("Position"), default=0, help_text=_(
        "Image position. 0 means that the image is featured."))

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Image")
        verbose_name_plural = _("WP Images")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('business:business_wooimage_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_wooimage_update', args=(self.pk,))


class wooProduct(commonBusinessModel):

    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    wid = CharField(_("WP ID"), max_length=16,
                    default="", blank=True, null=True, )
    slug = CharField(_("Slug"), max_length=255,
                     default="", blank=True, null=True)
    permalink = URLField(_("Permalink"), blank=True)
    date_created = DateField(_("Date Created"), help_text=_(
        "READONLY. The date the product was created, in the sites timezone."),
        blank=True, null=True)
    dimension_length = DecimalField(
        _("Length"), max_digits=10, decimal_places=2, default=0)
    dimension_width = DecimalField(
        _("Width"), max_digits=10, decimal_places=2, default=0)
    dimension_height = DecimalField(
        _("Height"), max_digits=10, decimal_places=2, default=0)
    weight = DecimalField(_("Weight"), help_text=_(
        "Product weight in decimal format."),
        max_digits=10, decimal_places=2,
        default=0)
    reviews_allowed = BooleanField(_("Reviewed Allowed?"), help_text=_(
        "Allow reviews. Default is true."), default=True)

    # Relationship Fields
    woostore = ForeignKey('business.wooStore', verbose_name=_(
        "Store"), blank=True, null=True)
    shipping_class = ForeignKey(
        'business.wooShippingClass', null=True, blank=True)
    tags = ManyToManyField(
        'business.wooTag', verbose_name=_("Tags"), blank=True)
    images = ManyToManyField(
        'business.wooImage', verbose_name=_("Images"), blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Product")
        verbose_name_plural = _("WP Products")

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('business:business_wooproduct_detail',
                       args=(self.slug,))

    def get_update_url(self):
        return reverse('business:business_wooproduct_update',
                       args=(self.slug,))


class wooShippingClass(commonBusinessModel):

    # Fields
    wid = CharField(_("WP ID"), max_length=64,
                    default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    slug = CharField(_("Slug"), max_length=255,
                     default="", blank=True, null=True)
    description = TextField(
        _("Description"), default="", blank=True, null=True)
    count = IntegerField(_("Count"), default=0)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Shipping Class")
        verbose_name_plural = _("WP Shipping Classes")

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse(
            'business:business_wooshippingclass_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse(
            'business:business_wooshippingclass_update', args=(self.slug,))


class wooStore(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=16, default="", blank=True, null=True,
                     help_text=_("Generally, a two-character uppercase code. Used in SKUs."))
    base_url = URLField(_("Base URL"), default="", blank=True, null=True, help_text=_(
        "Include the schema and FQDN only (e.g., 'https://example.com'). No trailing slash."))
    consumer_secret = CharField(
        _("Consumer Secret"), max_length=43, blank=True, null=True)
    timezone = TimeZoneField(default='America/New_York')
    verify_ssl = BooleanField(_("Verify SSL?"), default=True, help_text=_(
        "Uncheck this if you are using a self-signed SSL certificate to disable ssl verification."))

    class Meta:
        ordering = ('code',)
        verbose_name = _("WP Store")
        verbose_name_plural = _("WP Stores")

    def __str__(self):
        rv = []
        if self.code and self.base_url:
            return "{} - {}".format(self.code, self.base_url)
        elif self.code:
            return "{}".format(self.code)
        return _("Unknown Store")

    def get_absolute_url(self):
        return reverse('business:app_store_wp_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:app_store_wp_update', args=(self.pk,))


class wooTag(commonBusinessModel):

    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    wid = IntegerField(_("WP ID"), default=0)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    slug = CharField(_("Slug"), max_length=255,
                     default="", blank=True, null=True)
    description = TextField(
        _("Description"), default="", blank=True, null=True)
    count = IntegerField(_("Count"), default=0)

    # Relationship Fields
    store = ForeignKey('business.wooStore', blank=True, null=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Tag")
        verbose_name_plural = _("WP Tags")

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('business:business_wootag_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('business:business_wootag_update', args=(self.slug,))


class wooTerm(commonBusinessModel):

    # Fields
    wid = CharField(_("WP ID"), max_length=16,
                    default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    slug = CharField(_("Slug"), max_length=255,
                     default="", blank=True, null=True)
    menu_order = IntegerField(_("Menu Order"), default=0)
    count = IntegerField(_("Count"), default=0)
    wr_tooltip = CharField(_("WR Tooltip"), max_length=255,
                           default="", blank=True, null=True)
    wr_label = CharField(_("WR Label"), max_length=255,
                         default="", blank=True, null=True)

    # Relationship Fields
    productattribute = ForeignKey('business.wooAttribute', verbose_name=_(
        "Product Attribute"), blank=True, null=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Term")
        verbose_name_plural = _("WP Terms")

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('business:business_wooterm_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('business:business_wooterm_update', args=(self.slug,))


class wooVariant(commonBusinessModel):

    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    wid = CharField(_("WP ID"), max_length=16,
                    default="", blank=True, null=True, )
    date_created = DateField(_("Date Created"), help_text=_(
        "READONLY. The date the product was created, in the sites timezone."), blank=True, null=True)
    permalink = URLField(_("Permalink"), blank=True)
    sku = CharField(_("SKU"), help_text=_("Unique identifier."),
                    max_length=255, default="", blank=True, null=True)
    price = CharField(_("Price"), help_text=_(
        "READONLY. Current product price. This is set from regular_price and sale_price."), max_length=255, default="", blank=True, null=True)
    dimension_length = DecimalField(
        _("Length"), max_digits=10, decimal_places=2, default=0)
    dimension_width = DecimalField(
        _("Width"), max_digits=10, decimal_places=2, default=0)
    dimension_height = DecimalField(
        _("Height"), max_digits=10, decimal_places=2, default=0)
    weight = DecimalField(_("Weight"), help_text=_(
        "Product weight in decimal format."), max_digits=10, decimal_places=2, default=0)

    # Relationship Fields
    shipping_class = ForeignKey(
        'business.wooShippingClass', null=True, blank=True)
    images = ManyToManyField(
        'business.wooImage', verbose_name=_("Images"), blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Variant")
        verbose_name_plural = _("WP Variants")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('business:business_woovariant_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_woovariant_update', args=(self.pk,))


class wpMedia(commonBusinessModel):
    STATUSBOOL_OPEN = 'open'
    STATUSBOOL_CLOSED = 'closed'
    STATUSBOOL_CHOICES = (
        (STATUSBOOL_OPEN, _("Open")),
        (STATUSBOOL_CLOSED, _("Closed")),
    )

    MEDIATYPE_IMAGE = "image"
    MEDIATYPE_FILE = "file"
    MEDIATYPE_CHOICES = (
        (MEDIATYPE_IMAGE, _("Image")),
        (MEDIATYPE_FILE, )
    )

    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    alt_text = CharField(_("Alternate Text"), max_length=255,
                         default="", blank=True, null=True)
    width = IntegerField(_("Width"), default=0)
    height = IntegerField(_("Height"), default=0)
    file = CharField(_("File"), max_length=255,
                     default="", blank=True, null=True)
    author = IntegerField(_("Author"), default=0)
    mime_type = CharField(_("MIME Type"), max_length=255,
                          default="", blank=True, null=True)
    comment_status = CharField(_("Comment Status"), max_length=255,
                               default=STATUSBOOL_OPEN, choices=STATUSBOOL_CHOICES)
    wid = CharField(_("ID"), max_length=16, default="", blank=True, null=True)
    source_url = URLField(_("Source URL"), blank=True, null=True)
    template = CharField(_("Template"), max_length=255,
                         default="", blank=True, null=True)
    ping_status = CharField(_("Ping Status"), max_length=255,
                            default=STATUSBOOL_OPEN, choices=STATUSBOOL_CHOICES)
    caption = CharField(_("Caption"), max_length=255,
                        default="", blank=True, null=True)
    link = URLField(_("Link"), default="", blank=True, null=True)
    slug = CharField(_("Slug"), max_length=255, blank=True, null=True)
    modified = DateTimeField(_("Modified"), blank=True, null=True)
    guid = CharField(_("GUID"), max_length=255,
                     default="", blank=True, null=True)
    description = TextField(
        _("Description"), default="", blank=True, null=True)
    modified_gmt = DateTimeField(_("Modified GMT"), blank=True, null=True)
    title = CharField(_("Title"), max_length=255,
                      default="", blank=True, null=True)
    date_gmt = DateTimeField(_("Date GMT"), blank=True, null=True)
    type = CharField(_("Type"), max_length=64,
                     default="", blank=True, null=True)

    # Relationship Fields
    woostore = ForeignKey('business.woostore', blank=True, null=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Media")
        verbose_name_plural = _("WP Media")

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('business:business_wpmedia_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('business:business_wpmedia_update', args=(self.slug,))


class wpMediaSize(commonBusinessModel):

    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    file = CharField(_("File"), max_length=255,
                     default="", blank=True, null=True)
    mime_type = CharField(_("MIME Type"), max_length=255,
                          default="", blank=True, null=True)
    width = IntegerField(_("Width"), default=0)
    height = IntegerField(_("Height"), default=0)
    source_url = URLField(_("Source URL"), default="", blank=True, null=True)

    # Relationship Fields
    wpmedia = ForeignKey('business.wpMedia', verbose_name=_("Media"))

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("WP Media Size")
        verbose_name_plural = _("WP Media Sizes")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('business:business_wpmediasize_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_wpmediasize_update', args=(self.pk,))


class pfCountry(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=50,
                     default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)

    class Meta:
        ordering = ('code',)
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        elif self.name:
            return "{}".format(self.name)
        return _("Unknown Country")

    def get_absolute_url(self):
        return reverse('business:business_pfcountry_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_pfcountry_update', args=(self.pk,))

    @staticmethod
    def api_pull(store=None, key=None):
        """
        Update the Country and State objects from the Printful API.

        :param store: Optional bzStore object. If not provided, method will
                attempt to use the first store from the database if it exists.
        :param key: If a key is provided, then it is used instead of store.
                This is especially useful for when you're first creating a
                store, and so avoids a race condition.
        """
        if key:
            api = pyPrintful(key=key)
        else:
            _storeObj = pfStore.get_store(store)
            api = pyPrintful(key=_storeObj.key)

        countries = api.get_countries_list()
        for c in countries:
            cObj, cCreated = pfCountry.objects.update_or_create(
                code=c['code'],
                defaults={
                    'name': c['name']
                }
            )
            if c['states']:
                for s in c['states']:
                    sObj, sCreated = pfState.objects.update_or_create(
                        code=s['code'],
                        pfcountry=cObj,
                        defaults={
                            'name': s['name'],
                        }
                    )

    def get_states(self):
        return pfState.objects.filter(pfcountry=self)
    get_states.short_description = _("States")

    def num_states(self):
        return self.get_states().count()
    num_states.short_description = _("States")


class pfState(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=50,
                     default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    # Relationship Fields
    pfcountry = ForeignKey('business.pfCountry', verbose_name=_("Country"))

    class Meta:
        ordering = ('pfcountry__code', 'code',)
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        elif self.name:
            return "{}".format(self.name)
        return _("Unknown State")

    def get_absolute_url(self):
        return reverse('business:business_pfstate_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_pfstate_update', args=(self.pk,))


class pfSyncProduct(commonBusinessModel):

    # Fields
    pid = CharField(_("Printful ID"), max_length=200,
                    default="", blank=True, null=True)
    external_id = CharField(_("External ID"), max_length=200,
                            default="", blank=True, null=True)
    variants = IntegerField(_("Variant Count"), default=0)
    synced = IntegerField(_("Synced"), default=0)

    # Relationship Fields
    pfstore = ForeignKey('business.pfStore', verbose_name=_("Store"))

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("Sync Product")
        verbose_name_plural = _("Sync Products")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('business:business_pfsyncproduct_detail',
                       args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_pfsyncproduct_update',
                       args=(self.pk,))


class pfSyncVariant(commonBusinessModel):

    # Fields
    pid = CharField(_("Printful ID"), max_length=200,
                    default="", blank=True, null=True)
    external_id = CharField(_("External ID"), max_length=200,
                            default="", blank=True, null=True)
    synced = BooleanField(_("Synced"), default=False)

    # Relationship Fields
    pfsyncproduct = ForeignKey(
        'business.pfSyncProduct', verbose_name=_("Sync Product"))
    files = ManyToManyField('business.pfPrintFile', blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("Sync Variant")
        verbose_name_plural = _("Sync Variants")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('business:business_pfsyncvariant_detail',
                       args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_pfsyncvariant_update',
                       args=(self.pk,))


class pfSyncItemOption(commonBusinessModel):

    # Fields
    pid = CharField(_("Printful ID"), max_length=200,
                    default="", blank=True, null=True)
    value = CharField(_("Value"), max_length=255,
                      default="", blank=True, null=True)

    # Relationship Fields
    pfsyncvariant = ForeignKey('business.pfSyncVariant', )

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("Sync Item Option")
        verbose_name_plural = _("Sync Item Options")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse(
            'business:business_pfsyncitemoption_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse(
            'business:business_pfsyncitemoption_update', args=(self.pk,))


class pfCatalogColor(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=3,
                     default="", blank=True, null=True)
    label = CharField(_("Color"), max_length=255,
                      default="", blank=True, null=True)
    label_clean = CharField(_("Clean Label"), max_length=255,
                            default="", blank=True, null=True)
    hex_code = CharField(_("Color Hex Code"), max_length=255,
                         default="", blank=True, null=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("Printful Color")
        verbose_name_plural = _("Printful Colors")

    def __str__(self):
        rv = []
        if self.code:
            rv.append(self.code)
        if self.label_clean:
            rv.append(self.label_clean)
        elif self.label:
            rv.append(self.label)
        if rv:
            return " - ".join(rv)
        return _("Unknown Color")

    def get_absolute_url(self):
        return reverse(
            'business:business_pfcatalogcolor_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse(
            'business:business_pfcatalogcolor_update', args=(self.pk,))


class pfCatalogSize(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=3,
                     default="", blank=True, null=True)
    label = CharField(_("Size"), max_length=255,
                      default="", blank=True, null=True)
    label_clean = CharField(_("Clean Label"), max_length=255,
                            default="", blank=True, null=True)
    sort_group = CharField(_("Sort Group"), max_length=2,
                           default="", blank=True, null=True)
    sort_order = CharField(_("Sort Order"), max_length=16,
                           default="", blank=True, null=True)

    class Meta:
        ordering = ('sort_group', 'sort_order',)
        verbose_name = _("Printful Size")
        verbose_name_plural = _("Printful Sizes")

    def __str__(self):
        rv = []
        if self.code:
            rv.append(self.code)
        if self.label_clean:
            rv.append(self.label_clean)
        elif self.label:
            rv.append(self.label)
        if rv:
            return " - ".join(rv)
        return _("Unknown Size")

    def get_absolute_url(self):
        return reverse('business:business_pfcatalogsize_detail',
                       args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_pfcatalogsize_update',
                       args=(self.pk,))


class pfCatalogFileSpec(commonBusinessModel):
    COLORSYSTEM_RGB = 'R'
    COLORSYSTEM_CMYK = 'Y'
    COLORSYSTEM_CHOICES = (
        (COLORSYSTEM_RGB, "RGB"),
        (COLORSYSTEM_CMYK, "CMYK"),
    )
    # Fields
    name = CharField(_("Name"), max_length=5,
                     default="", blank=True, null=True)
    note = TextField(_("Note"), default="", blank=True, null=True)
    width = IntegerField(_("Width"), default=0)
    height = IntegerField(_("Height"), default=0)
    width_in = DecimalField(_("Width (in)"), default=0,
                            decimal_places=2, max_digits=4)
    height_in = DecimalField(_("Height (in)"), default=0,
                             decimal_places=2, max_digits=4)
    ratio = CharField(_("Ratio"), max_length=32,
                      default="", blank=True, null=True)
    colorsystem = CharField(_("Color System"), max_length=1,
                            default="R", choices=COLORSYSTEM_CHOICES)

    class Meta:
        ordering = ('name',)
        verbose_name = _("Printful File Spec")
        verbose_name_plural = _("Printful File Specs")

    def __str__(self):
        if self.name:
            return self.name
        return _("Unknown File Spec")

    def get_absolute_url(self):
        return reverse(
            'business:business_pfcatalogfilespec_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse(
            'business:business_pfcatalogfilespec_update', args=(self.pk,))


class pfCatalogFileType(commonBusinessModel):

    # Fields
    pid = CharField(_("Printful ID"), max_length=255,
                    default="", blank=True, null=True)
    title = CharField(_("Title"), max_length=255,
                      default="", blank=True, null=True)
    additional_price = CharField(_("Additional Price"), max_length=100,
                                 default="", blank=True, null=True)

    # Relationship Fields
    pfcatalogvariant = ForeignKey(
        'business.pfCatalogVariant', verbose_name=_("Variant"))

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("Printful File Type")
        verbose_name_plural = _("Printful File Types")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse(
            'business:business_pfcatalogfiletype_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse(
            'business:business_pfcatalogfiletype_update', args=(self.pk,))


class pfCatalogOptionType(commonBusinessModel):

    # Fields
    pid = CharField(_("Printful ID"), max_length=255,
                    default="", blank=True, null=True)
    title = CharField(_("Title"), max_length=255,
                      default="", blank=True, null=True)
    type = CharField(_("Type"), max_length=255,
                     default="", blank=True, null=True)
    additional_price = CharField(_("Additional Price"), max_length=100,
                                 default="", blank=True, null=True)

    # Relationship Fields
    pfcatalogvariant = ForeignKey('business.pfCatalogVariant', )

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("Printful Option Type")
        verbose_name_plural = _("Printful Option Types")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse(
            'business:business_pfcatalogoptiontype_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse(
            'business:business_pfcatalogoptiontype_update', args=(self.pk,))


class pfCatalogProduct(commonBusinessModel):

    # Fields
    is_active = BooleanField(_("Is Active?"), default=True)
    pid = CharField(_("Printful ID"), max_length=255,
                    default="", blank=True, null=True)
    type = CharField(_("Type"), max_length=255,
                     default="", blank=True, null=True)
    brand = CharField(_("Brand"), max_length=255,
                      default="", blank=True, null=True)
    model = CharField(_("Model"), max_length=255,
                      default="", blank=True, null=True)
    image = CharField(_("Image"), max_length=255,
                      default="", blank=True, null=True)
    variant_count = IntegerField(_("Variants"), default=0)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("Printful Product")
        verbose_name_plural = _("Printful Products")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse(
            'business:business_pfcatalogproduct_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse(
            'business:business_pfcatalogproduct_update', args=(self.pk,))


class pfCatalogVariant(commonBusinessModel):

    # Fields
    is_active = BooleanField(verbose_name=_("Is Active"), default=True)
    pid = CharField(_("Printful ID"), max_length=16,
                    default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    image = CharField(_("Image"), max_length=255,
                      default="", blank=True, null=True)
    price = CharField(_("Price"), max_length=255,
                      default="", blank=True, null=True)
    in_stock = BooleanField(_("In Stock"), default=False)
    weight = DecimalField(_("Weight (oz)"), default=0, blank=True,
                          null=True, decimal_places=2, max_digits=5)

    # Relationship Fields
    pfsize = ForeignKey('business.pfCatalogSize', blank=True,
                        null=True, verbose_name=_("Size"))

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("Printful Variant")
        verbose_name_plural = _("Printful Variants")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse(
            'business:business_pfcatalogvariant_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse(
            'business:business_pfcatalogvariant_update', args=(self.pk,))


class pfStore(commonBusinessModel):

    # Fields
    code = CharField(_("Code"), max_length=50,
                     default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    pid = IntegerField(_("Printful ID"), default=0)
    website = CharField(_("Website"), max_length=255,
                        default="", blank=True, null=True)
    created = CharField(_("Created"), max_length=255,
                        default="", blank=True, null=True)
    key = CharField(_("API Key"), max_length=64, default="", blank=True)
    return_address = ForeignKey("business.pfAddress", verbose_name=_(
        "Return Address"), related_name="returnaddress", blank=True, null=True)
    billing_address = ForeignKey("business.pfAddress", verbose_name=_(
        "Billing Address"), related_name="billingaddress", blank=True, null=True)
    payment_type = CharField(_("Payment Card Type"),
                             max_length=64, default="", blank=True, null=True)
    payment_number_mask = CharField(
        _("Payment Card Type"), max_length=64, default="", blank=True, null=True)
    payment_expires = CharField(
        _("Payment Card Type"), max_length=64, default="", blank=True, null=True)
    packingslip_email = EmailField(
        _("Packing Slip Email"), default="", blank=True, null=True)
    packingslip_phone = CharField(
        _("Packing Slip Phone"), max_length=64, default="", blank=True, null=True)
    packingslip_message = CharField(
        _("Packing Slip Message"), max_length=255, default="", blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _("Printful Store")
        verbose_name_plural = _("Printful Stores")

    def __str__(self):
        rv = []
        if self.code and self.name:
            return "{} - {}".format(self.code, self.name)
        elif self.code:
            return "{}".format(self.code)
        return _("Unknown Store")

    def get_absolute_url(self):
        return reverse('business:app_store_pf_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:app_store_pf_update', args=(self.pk,))

    def has_auth(self):
        return True if self.key else False
    has_auth.short_description = _("Auth?")
    has_auth.boolean = True

    def save(self, *args, **kwargs):
        logger.debug('Method: pfStore.save() Called')
        if self.pid == 0:
            if pfCountry.objects.all().count() == 0:
                pfCountry.api_pull(key=self.key)
            self.api_pull()
        self.api_push()
        self.api_pull()
        super(pfStore, self).save(*args, **kwargs)

    @staticmethod
    def get_store(store=None):
        """
        Gets a 'default' Printful store, generally for use with the Printful API
        methods on other related objects. If a store is provided, then it is
        validated and returned. Otherwise, this method will attempt to grab the
        first Printful store object in the database and return that.

        If no stores are in the database, then this method will raise an exception.
        The wrapping method will need to catch this and respond appropriately.

        :param store: Optional. pfStore object. Will validate that it is a valid
                pfStore object and return it back.
        """
        if type(store) is pfStore and store.has_auth():
            return store
        else:
            store = pfStore.objects.exclude(
                key__isnull=True).exclude(key__exact='').first()
            if store:
                return store
        raise ObjectDoesNotExist(
            "Either provide a store object or add at least one pfStore with an API key to the database.")

    def api_pull(self):
        """
        Update current store with data from Printful API.
        """
        if not self.has_auth():
            raise Exception("This store is missing the API Key.")

        # TODO Handle states/countries lookup Exceptions

        api = pyPrintful(key=self.key)
        sData = api.get_store_info()
        print(sData)
        print(api._store['last_response_raw'])

        self.website = sData['website']
        self.name = sData['name']
        self.pid = sData['id']
        self.created = sData['created']

        self.packingslip_phone = sData['packing_slip']['phone']
        self.packingslip_email = sData['packing_slip']['email']
        self.packingslip_message = sData['packing_slip']['message']

        self.payment_type = sData['payment_card']['type']
        self.payment_number_mask = sData['payment_card']['number_mask']
        self.payment_expires = sData['payment_card']['expires']

        if sData['billing_address']:
            _state = pfState.objects.get(
                code=sData['billing_address']['state_code'])
            _country = pfCountry.objects.get(
                code=sData['billing_address']['country_code'])
            self.billing_address, created = pfAddress.objects.update_or_create(
                name=sData['billing_address']['name'],
                company=sData['billing_address']['company'],
                address1=sData['billing_address']['address1'],
                address2=sData['billing_address']['address2'],
                city=sData['billing_address']['city'],
                zip=sData['billing_address']['zip'],
                phone=sData['billing_address']['phone'],
                email=sData['billing_address']['email'],
                state=_state,
                country=_country,
                defaults={}
            )

        if sData['return_address']:
            _state = pfState.objects.get(
                code=sData['return_address']['state_code'])
            _country = pfCountry.objects.get(
                code=sData['return_address']['country_code'])

            self.return_address, created = pfAddress.objects.update_or_create(
                name=sData['return_address']['name'],
                company=sData['return_address']['company'],
                address1=sData['return_address']['address1'],
                address2=sData['return_address']['address2'],
                city=sData['return_address']['city'],
                zip=sData['return_address']['zip'],
                phone=sData['return_address']['phone'],
                email=sData['return_address']['email'],
                state=_state,
                country=_country,
                defaults={}
            )

    def api_push(self):
        """
        Pushes the only data available to update via the API: packing slip info.
        """
        if not self.has_auth():
            raise Exception("This store is missing the API Key.")
        data = {
            'email': self.packingslip_email,
            'phone': self.packingslip_phone,
            'message': self.packingslip_message,
        }
        api = pyPrintful(key=self.key)
        api.put_store_packingslip(data)


class pfPrintFile(commonBusinessModel):

    # Fields
    pid = IntegerField(_("Printful ID"), default=0)
    type = CharField(_("Type"), max_length=255,
                     default="", blank=True, null=True)
    hash = CharField(_("Hash"), max_length=255,
                     default="", blank=True, null=True)
    url = CharField(_("URL"), max_length=255,
                    default="", blank=True, null=True)
    filename = CharField(_("Filename"), max_length=255,
                         default="", blank=True, null=True)
    mime_type = CharField(_("MIME Type"), max_length=255,
                          default="", blank=True, null=True)
    size = IntegerField(_("Size"), default=0)
    width = IntegerField(_("Width"), default=0)
    height = IntegerField(_("Height"), default=0)
    dpi = IntegerField(_("DPI"), default=0)
    status = CharField(_("Status"), max_length=255,
                       default="", blank=True, null=True)
    created = CharField(_("Created"), max_length=255,
                        default="", blank=True, null=True)
    thumbnail_url = CharField(
        _("Thumbnail URL"), max_length=255, default="", blank=True, null=True)
    visible = BooleanField(_("Visible"), default=False)

    # Relationship Fields
    pfstore = models.ForeignKey('business.pfStore', )

    class Meta:
        ordering = ('-created',)
        verbose_name = _("Printful File")
        verbose_name_plural = _("Printful Files")

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('business:business_pfprintfile_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('business:business_pfprintfile_update', args=(self.pk,))


class pfAddress(commonBusinessModel):
    # Fields
    name = CharField(_("Name"), max_length=255,
                     default="", blank=True, null=True)
    company = CharField(_("Company"), max_length=255,
                        default="", blank=True, null=True)
    address1 = CharField(_("Address 1"), max_length=255,
                         default="", blank=True, null=True)
    address2 = CharField(_("Address 2"), max_length=255,
                         default="", blank=True, null=True)
    city = CharField(_("City"), max_length=255,
                     default="", blank=True, null=True)
    state = ForeignKey("business.pfState", verbose_name=_(
        "State"), blank=True, null=True)
    country = ForeignKey("business.pfCountry", verbose_name=_(
        "Country"), blank=True, null=True)
    zip = CharField(_("Postal Code"), max_length=24,
                    default="", blank=True, null=True)
    phone = CharField(_("Phone"), max_length=24,
                      default="", blank=True, null=True)
    email = EmailField(_("Email"), default="", blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        if self.name and self.company:
            return ", ".join([self.name, self.company])
        return "Unnamed Address"

    def asHTML(self):
        """
        Returns an HTML div, formatted in a 'standard' way:

            Name
            Company
            Address1
            Address2
            Zip City, State
            Country
            Tel: <Phone>
            E-Mail: <Email>

        """
        rv = []
        rv.append("<div class='element-address'>")
        if self.name:
            rv.append(self.name + "<br/>")
        if self.company:
            rv.append(self.company + "<br/>")
        if self.address1:
            rv.append(self.address1 + "<br/>")
        if self.address2:
            rv.append(self.address2 + "<br/>")
        if self.zip:
            rv.append(self.zip + " ")
        if self.city:
            rv.append(self.city + ", ")
        if self.state:
            rv.append(self.state.code)
        if self.country:
            rv.append("<br/>" + self.country.name)
        if self.phone:
            rv.append("<br/>Tel: " + self.phone)
        if self.email:
            rv.append(
                "<br/>Email: <a href='mailto:[]'>[]</a>".replace('[]', self.email))
        rv.append("</div>")
        return "".join(rv)
