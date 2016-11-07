# from django.contrib import admin
# from .models import *
#
# # INLINES
#
# class PrintFileInline(admin.TabularInline):
#     model = pfPrintFile
#     # suit_classes = "suit-tab suit-tab-PrintFile"
#
# class ProductOptionInline(admin.TabularInline):
#     model = pfProductOption
#     # suit_classes = "suit-tab suit-tab-ProductValue"
#
# class ProductDimensionInline(admin.TabularInline):
#     model = pfProductDimension
#     # suit_classes = "suit-tab suit-tab-ProductDimension"
#
# class OptionValueInline(admin.TabularInline):
#     model = pfOptionValue
#     # suit_classes = "suit-tab suit-tab-ProductOption"
#
# class ProductInline(admin.TabularInline):
#     model = pfProduct
#     fields = ['vendor_id','brand','model',]
#
# # ADMINS
#
# class ProductTypeAdmin(admin.ModelAdmin):
#     list_display = ['name',]
#     inlines = (ProductInline,)
# admin.site.register(pfProductType, ProductTypeAdmin)
#
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ['name','is_linked',]
#     inlines = (ProductInline, )
# admin.site.register(pfBrand, BrandAdmin)
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['model','brand','product_type','price_range','num_variants',]
#     list_filter = ['brand','product_type',]
#     inlines = ( PrintFileInline, ProductDimensionInline, ProductOptionInline, )
# admin.site.register(pfProduct, ProductAdmin)
#
# class PrintFileAdmin(admin.ModelAdmin):
#     list_display = ['product','title','additional_price',]
#     list_filter = ['product',]
# admin.site.register(pfPrintFile, PrintFileAdmin)
#
# class OptionValueAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(pfOptionValue, OptionValueAdmin)
#
# class ProductDimensionAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(pfProductDimension, ProductDimensionAdmin)
#
# class ProductOptionAdmin(admin.ModelAdmin):
#     list_display = ['title','optiontype','product',]
#     list_filter = ['product',]
#     inlines = (OptionValueInline, )
# admin.site.register(pfProductOption, ProductOptionAdmin)
#
# class ProductVariantAdmin(admin.ModelAdmin):
#     list_filter = ['product',]
# admin.site.register(pfProductVariant, ProductVariantAdmin)
