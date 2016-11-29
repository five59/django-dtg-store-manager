# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import *
from django.utils.translation import ugettext_lazy as _


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    fields = ['code', 'name', 'src', 'alt', 'position', ]
    readonly_fields = fields
    suit_classes = 'suit-tab suit-tab-productimages'


class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 0
    fields = ['code', 'name', 'sku', 'price', 'att_color',
              'att_color_obj', 'att_size', 'att_size_obj', ]
    readonly_fields = fields
    # ['code', 'name', 'price', 'att_color', 'att_size', ]

    suit_classes = 'suit-tab suit-tab-productvariants'


class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'web_url',
        'has_key',
        'has_secret',
        'num_products',
        'last_sync',
    )
    readonly_fields = ('last_sync', 'num_products',)
admin.site.register(Shop, ShopAdmin)


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'product',
        'price',
        'regular_price',
        'att_color',
        'att_color_obj',
        'att_size',
        'att_size_obj',
    )
    list_editable = [
        # 'att_color_obj',
        'att_size_obj',
    ]
    list_filter = (
        ('product__item', admin.RelatedOnlyFieldListFilter),
        ('att_color_obj', admin.RelatedOnlyFieldListFilter),
        ('att_size_obj', admin.RelatedOnlyFieldListFilter),
    )
admin.site.register(ProductVariation, ProductVariationAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        # 'code',
        'sku',
        'name',
        # 'shop',
        'design',
        'item',
        'has_attributes_string',
        'product_type',
        "is_active",
        "status",
        'num_images',
    )
    list_filter = [
        'is_active',
        'status',
        ('shop', admin.RelatedOnlyFieldListFilter),
        ('design', admin.RelatedOnlyFieldListFilter),
        ('item', admin.RelatedOnlyFieldListFilter),
        # 'product_type',
    ]
    # list_editable = [
    #     'design',
    #     'item',
    # ]
    search_fields = ['name', 'code', 'sku']
    form = ProductForm
    inlines = (ProductImageInline, ProductVariationInline, )
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': [
                'sku',
                'name',
                'parent',
                'shop',
                'item',
                'design',
            ]
        }),
        (_("Short Description"), {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width',),
            'fields': [
                'short_description',
                'attributes_string',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-details',),
            'fields': [
                'product_type',
                'status',
                'catalog_visibility',
            ]
        }),
        (_("Flags"), {
            'classes': ('suit-tab', 'suit-tab-details',),
            'fields': [
                'is_active',
                'purchasable',
                'featured',
            ]
        }),
        (_("Additional"), {
            'classes': ('suit-tab', 'suit-tab-details',),
            'fields': [
                'purchase_note',
                'menu_order',
            ]
        }),
        (_("Web"), {
            'classes': ('suit-tab', 'suit-tab-details',),
            'fields': [
                'slug',
                'permalink',
            ]
        }),


        (_("Description"), {
            'classes': ('suit-tab', 'suit-tab-description', 'full-width'),
            'fields': [
                'description',
            ]
        }),

        # === PRICING === #
        (None, {
            'classes': ('suit-tab', 'suit-tab-pricing',),
            'fields': [
                'price',
                'regular_price',
            ]
        }),
        (_("Sale Details"), {
            'classes': ('suit-tab', 'suit-tab-pricing',),
            'fields': [
                'on_sale',
                'sale_price',
                'date_on_sale_from',
                'date_on_sale_to',
                'price_html',
            ]
        }),
        (_("Tax"), {
            'classes': ('suit-tab', 'suit-tab-pricing',),
            'fields': [
                'tax_status',
                'tax_class',
            ]
        }),


        # === INVENTORY === #

        (_("Stock"), {
            'classes': ('suit-tab', 'suit-tab-inventory',),
            'fields': [
                'manage_stock',
                'stock_quantity',
                'in_stock',
                'backorders',
                'backorders_allowed',
                'backordered',
                'sold_individually',
            ]
        }),
        (_("Shipping"), {
            'classes': ('suit-tab', 'suit-tab-inventory',),
            'fields': [
                'weight',
                'shipping_required',
                'shipping_taxable',
            ]
        }),
        (_("Virtual Products"), {
            'classes': ('suit-tab', 'suit-tab-inventory',),
            'fields': [
                'virtual',
                'downloadable',
                'download_limit',
                'download_expiry',
                'download_type',
                'external_url',
                'button_text',
            ]
        }),

        # === REVIEWS === #

        (None, {
            'classes': ('suit-tab', 'suit-tab-reviews',),
            'fields': [
                'reviews_allowed',
                'average_rating',
                'rating_count',
            ]
        }),


        (_("Metadata"), {
            'classes': ('suit-tab', 'suit-tab-metadata',),
            'fields': [
                'app_added',
                'app_last_sync',
                'date_created',
                'date_modified',
                'total_sales',
                'code',
            ]
        }),
    ]
    readonly_fields = [
        'code', 'date_created', 'date_modified',
        'app_added', 'app_last_sync', 'total_sales',
        'purchasable', 'permalink',
        'price', 'on_sale', 'price_html', 'backorders_allowed', 'backordered',
        'shipping_required', 'shipping_taxable',
        'average_rating', 'rating_count',
    ]
    suit_form_tabs = (
        ('info', _('Basic Info')),
        ('description', _('Description')),
        ('details', _('Details')),
        ('pricing', _('Pricing')),
        ('inventory', _('Inventory')),
        ('reviews', _('Reviews')),
        ('productimages', _('Images')),
        ('productvariants', _('Variants')),
        ('metadata', _('Metadata')),
    )
admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'name',
        'product',
        'position',
        'has_local_image',
    ]
admin.site.register(ProductImage, ProductImageAdmin)


class ProductAttributeTermInline(admin.TabularInline):
    model = ProductAttributeTerm
    extra = 0
    fields = ['code', 'name', 'menu_order', 'count', ]
    readonly_fields = ['code', 'count', ]


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'shop', 'has_archives', 'input_type', 'order_by', ]
    # list_editable = ['shop', ]
    list_filter = ['shop', ]
    inlines = (ProductAttributeTermInline,)
admin.site.register(ProductAttribute, ProductAttributeAdmin)


class ProductAttributeTermAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'productattribute', 'menu_order', 'count', ]
    list_filter = ['productattribute', ]
admin.site.register(ProductAttributeTerm, ProductAttributeTermAdmin)
