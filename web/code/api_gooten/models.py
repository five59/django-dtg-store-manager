from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models

from django.core.urlresolvers import reverse
from django.core import files

from django.db import models as models
from django.db.models import *

from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from django_extensions.db.fields import AutoSlugField

from catalog import models as cm

import requests
import os
import uuid
import urllib
import locale
import tempfile


class Product(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    is_active = BooleanField(default=False)

    id = IntegerField(default=0)
    uid = CharField(max_length=255, default="", blank=True, null=True)
    name = CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    is_featured = BooleanField(_("Featured?"), default=False)
    is_coming_soon = BooleanField(_("Coming Soon?"), default=False)
    has_available_product_variants = BooleanField(_("Variant?"), default=False)
    has_product_templates = BooleanField(_("Has Template?"), default=False)
    description = CharField(_("Desc"), max_length=255, default="", blank=True, null=True)
    max_zoom = DecimalField(max_digits=5, decimal_places=2, default=0)
    priceinfo_price = DecimalField(max_digits=7, decimal_places=2, default=0)
    priceinfo_currencycode = CharField(max_length=3, default="USD", blank=False, null=True)
    priceinfo_currencydigits = IntegerField(default=2)
    priceinfo_currencyformat = CharField(max_length=10, default="", blank=True, null=True)
    priceinfo_formattedprice = CharField(
        _("Price"), max_length=24, default="", blank=True, null=True)
    retailprice_price = DecimalField(max_digits=7, decimal_places=2, default=0)
    retailprice_currencycode = CharField(max_length=3, default="USD", blank=False, null=True)
    retailprice_currencydigits = IntegerField(default=2)
    retailprice_currencyformat = CharField(max_length=10, default="", blank=True, null=True)
    retailprice_formattedprice = CharField(max_length=24, default="", blank=True, null=True)

    # Relationship Fields
    categories = models.ManyToManyField('api_gooten.ProductCategory', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('api_gooten_product_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_product_update', args=(self.slug,))


class ProductImage(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='id', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    id = CharField(max_length=255, default="", blank=True, null=True)
    index = IntegerField(default=0)
    url = URLField(blank=True)
    is_active = BooleanField(default=True)

    image_height = models.CharField(_("Image Height"), default="0",
                                    max_length=10, blank=True, null=True)
    image_width = models.CharField(_("Image Width"), default="0",
                                   max_length=10, blank=True, null=True)
    image = models.ImageField(_("Item Image"), upload_to="api_gooten/productimage",
                              height_field="image_height", width_field="image_width", blank=True, null=True, help_text="")

    # Relationship Fields
    product = models.ForeignKey('api_gooten.Product', )
    imagetypes = models.ManyToManyField('api_gooten.ImageType', blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return u'%s' % self.slug

    def has_image(self):
        if self.image:
            return True
        return False
    has_image.short_description = "Local?"
    has_image.boolean = True

    def download_image(self):
        if not self.image:
            if self.url:
                print(
                    "--> Attempting download of linked image for {} #{} - {}.".format(self.product.name, self.id, self.index))
                request = requests.get(self.url, stream=True)
                if request.status_code == requests.codes.ok:
                    path = urllib.parse.urlparse(self.url).path
                    ext = os.path.splitext(path)[1]
                    file_name = "{}/{}-{}{}".format(
                        self.product.name,
                        self.id,
                        self.index,
                        ext
                    )
                    lf = tempfile.NamedTemporaryFile()
                    for block in request.iter_content(1024 * 8):
                        if not block:
                            break
                        lf.write(block)
                    self.image.save(file_name, files.File(lf))

    def image_thumb(self):
        if self.image:
            return "<img src=\"{}\" height=\"64\" width=\"64\" alt=\"{}\" />".format(
                self.image.url, self.value)
        return ""
    image_thumb.allow_tags = True
    image_thumb.short_description = "Thumbnail"

    def get_product(self):
        return self.product
    get_product.short_description = "Product"

    def get_absolute_url(self):
        return reverse('api_gooten_productimage_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_productimage_update', args=(self.slug,))


class ProductCategory(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    id = CharField(max_length=255, default="", blank=True, null=True)
    name = CharField(max_length=255, default="", blank=True, null=True)

    class Meta:
        ordering = ('id',)
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name

    # TODO def get_product_count(self) - needs a reverse many-to-many lookup

    def get_absolute_url(self):
        return reverse('api_gooten_productcategory_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_productcategory_update', args=(self.slug,))


class ImageType(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    name = CharField(max_length=255, default="", blank=True, null=True)

    friendly_name = CharField(max_length=255, default="", blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Image Type"
        verbose_name_plural = "Image Types"

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('api_gooten_imagetype_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_imagetype_update', args=(self.slug,))


class ProductInfo(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='pkid', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    info_key = CharField(max_length=255, default="", blank=True, null=True)
    index = IntegerField(default=0)

    # Relationship Fields
    product = models.ForeignKey('api_gooten.Product', )
    content_type = models.ForeignKey('api_gooten.ContentType', )

    class Meta:
        ordering = ('-created',)
        verbose_name = "Product Info"
        verbose_name_plural = "Product Info"

    def __str__(self):
        return self.info_key

    def get_text(self):
        rv = []
        for i in InfoContent.objects.filter(productinfo=self):
            rv.append(i.text)
        return ". ".join(rv)
    get_text.short_description = "Text"

    def get_product(self):
        return self.product
    get_product.short_description = "Product"

    def get_content_type(self):
        return self.content_type
    get_content_type.short_description = "Content Type"

    def get_absolute_url(self):
        return reverse('api_gooten_productinfo_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_productinfo_update', args=(self.slug,))


class ContentType(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    name = CharField(max_length=255, default="", blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Content Type'
        verbose_name_plural = 'Content Types'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('api_gooten_contenttype_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_contenttype_update', args=(self.slug,))


class InfoContent(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='text', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    text = CharField(max_length=5000, default="", blank=True, null=True)

    # Relationship Fields
    productinfo = models.ForeignKey('api_gooten.ProductInfo', )

    class Meta:
        ordering = ('-created',)
        verbose_name = "Info Content"
        verbose_name_plural = "Info Content"

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('api_gooten_infocontent_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_infocontent_update', args=(self.slug,))


class Variant(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='sku', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    is_active = BooleanField(_("Active?"), default=False)

    sku = CharField(_("SKU"), max_length=255, default="", blank=True, null=True)
    has_templates = BooleanField(_("Templates?"), default=False)
    max_images = IntegerField(_("Num Images"), default=0)
    priceinfo_price = DecimalField(_("Price"), max_digits=7, decimal_places=2, default=0)
    priceinfo_currencycode = CharField(
        _("Currency Code"), max_length=3, default="USD", blank=False, null=True)
    priceinfo_currencydigits = IntegerField(_("Digits"), default=2)
    priceinfo_currencyformat = CharField(
        _("Format"), max_length=10, default="", blank=True, null=True)
    priceinfo_formattedprice = CharField(
        _("Formatted Price"), max_length=24, default="", blank=True, null=True)

    # Transitory Attributes (These should be considered non-definitive, as they are updated from the VariantOptions).
    # They are included here to keep filtering at the database level from within Django rather than bubbling up
    # the logic to Python, which would slow down the processing.
    c_brand = ForeignKey(cm.Brand, verbose_name="Brand",
                         related_name="catalog_brand", blank=True, null=True)
    c_item = ForeignKey(cm.Item, verbose_name="Item",
                        related_name="catalog_item", blank=True, null=True)
    c_color = ForeignKey(cm.Color, verbose_name="Color",
                         related_name="catalog_color", blank=True, null=True)
    c_size = ForeignKey(cm.Size, verbose_name="Size",
                        related_name="catalog_size", blank=True, null=True)

    # Relationship Fields
    product = models.ForeignKey('api_gooten.Product', )

    def __init__(self, *args, **kwargs):
        super(Variant, self).__init__(*args, **kwargs)
        self._original_state = dict(self.__dict__)

    def save(self, *args, **kwargs):
        if self.is_dirty():
            for k, v in self.changed_columns().items():
                if k == 'c_item_id':
                    self.c_brand = self.c_item.brand

        state = dict(self.__dict__)
        del state['_original_state']
        self._original_state = state
        super(Variant, self).save()

    def is_dirty(self):
        missing = object()
        result = {}
        for key, value in self._original_state.items():
            if value != self.__dict__.get(key, missing):
                return True
        return False

    def changed_columns(self):
        missing = object()
        result = {}
        for key, value in self._original_state.items():
            if value != self.__dict__.get(key, missing):
                result[key] = {'old': value, 'new': self.__dict__.get(key, missing)}
        return result

    class Meta:
        ordering = ('product', 'sku',)
        verbose_name = 'Variant'
        verbose_name_plural = 'Variants'

    def friendly_name(self):
        # if self.c_brand and self.c_item:
        #     if self.c_size and self.c_color:
        #         rv = "{}{} - {} / {} / {}".format(self.c_brand.code, self.c_item.code,
        #                                           self.c_item.name, self.c_color.name, self.c_size.name)
        #     else:
        #         rv = "{}{} - {}".format(self.c_brand.code, self.c_item.code, self.c_item.name)
        # else:
        rv = "{}".format(self.sku)
        return rv

    def __str__(self):
        return self.friendly_name()

    def get_absolute_url(self):
        return reverse('api_gooten_variant_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_variant_update', args=(self.slug,))

    def get_product(self):
        return self.product
    get_product.short_description = "Product"

    def get_templates(self):
        return VariantTemplate.objects.filter(variant=self)
    get_templates.short_description = 'Templates'

    def num_templates(self):
        return self.get_templates().count()
    num_templates.short_description = 'Templates'

    def get_options(self):
        return VariantOption.objects.filter(variant=self)
    get_options.short_description = 'Options'

    def num_options(self):
        return self.get_options().count()
    num_options.short_description = 'Options'


class Attribute(models.Model):
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='pkid', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    grouping = CharField(max_length=255, default="", blank=True, null=True)

    option_id = CharField(max_length=255, default="", blank=True, null=True)
    name = CharField(max_length=255, default="", blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'

    def __str__(self):
        return self.name

    def get_num_values(self):
        return AttributeValue.objects.filter(attribute=self).count()
    get_num_values.short_description = "Items"

    def get_absolute_url(self):
        return reverse('api_gooten_attribute_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_attribute_update', args=(self.slug,))


class AttributeValue(models.Model):
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='pkid', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)

    value = CharField(max_length=255, default="", blank=True, null=True)
    value_id = CharField(max_length=255, default="", blank=True, null=True)
    sort_value = CharField(max_length=255, default="", blank=True, null=True)
    image_type = CharField(max_length=255, default="", blank=True, null=True)
    image_url = URLField(blank=True)
    image_height = models.CharField(_("Image Height"), default="0",
                                    max_length=10, blank=True, null=True)
    image_width = models.CharField(_("Image Width"), default="0",
                                   max_length=10, blank=True, null=True)
    image = models.ImageField(_("Item Image"), upload_to="api_gooten/attribute", max_length=1000,
                              height_field="image_height", width_field="image_width", blank=True, null=True, help_text="")

    # Relationship Fields
    attribute = models.ForeignKey('api_gooten.Attribute', blank=True, null=True)

    class Meta:
        ordering = ('sort_value',)
        verbose_name = 'Attribute Value'
        verbose_name_plural = 'Attribute Values'

    def __str__(self):
        return self.value

    def has_image(self):
        if self.image:
            return True
        return False
    has_image.short_description = "Local?"
    has_image.boolean = True

    def download_image(self):
        if not self.image:
            if self.image_url:
                print("-- Downloading {} - {}".format(self.attribute.name, self.value))
                # print("--> Downloading:\t{}\t{}\t{}.".format(self.variant.product.name,
                #                                              self.variant.sku, self.name))
                request = requests.get(self.image_url, stream=True)
                if request.status_code == requests.codes.ok:
                    path = urllib.parse.urlparse(self.image_url).path
                    ext = os.path.splitext(path)[1]
                    file_name = "{}/{}{}".format(
                        self.attribute.name,
                        self.value,
                        ext
                    )
                    print("Filename: {}".format(file_name))

                    lf = tempfile.NamedTemporaryFile()
                    for block in request.iter_content(1024 * 8):
                        if not block:
                            break
                        lf.write(block)
                    self.image.save(file_name, files.File(lf))

    def image_thumb(self):
        if self.image:
            return "<img src=\"{}\" height=\"64\" width=\"64\" alt=\"{}\" />".format(
                self.image.url, self.value)
        return ""
    image_thumb.allow_tags = True
    image_thumb.short_description = "Thumbnail"

    def get_attribute(self):
        return self.attribute
    get_attribute.short_description = 'Attribute'

    def get_absolute_url(self):
        return reverse('api_gooten_attributevalue_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_attributevalue_update', args=(self.slug,))


class VariantOption(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='pkid', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    value = models.ForeignKey('api_gooten.AttributeValue', blank=True, null=True)
    variant = models.ForeignKey('api_gooten.Variant', blank=True, null=True)

    class Meta:
        ordering = ('value__sort_value', 'value__attribute__name',)
        verbose_name = 'Variant Option'
        verbose_name_plural = 'Variant Options'

    def __str__(self):
        return "{}: {}".format(self.value.attribute, self.value)

    def get_absolute_url(self):
        return reverse('api_gooten_variantoption_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_variantoption_update', args=(self.slug,))

    def get_attribute(self):
        return self.value.attribute
    get_attribute.short_description = "Attribute"

    def get_image_thumb(self):
        return self.value.image_thumb()
    get_image_thumb.allow_tags = True

    def get_value(self):
        return self.value
    get_value.short_description = 'Value'

    def get_sort_value(self):
        return self.value.sort_value
    get_sort_value.short_description = "Order"


class VariantTemplate(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='pkid', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    is_active = BooleanField(default=True)

    name = CharField(max_length=255, default="", blank=True, null=True)
    is_default = BooleanField(default=True)
    image_url = URLField(blank=True)

    image_height = models.CharField(_("Image Height"), default="0",
                                    max_length=10, blank=True, null=True)
    image_width = models.CharField(_("Image Width"), default="0",
                                   max_length=10, blank=True, null=True)
    image = models.ImageField(_("Item Image"), upload_to="api_gooten/variant_template",
                              height_field="image_height", width_field="image_width", blank=True, null=True, help_text="")

    # Relationship Fields
    variant = models.ForeignKey('api_gooten.Variant', )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Variant Template'
        verbose_name_plural = 'Variant Templates'

    def __str__(self):
        return "{} / {}".format(self.variant.sku, self.name)

    def image_thumb(self):
        if self.image:
            return "<img src=\"{}\" height=\"64\" width=\"64\" alt=\"{}\" />".format(
                self.image.url, self.value)
        return ""
    image_thumb.allow_tags = True
    image_thumb.short_description = "Thumbnail"

    def get_absolute_url(self):
        return reverse('api_gooten_VariantTemplate_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_VariantTemplate_update', args=(self.slug,))


class TemplateSpace(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='pkid', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    id = CharField(max_length=255, default="", blank=True, null=True)
    index = IntegerField(default=0)
    final_x1 = IntegerField(default=0)
    final_x2 = IntegerField(default=0)
    final_y1 = IntegerField(default=0)
    final_y2 = IntegerField(default=0)

    # Relationship Fields
    variant_template = models.ForeignKey('api_gooten.VariantTemplate', )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Template Space'
        verbose_name_plural = 'Template Spaces'

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('api_gooten_templatespace_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_templatespace_update', args=(self.slug,))


class LayerType(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    name = CharField(max_length=255, default="", blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Layer Type'
        verbose_name_plural = 'Layer Types'

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('api_gooten_layertype_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_layertype_update', args=(self.slug,))


class SpaceLayer(models.Model):

    # Fields
    pkid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='pkid', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    include_in_print = BooleanField(default=False)
    id = CharField(max_length=24, default="", blank=True, null=True)
    x1 = IntegerField(default=0)
    x2 = IntegerField(default=0)
    y1 = IntegerField(default=0)
    y2 = IntegerField(default=0)
    zIndex = IntegerField(default=0)

    # Relationship Fields
    templatespace = models.ForeignKey('api_gooten.TemplateSpace', )
    layer_type = models.ForeignKey('api_gooten.LayerType', )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Space Layer'
        verbose_name_plural = 'Space Layers'

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('api_gooten_spacelayer_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_gooten_spacelayer_update', args=(self.slug,))
