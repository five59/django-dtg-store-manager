from django.contrib import admin
from .models import *

class BrandAdmin(admin.ModelAdmin):
    pass
admin.site.register(Brand, BrandAdmin)

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','group','plus_size_charge',]
    list_filter = ['group',]
admin.site.register(Size, SizeAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'group','color_hue','color_brightness',]
    list_filter = ['group',]
admin.site.register(Color, ColorAdmin)

class ShippingOptionAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(ShippingOption, ShippingOptionAdmin)

class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ['name','get_num_products']
admin.site.register(ProductGroup, ProductGroupAdmin)

class ShippingZoneAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(ShippingZone, ShippingZoneAdmin)

class ShippingAdmin(admin.ModelAdmin):
    list_display = ['group','option','zone','company','first_item_price','additional_item_price',]
    list_filter = ['group','option','zone',]
admin.site.register(Shipping, ShippingAdmin)

class AdditionalSettingsAdmin(admin.ModelAdmin):
    list_display = ['name','value',]
admin.site.register(AdditionalSettings, AdditionalSettingsAdmin)

class CountryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Country, CountryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku','localproductgroup','productgroup','brand','name', 'image',] #'get_num_variants','get_num_colors','get_num_sizes']
    list_filter = ['productgroup', 'localproductgroup', 'brand','country',]
    list_editable = ['image',]
admin.site.register(Product, ProductAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['get_sku','product','color','size',]
    list_filter = ['product','color','size']
admin.site.register(ProductVariant, ProductVariantAdmin)

class LocalProductGroupAdmin(admin.ModelAdmin):
    list_display = ['name','get_num_products']
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(LocalProductGroup, LocalProductGroupAdmin)
