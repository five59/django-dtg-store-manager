from mptt.admin import *
from django.contrib import admin
from .models import *
from django_mptt_admin.admin import DjangoMpttAdmin

# MASTER ADMIN
class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    fields = ['name','master_id','id_type',]
    suit_classes = 'suit-tab suit-tab-products'
class VariantInline(admin.TabularInline):
    model = Variant
    extra = 0
    fields = ['title','color','size',]
    suit_classes = 'suit-tab suit-tab-variants'
class VendorProductInline(admin.TabularInline):
    model = VendorProduct
    extra = 0
    fields = ['vendor','brand','mpn','name']
    suit_classes = 'suit-tab suit-tab-vendorproducts'
class VendorVariantInline(admin.TabularInline):
    model = VendorVariant
    extra = 0
    fields = ['vendor_id','vendor_color','vendor_size',]
    # suit_classes = 'suit-tab suit-tab-vendorvariants'
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','has_logo','has_description',
      'num_vendors','get_num_products','consumer_url','wholesale_url']
    # list_editable = ['image',]
    inlines = [ProductInline, ]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['name','image','consumer_url','wholesale_url','description']
        })
    ]
    suit_form_tabs = (
        ('info','Info'),
        ('products','Products')
    )
class PODVendorAdmin(admin.ModelAdmin):
    list_display = ['name','code','has_key','consumer_url','dashboard_url','apibase_url',]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['name','code',]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['consumer_url', 'dashboard_url','apibase_url','api_key','api_hash']
        }),
    ]
    suit_form_tabs = (
        ('info','Info'),
    )
class ColorAdmin(admin.ModelAdmin):
    list_display = [
          'name',
          'pms_code','pms_family',
          'hex_code',
          'r_value','g_value','b_value',
          'get_num_variants','get_num_vendorcolor',]
    list_filter = ['pms_family',]
    inlines = (VariantInline, )
class GoogleCategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','grouping','sortorder']
    list_filter = ['grouping',]
    # list_editable = ['grouping','sortorder',]
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = [
        'tree_actions',
        'indented_title',
        'num_products',
    ]
    mptt_level_indent = 50
class OutletAdmin(admin.ModelAdmin):
    list_display = ['name','category','web_url',]
    list_filter = ['category',]
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'brand',
        'master_id',
        'name',
        'size_type',
        'gender',
        'age_group',
        'vendor_count',
        'category',
        'googlecategory',
    ]
    inlines = (VariantInline, VendorProductInline, )
    list_filter = [ 'brand', 'gender','age_group', 'size_type', 'category', ]
    list_editable = [
        # 'master_id',
        # 'category',
        # 'size_type',
        # 'gender',
        # 'age_group',
        ]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['name','brand',]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['master_id', 'id_type',]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['description',]
        }),
        (None, {
          'classes': ('suit-tab', 'suit-tab-media',),
          'fields': ['link', 'mobile_link',]
        }),
        ("Categorization", {
            'classes': ('suit-tab', 'suit-tab-meta',),
            'fields': [
              'category',
              'googlecategory',
              'age_group',
              'gender',
              'material',
              'pattern',
            ]
        }),
        ("Size", {
            'classes': ('suit-tab', 'suit-tab-meta',),
            'fields': [
              'size_type',
              'size_system',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-media',),
            'fields': [  'image', 'additional_image_link',]
        }),
    ]
    suit_form_tabs = (
        ('info','Info'),
        ('meta','Classifications'),
        ('media','Media & Reference'),
        ('variants','Variants'),
        ('vendorproducts','Vendors Products'),
    )
    # list_editable = ['gender','age_group',]
class VariantAdmin(admin.ModelAdmin):
    list_display = ['title','product','color','size',]

# VENDOR ADMIN
class VendorBrandAdmin(admin.ModelAdmin):
    list_display = ['name','num_products','master_brand','vendor',]
    list_filter = ['vendor',]
    list_editable = ['master_brand',]
    order_by = ['num_products',]
class VendorSizeAdmin(admin.ModelAdmin):
    list_display = ['vendor_code','vendor_name','vendor','vendor_grouping','master_size',]
    list_filter = ['vendor','master_size',]
    # list_editable = ['master_size',]
class VendorVariantAdmin(admin.ModelAdmin):
    list_display = ['vendor_id','podvendor','vendor_product','in_stock','price',]
    list_filter = ['podvendor',]
class VendorCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','vendor',]
    list_filter = ['vendor',]
class VendorProductAdmin(admin.ModelAdmin):
    list_display = ['mpn','vendor','brand','sku','category','name','master_product',]
    list_filter = ['vendor', 'brand','category',]
    list_editable = ['master_product',]
    inlines = (VendorVariantInline, )
class VendorColorAdmin(admin.ModelAdmin):
    list_display = ['vendor_code', 'vendor', 'color_name', 'color_code', 'color_group','master_color',]
    list_filter = [
        'vendor',
        ('master_color', admin.RelatedOnlyFieldListFilter),
    ]

# CREATIVE ADMIN
class CreativeInline(admin.TabularInline):
    model = Creative
    extra = 0
    fields = ['code','name','artist',]
    suit_classes = 'suit-tab suit-tab-creative'
class CreativeArtistInline(admin.TabularInline):
    model = Creative
    extra = 0
    fields = ['full_code','name','series',]
    # order_by = ['series','name',]
    suit_classes = 'suit-tab suit-tab-creative'
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['full_code', 'name', 'series']
        return self.readonly_fields

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name','has_agreement','location','web','num_assigned','num_live','total_creative',]
    list_filter = ['has_agreement','location',]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['name','has_agreement',]
        }),
        ("Contact", {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['web','phone','email','location',]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-agreement',),
            'fields': ['agreement',]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-notes',),
            'fields': ['notes',]
        }),
    ]
    inlines = (CreativeArtistInline,)
    suit_form_tabs = (
        ('info','Info'),
        ('agreement','Agreement'),
        ('notes','Notes'),
        ('creative','Creative'),
    )
class CreativeAdmin(admin.ModelAdmin):
    list_display = ['full_code','status_tag','name','artist','series',] #'series_name','series_outlet']
    list_filter = ['status','artist','series',]
    order_by = ['series','name',]
    # list_editable = ['artist',]
class CreativeSeriesAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'num_creative',
        'name',
        'primary_outlet',
        ]
    list_filter = ['primary_outlet',]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['code','name','primary_outlet',]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-notes',),
            'fields': ['note',]
        }),
    ]
    suit_form_tabs = (
        ('info','Info'),
        ('creative','Creative'),
        ('notes','Notes'),
    )
    inlines = (CreativeInline,)

admin.site.register(Brand, BrandAdmin)
admin.site.register(PODVendor, PODVendorAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(GoogleCategory, GoogleCategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Outlet, OutletAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)

admin.site.register(VendorBrand, VendorBrandAdmin)
admin.site.register(VendorSize, VendorSizeAdmin)
admin.site.register(VendorVariant, VendorVariantAdmin)
admin.site.register(VendorCategory, VendorCategoryAdmin)
admin.site.register(VendorProduct, VendorProductAdmin)
admin.site.register(VendorColor, VendorColorAdmin)

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Creative, CreativeAdmin)
admin.site.register(CreativeSeries, CreativeSeriesAdmin)
