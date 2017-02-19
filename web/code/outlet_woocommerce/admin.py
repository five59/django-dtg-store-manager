from django.contrib import admin
from .models import *
from django import forms
from django.utils.translation import ugettext_lazy as _

# Inlines


class wooTermInline(admin.TabularInline):
    model = wooTerm
    extra = 0
    can_delete = False
    fields = ("wid", "name", "menu_order", "count",)
    readonly_fields = ("wid", "count", )


class wpMediaSizeInline(admin.TabularInline):
    model = wpMediaSize
    extra = 0
    can_delete = False
    fields = ("name", "file", "mime_type", "width", "height",)
    readonly_fields = fields


# Main Admins

class wooStoreAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "base_url", "verify_ssl", "has_key", "has_secret",)
    list_filter = ("verify_ssl",)
admin.site.register(wooStore, wooStoreAdmin)


class wooProductAdmin(admin.ModelAdmin):
    list_display = (
        'wid',
        'sku',
        'name',
        'woostore',
        'status',
        'is_active',
        # "num_variants",
        # 'num_images',
    )
    list_filter = [
        'is_active',
        'status',
        ('woostore', admin.RelatedOnlyFieldListFilter),
        # ('design__series', admin.RelatedOnlyFieldListFilter),
        # ('design', admin.RelatedOnlyFieldListFilter),
        # ('item', admin.RelatedOnlyFieldListFilter),
        # 'product_type',
    ]
    # list_editable = [
    #     'design',
    #     'item',
    # ]
    search_fields = ['name', 'wid', 'sku']
    # form = ProductForm
    # inlines = (ProductImageInline, ProductVariationInline, )
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': [
                'sku',
                'name',
                'parent',
                'woostore',
            ]
        }),
        (_("Short Description"), {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width',),
            'fields': [
                'short_description',
                # 'attributes_string',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-details',),
            'fields': [
                'type',
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
                # 'download_limit',
                # 'download_expiry',
                # 'download_type',
            ]
        }),
        (_("External Products"), {
            'classes': ('suit-tab', 'suit-tab-inventory',),
            'fields': [
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
                'date_added',
                'date_updated',
                'date_created',
                'date_modified',
                'total_sales',
                'wid',
            ]
        }),
    ]
    readonly_fields = [
        'wid', 'sku', 'date_created', 'date_modified',
        'date_added', 'date_updated', 'total_sales',
        'purchasable', 'permalink',
        'price', 'on_sale', 'price_html', 'backorders_allowed', 'backordered',
        'shipping_required', 'shipping_taxable',
        'average_rating', 'rating_count',
        'description',
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

admin.site.register(wooProduct, wooProductAdmin)


class wooAttributeAdmin(admin.ModelAdmin):
    list_display = ("wid", "name", "slug", "type", "order_by",
                    "has_archives", "is_active", "store", "num_terms",
                    )
    list_filter = (
        ('store', admin.RelatedOnlyFieldListFilter),
        "type",
        "order_by",
        "has_archives",
    )
    readonly_fields = ("wid", )
    inlines = (wooTermInline,)
admin.site.register(wooAttribute, wooAttributeAdmin)


class wooImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(wooImage, wooImageAdmin)


class wooTermAdmin(admin.ModelAdmin):
    list_display = ("wid", "name", "slug", "productattribute", "is_active",
                    "menu_order", "count", "get_store_code",
                    'wr_tooltip', 'wr_color', 'wr_label',
                    )
    list_filter = (
        ('productattribute__store', admin.RelatedOnlyFieldListFilter),
        ('productattribute', admin.RelatedOnlyFieldListFilter),
    )
    list_editable = (
        'menu_order', 'wr_tooltip', 'wr_color', 'wr_label',
    )
    readonly_fields = ("wid", "count", "is_active", )
admin.site.register(wooTerm, wooTermAdmin)


class wooCategoryAdmin(admin.ModelAdmin):
    list_display = ("wid", "name", "parent", "display", "image_id", "count", "is_active")
    list_filter = (
        ('store', admin.RelatedOnlyFieldListFilter),
    )
    readonly_fields = ("wid", "image_id", "count", )
admin.site.register(wooCategory, wooCategoryAdmin)


class wooTagAdmin(admin.ModelAdmin):
    list_display = ("wid", "name", "slug", "count", "is_active")
    list_filter = (
        ('store', admin.RelatedOnlyFieldListFilter),
    )
    readonly_fields = ("wid", "count", )
admin.site.register(wooTag, wooTagAdmin)


class wooVariantAdmin(admin.ModelAdmin):
    pass
admin.site.register(wooVariant, wooVariantAdmin)


class wpMediaAdmin(admin.ModelAdmin):
    list_display = ("wid", "file", "alt_text", "title", "slug", "woostore", "is_active",)
    list_filter = ("woostore",)
    inlines = (wpMediaSizeInline, )
admin.site.register(wpMedia, wpMediaAdmin)


class wpMediaSizeAdmin(admin.ModelAdmin):
    list_display = ("wpmedia", "name", "file", "width", "height",)
admin.site.register(wpMediaSize, wpMediaSizeAdmin)
