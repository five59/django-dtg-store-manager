# import uuid
# from django.core.urlresolvers import reverse
# from django_extensions.db.fields import AutoSlugField
# from django.db.models import *
# from django.conf import settings
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth import get_user_model
# from django.contrib.auth import models as auth_models
# from django.db import models as models
# from django_extensions.db import fields as extension_fields
# import colorsys
#
# class Brand(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     vendor_id = models.IntegerField(verbose_name="Aura ID")
#     name = models.CharField(verbose_name="Name", max_length=255, default="", blank=True)
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#     class Meta:
#         ordering = ('name',)
#         verbose_name = "Brand"
#         verbose_name_plural = "Brands"
#     def __str__(self):
#         return self.name
#
# class Size(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     aura_id = models.IntegerField(verbose_name="Aura ID")
#     name = models.CharField(verbose_name="Name", max_length=255, default="", blank=True)
#     group = models.CharField(verbose_name="Product Group", max_length=255, default="", blank=True)
#     plus_size_charge = models.DecimalField(max_digits=6, decimal_places=2)
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#     class Meta:
#         ordering = ('name',)
#         verbose_name = "Size"
#         verbose_name_plural = "Sizes"
#     def __str__(self):
#         return self.name
#     def get_num_productvariants(self):
#         return ProductVariant.objects.filter(size=self).count()
#     get_num_productvariants.short_description = 'Product Variant Count'
#
# class Color(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     aura_id = models.IntegerField(verbose_name="Aura ID")
#     name = models.CharField(verbose_name="Name", max_length=255, default="", blank=True)
#     code = models.CharField(verbose_name="Hex Code", max_length=6, default="", blank=True)
#     group = models.CharField(verbose_name="Group", max_length=6, default="", blank=True)
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#
#     color_hue = models.IntegerField(default=0)
#     color_brightness = models.IntegerField(default=0)
#
#     class Meta:
#         ordering = ('color_hue','color_brightness',)
#         verbose_name = "Color"
#         verbose_name_plural = "Colors"
#     def __str__(self):
#         return self.name
#
# class ShippingOption(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     aura_id = models.IntegerField(verbose_name="Aura ID", default=0)
#     name = models.CharField(max_length=64, default="", blank=True, verbose_name="Name")
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Shipping Option"
#         verbose_name_plural = "Shipping Options"
#
# class ProductGroup(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     aura_id = models.IntegerField(verbose_name="Aura ID", default=0)
#     name = models.CharField(max_length=64, default="", blank=True, verbose_name="Name")
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Product Group"
#         verbose_name_plural = "Product Groups"
#         ordering = ('name',)
#     def get_products(self):
#         return Product.objects.filter(productgroup=self)
#     def get_num_products(self):
#         return Product.objects.filter(productgroup=self).count()
#
# class ShippingZone(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=64, default="", blank=True, verbose_name="Name")
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Shipping Zone"
#         verbose_name_plural = "Shipping Zones"
#
# class Shipping(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     group = models.ForeignKey(ProductGroup, null=True, blank=True)
#     option = models.ForeignKey(ShippingOption, null=True, blank=True)
#     zone = models.ForeignKey(ShippingZone, null=True, blank=True)
#     company = models.CharField(verbose_name="Company", max_length=255, default="", blank=True)
#     first_item_price = models.DecimalField(max_digits=6, decimal_places=2)
#     additional_item_price = models.DecimalField(max_digits=6, decimal_places=2)
#     slug = extension_fields.AutoSlugField(populate_from='company', blank=True)
#
#     class Meta:
#         ordering = ('option','group',)
#         verbose_name = "Shipping"
#         verbose_name_plural = "Shipping"
#     def __str__(self):
#         # return " - ".join([self.option, self.group])
#         return u"Shipping"
#
# class AdditionalSettings(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(verbose_name="Name", max_length=255, default="", blank=True)
#     value = models.CharField(verbose_name="Value", max_length=255, default="", blank=True)
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#     class Meta:
#         ordering = ('name',)
#         verbose_name = "Additional Setting"
#         verbose_name_plural = "Additional Settings"
#     def __str__(self):
#         return self.name
#
# class Country(models.Model):
#     """( Country description)"""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=64, default="", blank=True, verbose_name="Name")
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#
#     image_height = models.CharField(blank=True, null=True, default="", max_length=100)
#     image_width = models.CharField(blank=True, null=True, default="", max_length=100)
#     image = models.ImageField(verbose_name="Country Flag", upload_to="country/",
#                               blank=True, null=True,
#                               height_field='image_height', width_field="image_width")
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Country"
#         verbose_name_plural = "Countries"
#
# class LocalProductGroup(models.Model):
#     """( LocalProductGroup description)"""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=64, default="", blank=True, verbose_name="Name")
#     slug = models.SlugField(blank=True, verbose_name="Slug")
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Local Product Group"
#         verbose_name_plural = "Local Product Groups"
#         ordering = ['name',]
#     def get_products(self):
#         return Product.objects.filter(localproductgroup=self)
#     def get_num_products(self):
#         return Product.objects.filter(localproductgroup=self).count()
#
# class Product(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     aura_id = models.IntegerField(verbose_name="Aura ID")
#     sku = models.CharField(verbose_name="SKU", max_length=50, default="", blank=True)
#     name = models.CharField(verbose_name="Name", max_length=255, default="", blank=True)
#     material_name = models.CharField(verbose_name="Material", max_length=255, default="", blank=True)
#     inventory_description = models.TextField(verbose_name="Description", default="", blank=True)
#     slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     color_price = models.DecimalField(max_digits=6, decimal_places=2)
#     size_chart_image_url = models.URLField(verbose_name="Size Chart URL", blank=True)
#     brand = models.ForeignKey(Brand, null=True, blank=True)
#     productgroup = models.ForeignKey(ProductGroup, null=True, blank=True, verbose_name="Product Group")
#     country = models.ForeignKey(Country, null=True, blank=True)
#
#     # Local Fields
#     image_height = models.CharField(blank=True, null=True, default="", max_length=100)
#     image_width = models.CharField(blank=True, null=True, default="", max_length=100)
#     image = models.ImageField(verbose_name="Product Image", upload_to="product/",
#                               blank=True, null=True,
#                               height_field='image_height', width_field="image_width")
#     local_sku = models.CharField(verbose_name="SKU", max_length=50, default="", blank=True)
#     local_name = models.CharField(verbose_name="Name", max_length=255, default="", blank=True)
#     localproductgroup = models.ForeignKey(LocalProductGroup, null=True, blank=True, verbose_name="Local Product Group")
#     local_description = models.TextField(verbose_name="Description", default="", blank=True)
#     mfg_product_url = models.URLField(default="", blank=True, null=True,
#                                       verbose_name="Product URL", help_text="URL of the manufacturer's product page")
#
#     class Meta:
#         ordering = ('productgroup','brand','name','sku',)
#         verbose_name = "Product"
#         verbose_name_plural = "Products"
#     def __str__(self):
#         return self.get_name()
#
#     def get_name(self):
#         if self.local_name:
#             return self.local_name
#         return self.name
#     get_name.short_description="Name"
#
#     def get_variants(self):
#         return ProductVariant.objects.filter(product=self)
#     get_variants.short_description="Variants"
#
#     def get_num_variants(self):
#         return ProductVariant.objects.filter(product=self).count()
#     get_num_variants.short_description="Variant Count"
#
#     def get_sizes(self):
#         return None
#     get_sizes.short_description="Sizes"
#
#     def get_num_sizes(self):
#         return None
#     get_num_sizes.short_description="Size Count"
#
#     def get_colors(self):
#         return None
#     get_colors.short_description="Colors"
#
#     def get_num_colors(self):
#         return None
#     get_num_colors.short_description="Color Count"
#
#     def is_tiered_pricing(self):
#         if self.price == self.color_price:
#             return False
#         return True
#     is_tiered_pricing.short_description="Has Tiered Pricing?"
#
#     def get_variants_white(self):
#         return ProductVariant.objects.filter(product=self, color__group='White')
#     get_variants.short_description="White Variants"
#
#     def get_variants_color(self):
#         return ProductVariant.objects.filter(product=self, color__group='Color')
#     get_variants.short_description="Color Variants"
#
#     def get_sku(self):
#         if self.local_sku:
#             return self.local_sku
#         return self.sku
#
#     def get_pricing(self):
#         if self.price == self.color_price:
#             return "${:,.2f}".format( self.price )
#         return "${:,.2f} &mdash; ${:,.2f}".format( self.price, self.color_price,  )
#
# class ProductVariant(models.Model):
#     """( ProductVariant description)"""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     product = models.ForeignKey(Product)
#     color = models.ForeignKey(Color, null=True, blank=True)
#     size = models.ForeignKey(Size, null=True, blank=True)
#
#     image_height = models.CharField(blank=True, null=True, default="", max_length=100)
#     image_width = models.CharField(blank=True, null=True, default="", max_length=100)
#     image = models.ImageField(verbose_name="Variant Image", upload_to="product/",
#                               blank=True, null=True,
#                               height_field='image_height', width_field="image_width")
#     local_sku = models.CharField(verbose_name="SKU", max_length=50, default="", blank=True)
#     mfg_product_url = models.URLField(default="", blank=True, null=True,
#                                       verbose_name="Product URL", help_text="URL of the manufacturer's product page")
#
#     def get_sku(self):
#         rv_c, rv_s = "XX"
#         if self.local_sku:
#             return self.local_sku
#         if self.color:
#             rv_c = self.color.aura_id
#         if self.size:
#             rv_s = self.size.aura_id
#         return "{}-{}-{}".format(self.product.sku, rv_c, rv_s)
#     get_sku.short_description = "SKU"
#     def __str__(self):
#         return "{} / {} / {}".format(self.product, self.color, self.size)
#     class Meta:
#         verbose_name = "Product Variant"
#         verbose_name_plural = "Product Variants"
#         ordering = ('-color__code','size__aura_id',)
#     def has_image(self):
#         if self.image:
#             return True
#         return False
#     has_image.boolean = True
#     has_image.short_description = "Image?"