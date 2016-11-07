from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
import colorsys
import uuid

class PODVendor(models.Model):
    """( PODVendor description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(_("Short Code"), max_length=3, default="", blank=True)

    name = models.CharField(_("Name"), max_length=64, default="", blank=True)

    consumer_url = models.URLField(_("Consumer URL"), blank=True, null=True)
    dashboard_url = models.URLField(_("Admin Dashboard URL"), blank=True, null=True)
    apibase_url = models.URLField(_("API Base URL"), blank=True, null=True)

    api_key = models.CharField(_("API Key"), max_length=64, default="", blank=True)
    api_hash = models.CharField(_("API Hash"), max_length=96, default="", blank=True)

    def __str__(self):
        if self.name:
            return str(self.name)
        return u'POD Vendor'

    class Meta:
        verbose_name = "POD Vendor"
        verbose_name_plural = "POD Vendors"
    def has_key(self):
        return True if self.api_key else False
    has_key.short_description='Has API Key?'
    has_key.boolean = True

class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    image_height = models.CharField(blank=True, null=True, default="", max_length=100)
    image_width = models.CharField(blank=True, null=True, default="", max_length=100)
    image = models.ImageField(verbose_name="Brand Logo", upload_to="brand/",
                              blank=True, null=True,
                              height_field='image_height', width_field="image_width")

    consumer_url = models.URLField(_("Consumer URL"), default="", blank=True, null=True)
    wholesale_url = models.URLField(_("Wholesale URL"), default="", blank=True, null=True)

    description = models.TextField(blank=True, default="")

    class Meta:
        ordering = ('name',)
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        if self.name:
            return self.name
        return u'Brand'

    def num_vendors(self):
        return VendorBrand.objects.filter(master_brand=self).count()
    num_vendors.short_description = "Vendor Count"

    def has_logo(self):
        if self.image:
            return True
        return False
    has_logo.boolean = True
    has_logo.short_description = "Logo?"

    def has_description(self):
        if self.description:
            return True
        return False
    has_description.boolean = True
    has_description.short_description = "Description?"

    def get_num_products(self):
        return Product.objects.filter(brand=self).count()
    get_num_products.short_description="Product Count"

    def get_products(self):
        return Product.objects.filter(brand=self)
    get_products.short_description="Products"

class VendorBrand(models.Model):
    """( VendorBrand description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=255, default="", blank=True)
    vendor = models.ForeignKey(PODVendor, null=True, blank=True)
    vendor_key = models.CharField(_("Vendor ID"), null=True, blank=True, max_length=12, default="")
    master_brand = models.ForeignKey(Brand, null=True, blank=True)
    def num_products(self):
        return VendorProduct.objects.filter(brand=self).count()
    num_products.short_description="Vendor Products"
    def __str__(self):
        if self.name:
            return self.name
        return u"VendorBrand"
    class Meta:
        verbose_name = "Vendor Brand"
        verbose_name_plural = "Vendor Brands"

class Color(models.Model):
    """( Color description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=64, default="", blank=True, null=True)
    pms_code = models.CharField(_("PMS Code"), max_length=64, default="", blank=True, null=True)
    PMSFAM_UNCOATED = 'U'
    PMSFAM_COATED = 'C'
    PMSFAM_METALLIC = 'M'
    PMSFAM_NEON = 'N'
    PMSFAM_CHOICES = (
        (PMSFAM_UNCOATED, 'Uncoated'),
        (PMSFAM_COATED, 'Coated'),
        (PMSFAM_METALLIC, 'Metallic'),
        (PMSFAM_NEON, 'Neon'),
    )
    pms_family = models.CharField(_("PMS Family"), max_length=1, default="", blank=True, null=True, choices=PMSFAM_CHOICES)
    hex_code = models.CharField(_("HEX Code"), max_length=64, default="", blank=True, null=True,
        help_text="The 6-digit hexidecimal code for this colour. Do not include the hash tag.")
    r_value = models.IntegerField(_("Red Value"), default=0, help_text="Scale of 0-255")
    g_value = models.IntegerField(_("Green Value"), default=0, help_text="Scale of 0-255")
    b_value = models.IntegerField(_("Blue Value"), default=0, help_text="Scale of 0-255")
    def get_num_vendorcolor(self):
        return VendorColor.objects.filter(master_color=self).count()
    get_num_vendorcolor.short_description="VC Count"
    def get_num_variants(self):
        return Variant.objects.filter(color=self).count()
    get_num_vendorcolor.short_description="Variant Count"

    def __str__(self):
        # if self.pms_code:
        #     return "{} ({})".format(self.name, self.pms_code)
        if self.name:
            return self.name
        return u'Color'
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"
        ordering = ['name',]

class VendorColor(models.Model):
    """( VendorColor description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(PODVendor)
    vendor_code = models.CharField(_("Vendor ID"), max_length=64, null=True, blank=True)
    color_code = models.CharField(_("Vendor Color Code"), max_length=64, null=True, blank=True)
    color_group = models.CharField(_("Vendor Color Group"), max_length=64, null=True, blank=True)
    color_name = models.CharField(_("Vendor Color Name"), max_length=64, null=True, blank=True)
    master_color = models.ForeignKey(Color, null=True, blank=True)

    def __str__(self):
        if self.color_name:
            return "{} - {}".format(self.vendor, self.color_name)
        return u"VendorColor"
    class Meta:
        verbose_name = "Vendor Color"
        verbose_name_plural = "Vendor Colors"


class Size(models.Model):
    """( Size description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=100, default="", blank=True)
    sortorder = models.IntegerField(default=0, blank=True, null=True)
    grouping = models.CharField(_("Category"), max_length=100, default="", blank=True)

    def __str__(self):
        if self.name:
            if self.grouping:
                return "{} / {}".format(self.grouping, self.name)
            return self.name
        return u'Size'
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"
        ordering = ['grouping','sortorder',]

class VendorSize(models.Model):
    """( VendorSize description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(PODVendor)
    vendor_name = models.CharField(_("Vendor Name"), max_length=64, null=True, blank=True)
    vendor_code = models.CharField(_("Vendor ID"), max_length=64, null=True, blank=True)
    vendor_grouping = models.CharField(_("Category"), max_length=100, default="", blank=True)
    master_size = models.ForeignKey(Size, null=True, blank=True)

    def __str__(self):
        if self.vendor_name:
            return self.vendor_name
        return u"VendorSize"
    class Meta:
        verbose_name = "Vendor Size"
        verbose_name_plural = "Vendor Sizes"


class GoogleCategory(MPTTModel):
    id = models.IntegerField(_('Google ID'), primary_key=True)
    name = models.CharField(_('Google Name'), max_length=300, default="", blank=True)
    parent = TreeForeignKey('self', null=True, blank=True,
        related_name='children', db_index=True)
    long_name = models.CharField(_("Category Name"), max_length=300,
        default="", blank=True, help_text="")
    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        elif self.long_name:
            return "{}".format(self.long_name)
        else:
            return u'GoogleCategory'
    class Meta:
        verbose_name = "Google Product Category"
        verbose_name_plural = "Google Product Categories"
    class MPTTMeta:
        order_insertion_by = ['name']

class Category(MPTTModel):
    """( ProductCategory description)"""
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(_("Name"), max_length=300, default="", blank=True)
    parent = TreeForeignKey('self', null=True, blank=True,
      related_name='children', db_index=True)

    def num_products(self):
        return Product.objects.filter(category=self).count()

    def name_treeitem(self):
        indent = "---" * self.level
        rv = "{} {}".format(indent,self.name)

            # '<div style="text-indent:{}px">{}</div>',
            # instance._mpttfield('level') * self.mptt_level_indent,
            # item.name,  # Or whatever you want to put here
        # )

        return rv

    def __str__(self):
        return self.name_treeitem()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    class MPTTMeta:
        order_insertion_by = ['name']


class Outlet(models.Model):
    """( Outlet description)"""
    CATEGORY_UNKNOWN = 'X'
    CATEGORY_WEBSHOP = 'W'
    CATEGORY_MARKETPLACE = 'M'
    CATEGORY_RETAIL = 'R'
    CATEGORY_LICENSE = 'L'
    CATEGORY_CHOICES = (
        (CATEGORY_UNKNOWN, 'Unknown'),
        (CATEGORY_WEBSHOP, 'Web Shop'),
        (CATEGORY_MARKETPLACE, 'Marketplace'),
        (CATEGORY_RETAIL, 'Retail'),
        (CATEGORY_LICENSE, 'License'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=64, default="", blank=True)
    web_url = models.URLField(blank=True, null=True)
    category = models.CharField(_("Category"), max_length=1, blank=True,
        default=CATEGORY_UNKNOWN, choices=CATEGORY_CHOICES)
    description = models.TextField(_("Description"), blank=True, default="")
    def __str__(self):
        if self.name:
            return self.name
        return u'Outlet'
    class Meta:
        verbose_name = "Outlet"
        verbose_name_plural = "Outlets"

class Product(models.Model):
    """( Product description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    master_id = models.CharField(_("Identifier"), max_length=50, default="",
        blank=True, null=True)
    IDTYPE_GTIN = "G"
    IDTYPE_MPN = "M"
    IDTYPE_CHOICES = (
        (IDTYPE_GTIN, "GTIN - Global Trade Item Number"),
        (IDTYPE_MPN, "MPN - Manufacturer Part Number"),
    )
    id_type = models.CharField(_("ID Type"), max_length=1, default=IDTYPE_MPN, choices=IDTYPE_CHOICES)

    name = models.CharField(_("Title"), max_length=150, default="", blank=True, null=True, help_text="")
    description = models.TextField(_("Description"), default="", blank=True, null=True, help_text="")

    brand = models.ForeignKey(Brand, blank=True, null=True)

    category = models.ForeignKey(Category, blank=True, null=True)

    link = models.URLField(_("Product URL"), default="", blank=True, null=True, help_text="")
    mobile_link = models.URLField(_("Mobile URL"), default="", blank=True, null=True, help_text="")

    image_height = models.CharField(_("Image Height"), default="0", max_length=10)
    image_width = models.CharField(_("Image Width"), default="0", max_length=10)
    image = models.ImageField(_("Product Image"), upload_to="product",
        height_field="image_height", width_field="image_width", blank=True, null=True, help_text="")

    additional_image_height = models.CharField(_("Additional Image Height"), default="0", max_length=10)
    additional_image_width = models.CharField(_("Additional Image Width"), default="0", max_length=10)
    additional_image_link = models.ImageField(_("Additional Image"),  upload_to="product_additional",
        height_field="additional_image_height", width_field="additional_image_width",
        blank=True, null=True, help_text="")

    is_sellable = models.BooleanField(_("Is Sellable Product?"), default=False)

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

    age_group = models.CharField(_("Age Group"), max_length=1,
        default=AGEGROUP_ADULT, blank=False, choices=AGEGROUP_CHOICES)

    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_UNISEX = "U"
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_UNISEX, 'Unisex'),
    )
    gender = models.CharField(_("Gender"), max_length=1,
        default=GENDER_UNISEX, blank=False, choices=GENDER_CHOICES)
    material = models.CharField(_("Material"), max_length=200,
        default="", blank=True, null=True, help_text="")
    pattern = models.CharField(_("Pattern"), max_length=100,
        default="", blank=True, null=True, help_text="")

    googlecategory = models.ForeignKey(GoogleCategory, blank=True, null=True)

    SIZETYPE_NONE = "N"
    SIZETYPE_REGULAR = "R"
    SIZETYPE_PETITE = "T"
    SIZETYPE_PLUS = "L"
    SIZETYPE_BIGANDTALL = "B"
    SIZETYPE_MATERNITY = "M"
    SIZETYPE_CHOICES = (
        (SIZETYPE_NONE, 'None'),
        (SIZETYPE_REGULAR, 'Regular'),
        (SIZETYPE_PETITE, 'Petite'),
        (SIZETYPE_PLUS, 'Plus'),
        (SIZETYPE_BIGANDTALL, 'Big and Tall'),
        (SIZETYPE_MATERNITY, 'Maternity'),
    )
    size_type = models.CharField(_("Size Type"), max_length=1,
        default=SIZETYPE_NONE, blank=True, choices=SIZETYPE_CHOICES)

    SIZESYSTEM_US = 'US'
    SIZESYSTEM_UK = 'UK'
    SIZESYSTEM_EU = 'EU'
    SIZESYSTEM_DE = 'DE'
    SIZESYSTEM_FR = 'FR'
    SIZESYSTEM_JP = 'JP'
    SIZESYSTEM_CN = 'CN'
    SIZESYSTEM_IT = 'IT'
    SIZESYSTEM_BR = 'BR'
    SIZESYSTEM_MEX = 'MEX'
    SIZESYSTEM_AU = 'AU'
    SIZESYSTEM_CHOICES = (
        (SIZESYSTEM_US, 'US - United States'),
        (SIZESYSTEM_UK, 'UK - United Kingdom'),
        (SIZESYSTEM_EU, 'EU - European Union'),
        (SIZESYSTEM_DE, 'DE - Germany'),
        (SIZESYSTEM_FR, 'FR - France'),
        (SIZESYSTEM_JP, 'JP - Japan'),
        (SIZESYSTEM_CN, 'CN - China'),
        (SIZESYSTEM_IT, 'IT - Italy'),
        (SIZESYSTEM_BR, 'BR - Brazil'),
        (SIZESYSTEM_MEX, 'MEX - Mexico'),
        (SIZESYSTEM_AU, 'AU - Australia'),
    )
    size_system = models.CharField(_("Size System"), max_length=3,
        default=SIZESYSTEM_US, blank=False, choices=SIZESYSTEM_CHOICES)

    @property
    def vendor_count(self):
        return VendorProduct.objects.filter(master_product=self).count()

    def __str__(self):
        if (self.brand and self.name and self.master_id):
            return " / ".join([self.brand.name, self.master_id, self.name])
        return u"Product"
        if self.name:
            return self.name
        return 'Product'
        # return "{} / {} / {}".format(self.brand, self.master_id, self.name)

    def temp_vendorbrand(self):
        vp = VendorProduct.objects.filter(master_product=self)
        return str(vp[0].brand)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['brand', 'master_id', 'name']

class Variant(models.Model):
    """( ProductVariant description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product)

    title = models.CharField(_("Title"), max_length=150, default="", blank=True, null=True, help_text="")

    image_url = models.URLField(_("Image URL"), null=True, blank=True)

    image_height = models.CharField(_("Image Height"), default="0", max_length=10)
    image_width = models.CharField(_("Image Width"), default="0", max_length=10)
    image = models.ImageField(_("Product Image"), upload_to="product",
        height_field="image_height", width_field="image_width", blank=True, null=True, help_text="")
    link = models.URLField(_("Product URL"), default="", blank=True, null=True, help_text="")

    color = models.ForeignKey(Color, blank=True, null=True)
    size = models.ForeignKey(Size, blank=True, null=True)

    def __str__(self):
        return u'Variant'
        # return self.title
        if self.title:
            return self.title
        return "{}, {}, {}".format(self.product.name, self.color, self.size)

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variants"

class VendorCategory(models.Model):
    """( VendorProduct description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=64, default="", blank=True)
    vendor = models.ForeignKey(PODVendor, blank=True, null=True)
    def __str__(self):
        if self.name:
            return self.name
        return u'VendorCategory'
    class Meta:
        verbose_name = "Vendor Category"
        verbose_name_plural = "Vendor Categories"

class VendorProduct(models.Model):
    """( VendorProduct description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mpn = models.CharField(_("Vendor Product MPN"), max_length=100, null=True, blank=True, default="")
    sku = models.CharField(_("Vendor SKU"), max_length=100, null=True, blank=True, default="")
    vendor = models.ForeignKey(PODVendor, verbose_name="POD Vendor", null=True, blank=True)
    name = models.CharField(_("Local Product Name"), max_length=255, default="", blank=True)
    category = models.ForeignKey(VendorCategory, verbose_name="Category", null=True, blank=True)
    image_url = models.URLField(_("Vendor Product Image"), blank=True, null=True)
    master_product = models.ForeignKey(Product, verbose_name="Master Product", null=True, blank=True)
    brand = models.ForeignKey(VendorBrand, verbose_name="Vendor Brand", null=True, blank=True)
    description = models.TextField(_("Vendor Description"), blank=True, default="", null=True)
    material = models.CharField(_("Vendor Material"), blank=True, null=True, max_length=128)
    country = models.CharField(_("Vendor Country"), blank=True, null=True, max_length=128)
    def __str__(self):
        if self.name:
            return self.name
        return u'VendorProduct'
    class Meta:
        verbose_name = "Vendor Product"
        verbose_name_plural = "Vendor Products"

class VendorVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.CharField(_("Vendor MPN"), max_length=64, blank=True, null=True)
    podvendor = models.ForeignKey(PODVendor, null=True, blank=True)
    vendor_product = models.ForeignKey(VendorProduct, blank=True, null=True)
    # variant = models.ForeignKey(Variant, null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    price = models.CharField(_("Price"), max_length=64, default="", blank=True, null=True)
    vendor_color = models.ForeignKey(VendorColor, blank=True, null=True)
    vendor_size = models.ForeignKey(VendorSize, blank=True, null=True)
    def __str__(self):
        return self.vendor_id
        # return "{} {}".format(variant.title, ppodvendor.name)

    class Meta:
        verbose_name = "Vendor Variant"
        verbose_name_plural = "Vendor Variants"


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=64, blank=True, null=True)
    web = models.URLField(_("Web Site"), blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=20, blank=True, null=True)
    email = models.EmailField(_("E-Mail"), blank=True, null=True)
    location = models.CharField(_("Location"), max_length=255, blank=True, null=True)
    agreement = models.TextField(blank=True, null=True, default="")
    has_agreement = models.BooleanField(_("Agreement in Place?"), default=False)
    notes = models.TextField(blank=True, null=True, default="")

    def num_live(self):
        return Creative.objects.filter(
            artist=self, status=Creative.STATUS_LIVE).count()
    num_live.short_description = "Live"

    def num_assigned(self):
        return Creative.objects.filter(
            artist=self, status=Creative.STATUS_INDEV).count()
    num_assigned.short_description = "Assigned"

    def total_creative(self):
        return Creative.objects.filter(artist=self).count()
    total_creative.short_description = "Total"


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ['name',]

class CreativeSeries(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), unique=True, max_length=3, blank=False, null=False)
    name = models.CharField(_("Name"), default="", max_length=64, blank=True, null=True)
    primary_outlet = models.ForeignKey(Outlet, blank=True, null=True)
    note = models.TextField(default="", null=True, blank=True)
    def num_creative(self):
        return Creative.objects.filter(series=self).count()
    num_creative.short_description = "Num Creative"
    def __str__(self):
        if self.primary_outlet:
            return " / ".join([self.primary_outlet.name, self.name])
        return self.name
    class Meta:
        verbose_name = "Creative Series"
        verbose_name_plural = "Creative Series"
        ordering = ['name',]

class Creative(models.Model):
    STATUS_NEW = "N"
    STATUS_INDEV = "V"
    STATUS_LIVE = "L"
    STATUS_DEFERRED = "D"
    STATUS_CHOICES = (
        (STATUS_NEW, "New"),
        (STATUS_INDEV, "In Development"),
        (STATUS_LIVE, "Live"),
        (STATUS_DEFERRED, "Deferred"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=3, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=64, blank=True, null=True)
    artist = models.ForeignKey(Artist, null=True, blank=True)
    note = models.TextField(default="", null=True, blank=True)
    status = models.CharField(_("Status"), choices=STATUS_CHOICES, max_length=1,
                              default=STATUS_NEW, null=True, blank=True)
    series = models.ForeignKey(CreativeSeries, blank=True, null=True)
    def series_name(self):
        if self.series:
            return self.series.name
        return "None"
    series_name.short_description = "Series"

    def series_outlet(self):
        if self.series:
            return self.series.primary_outlet
        return "None"
    series_outlet.short_description = "Outlet"

    def full_code(self):
        try:
            return "{}{}".format(self.series.code, self.code)
        except:
            return "Unknown"
    full_code.short_description = "Full Code"

    def status_tag(self):
        # return self.status
        STATUS_COLORS = {
            self.STATUS_NEW: '#CC3333',
            self.STATUS_INDEV: '#cc9933',
            self.STATUS_LIVE: '#009900',
            self.STATUS_DEFERRED: '#999999',
        }
        rv = "<div style='text-align: center; padding: 2px; color:#ffffff; background-color:{};'>{}</div>".format(
            STATUS_COLORS[self.status], self.get_status_display() )
        return rv
    status_tag.short_description = "Status"
    status_tag.allow_tags = True

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Creative"
        verbose_name_plural = "Creative"
        ordering = ['name',]
        unique_together = (("series", "code"),)
