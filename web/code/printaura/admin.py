# from django.contrib import admin
# from .models import *
#
# # Inlines
# class ProductInline(admin.TabularInline):
#     model = Product
#     extra = 0
#     fields = ['name','sku', 'aura_id',]
#
# class ProductVariantInline(admin.TabularInline):
#     model = ProductVariant
#     extra = 0
#     fields = ['color','image','local_sku',]
#     suit_classes = 'suit-tab suit-tab-variants'
#
#
# # Model Admins
#
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ['name','has_logo','has_description','get_num_products','web_url']
#     inlines = [ProductInline, ]
# admin.site.register(Brand, BrandAdmin)
#
# class SizeAdmin(admin.ModelAdmin):
#     list_display = ['name','group','plus_size_charge','get_num_productvariants',]
#     list_filter = ['group',]
# admin.site.register(Size, SizeAdmin)
#
# class ColorAdmin(admin.ModelAdmin):
#     list_display = ['name', 'code', 'group','color_hue','color_brightness',]
#     list_filter = ['group',]
# admin.site.register(Color, ColorAdmin)
#
# class ShippingOptionAdmin(admin.ModelAdmin):
#     list_display = ['name',]
# admin.site.register(ShippingOption, ShippingOptionAdmin)
#
# class ProductGroupAdmin(admin.ModelAdmin):
#     list_display = ['name','get_num_products']
# admin.site.register(ProductGroup, ProductGroupAdmin)
#
# class ShippingZoneAdmin(admin.ModelAdmin):
#     list_display = ['name',]
# admin.site.register(ShippingZone, ShippingZoneAdmin)
#
# class ShippingAdmin(admin.ModelAdmin):
#     list_display = ['group','option','zone','company','first_item_price','additional_item_price',]
#     list_filter = ['group','option','zone',]
# admin.site.register(Shipping, ShippingAdmin)
#
# class AdditionalSettingsAdmin(admin.ModelAdmin):
#     list_display = ['name','value',]
# admin.site.register(AdditionalSettings, AdditionalSettingsAdmin)
#
# class CountryAdmin(admin.ModelAdmin):
#
#     fieldsets = [
#         (None, {
#             'classes': ('suit-tab', 'suit-tab-main',),
#             'fields': ["name", "image",],
#         }),
#     ]
#     suit_form_tabs = (
#         ('main','Main'),
#     )
#
# admin.site.register(Country, CountryAdmin)
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['sku','local_sku','localproductgroup','name','local_name','image']
#     # list_display = ['sku','localproductgroup','productgroup','brand','name', 'image',]
#     #'get_num_variants','get_num_colors','get_num_sizes']
#     list_filter = ['brand', 'productgroup', 'localproductgroup', 'country',]
#     # list_editable = ['localproductgroup','local_sku','local_name',]
#     list_editable = ['image','localproductgroup',]
#     inlines = [ProductVariantInline,]
#     fieldsets = [
#         (None, {
#             'classes': ('suit-tab', 'suit-tab-api',),
#             'fields': ["name", "sku", "aura_id",],
#         }),
#         ("Categorization", {
#             'classes': ('suit-tab', 'suit-tab-api',),
#             'fields': ["productgroup", "brand", "country", "material_name",],
#         }),
#         ("Description", {
#             'classes': ('suit-tab', 'suit-tab-api','full-width',),
#             'fields': ["inventory_description",],
#         }),
#         ("Pricing", {
#             'classes': ('suit-tab', 'suit-tab-api',),
#             'fields': ["price", "color_price",],
#         }),
#
#         ("Resources", {
#             'classes': ('suit-tab', 'suit-tab-resources',),
#             'fields': ["size_chart_image_url", "mfg_product_url",],
#         }),
#
#         ("Media", {
#             'classes': ('suit-tab', 'suit-tab-media',),
#             'fields': ["image",],
#         }),
#
#         (None, {
#             'classes': ('suit-tab', 'suit-tab-local',),
#             'fields': ["local_name", "local_sku", "localproductgroup",],
#         }),
#         ("Description", {
#             'classes': ('suit-tab', 'suit-tab-local', 'full-width',),
#             'fields': ["local_description",],
#         }),
#     ]
#     suit_form_tabs = (
#         ('api','API'),
#         ('local','Local'),
#         ('media','Media'),
#         ('resources','Resources'),
#         ('variants','Product Variants'),
#     )
# admin.site.register(Product, ProductAdmin)
#
# class ProductVariantAdmin(admin.ModelAdmin):
#     list_display = ['get_sku','product','color','image',]
#     list_editable = ['image',]
#     list_filter = ['product','color','size']
# admin.site.register(ProductVariant, ProductVariantAdmin)
#
# class LocalProductGroupAdmin(admin.ModelAdmin):
#     list_display = ['name','get_num_products']
#     prepopulated_fields = {"slug": ("name",)}
# admin.site.register(LocalProductGroup, LocalProductGroupAdmin)
