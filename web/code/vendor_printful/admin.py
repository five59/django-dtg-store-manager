from django.contrib import admin
# from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import *
# from .forms import *
from django.utils.translation import ugettext_lazy as _
from django_extensions.admin import ForeignKeyAutocompleteAdmin


# Inlines

class pfCatalogFileTypeInline(admin.TabularInline):
    model = pfCatalogFileType
    fields = ('pid', 'title', 'additional_price', 'pfcatalogfilespec',)
    readonly_fields = ('pid', 'title', 'additional_price',)
    can_delete = False
    extra = 0
    suit_classes = "suit-tab suit-tab-pfcatalogfiletype"


class pfCatalogOptionTypeInline(admin.TabularInline):
    model = pfCatalogOptionType
    fields = ('pid', 'type', 'title', 'additional_price',)
    readonly_fields = fields
    can_delete = False
    extra = 0
    suit_classes = "suit-tab suit-tab-pfcatalogoptiontype"


class pfCatalogVariantInline(admin.TabularInline):
    model = pfCatalogVariant
    fields = ('get_sku_part',
              #   'pid', 'name',
              'pfsize', 'pfcolor',
              'price', 'in_stock',)
    readonly_fields = fields
    can_delete = False
    extra = 0


class pfStateInline(admin.TabularInline):
    model = pfState
    fields = ('code', 'name',)
    readonly_fields = fields
    can_delete = False
    extra = 0

# Admin Models

# class pfAddress(admin.ModelAdmin)
# class pfCardInfo(admin.ModelAdmin)


class pfCatalogColorAdmin(admin.ModelAdmin):
    list_display = ("label", "code", "label_clean", "hex_code",)
    readonly_fields = ("label", "hex_code",)
    list_editable = ("code", "label_clean", )
admin.site.register(pfCatalogColor, pfCatalogColorAdmin)


class pfCatalogFileSpecAdmin(admin.ModelAdmin):
    list_display = ('get_dimensions', 'name',
                    'width_in', 'height_in',
                    'note', 'ratio', 'colorsystem',)
    # list_editable = ('name',)
    list_filter = ('width_in', 'height_in')
admin.site.register(pfCatalogFileSpec, pfCatalogFileSpecAdmin)


class pfCatalogFileTypeAdmin(admin.ModelAdmin):
    list_display = ('get_pfcatalogproduct_brand', 'get_pfcatalogproduct_model',
                    'title', 'pfcatalogfilespec', 'get_pfcatalogvariant_size',)
    list_editable = ('pfcatalogfilespec',)
    list_filter = ('pfcatalogvariant__pfcatalogproduct__brand',
                   'pfcatalogvariant__pfcatalogproduct__model',
                   'pfcatalogvariant__pfsize',
                   'title', 'pfcatalogfilespec',)
admin.site.register(pfCatalogFileType, pfCatalogFileTypeAdmin)


class pfCatalogOptionTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(pfCatalogOptionType, pfCatalogOptionTypeAdmin)


class pfCatalogProductAdmin(admin.ModelAdmin):
    list_display = ('pid', 'type', 'brand', 'model',
                    'variant_count', 'num_colors', 'num_sizes',
                    'is_active', 'num_out_of_stock', )
    list_filter = ('type', 'brand', 'is_active',)
    search_fields = ('pid', 'brand', 'model',)
    fields = ('id', 'pid', 'type', 'brand', 'model', 'image',
              'variant_count', 'get_colors_as_string', 'get_sizes_as_string',)
    readonly_fields = fields
    inlines = (pfCatalogVariantInline, )
admin.site.register(pfCatalogProduct, pfCatalogProductAdmin)


class pfCatalogSizeAdmin(admin.ModelAdmin):
    list_display = ("label", "code", "label_clean", "sort_group", "sort_order",)
    readonly_fields = ("label",)
    list_filter = ("sort_group",)
    list_editable = ("code", "label_clean", "sort_order",)
admin.site.register(pfCatalogSize, pfCatalogSizeAdmin)


class pfCatalogVariantAdmin(admin.ModelAdmin):
    list_display = ('pid', 'get_brand', 'pfcatalogproduct', 'pfsize', 'pfcolor', 'price',
                    'in_stock', 'is_active', )
    list_filter = ('pfsize', 'pfcolor', 'in_stock', 'is_active',
                   'pfcatalogproduct__brand', 'pfcatalogproduct', )
    search_fields = ('pid', 'name',)
    inlines = (pfCatalogOptionTypeInline, pfCatalogFileTypeInline, )
    readonly_fields = (
        'image', 'price', 'in_stock', 'id', 'date_added', 'date_updated', 'is_active', 'pid',)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-basic',),
            'fields': ('name', 'pfcatalogproduct',),
        }),
        (_("Attributes"), {
            'classes': ('suit-tab', 'suit-tab-basic',),
            'fields': ('pfsize', 'pfcolor',),
        }),
        (_("Info"), {
            'classes': ('suit-tab', 'suit-tab-basic',),
            'fields': ('image', 'price', 'weight', 'in_stock',),
        }),
        (_("USA"), {
            'classes': ('suit-tab', 'suit-tab-shipping',),
            'fields': ('ship_us_1', 'ship_us_2',),
        }),
        (_("Canada"), {
            'classes': ('suit-tab', 'suit-tab-shipping',),
            'fields': ('ship_ca_1', 'ship_ca_2',),
        }),
        (_("Worldwide"), {
            'classes': ('suit-tab', 'suit-tab-shipping',),
            'fields': ('ship_ww_1', 'ship_ww_2',),
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-meta',),
            'fields': ('id', 'date_added', 'date_updated', 'is_active', 'pid',),
        }),
    ]
    suit_form_tabs = (
        ("basic", "Basic"),
        ("pfcatalogfiletype", "Files"),
        ("pfcatalogoptiontype", "Options"),
        ("shipping", "Shipping"),
        ("meta", "Metadata"),
    )
admin.site.register(pfCatalogVariant, pfCatalogVariantAdmin)

# pfCosts


class pfCountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'num_states',)
    search_fields = ('code', 'name',)
    fields = ('code', 'name',)
    readonly_fields = fields
    inlines = (pfStateInline, )
admin.site.register(pfCountry, pfCountryAdmin)

# pfOrder
# pfOrderGiftData
# pfOrderItem
# pfPackingSlip


class pfPrintFileAdmin(admin.ModelAdmin):
    list_display = ('get_thumb_html', 'pid', 'pfstore', 'filename', 'pfcatalogfilespec',
                    'get_dimensions', 'type', 'status', 'visible',)
    list_filter = ('pfstore', 'mime_type', 'status', 'type', 'visible', 'pfcatalogfilespec',)
    readonly_fields = ('pid', 'type', 'hash', 'url', 'filename', 'mime_type', 'size', 'width',
                       'height', 'dpi', 'status', 'created', 'thumbnail_url', 'preview_url', 'visible')

admin.site.register(pfPrintFile, pfPrintFileAdmin)

# pfShipment
# pfShipmentItem
# pfShipingInfo


class pfStateAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'pfcountry',)
    list_filter = ('pfcountry',)
    search_fields = ('code', 'name',)
    fields = ('code', 'name', 'pfcountry',)
    readonly_fields = fields
admin.site.register(pfState, pfStateAdmin)


class pfStoreAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'has_api_auth', 'date_added', 'date_updated',)
admin.site.register(pfStore, pfStoreAdmin)


class pfSyncItemOptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(pfSyncItemOption, pfSyncItemOptionAdmin)


class pfSyncProductAdmin(admin.ModelAdmin):
    list_display = ('pid', 'external_id', 'name', 'pfstore', 'variants', 'synced', 'all_synced',)
    list_filter = ('pfstore',)
admin.site.register(pfSyncProduct, pfSyncProductAdmin)


class pfSyncVariantAdmin(admin.ModelAdmin):
    list_display = ('pid', 'external_id', 'name', 'synced',
                    'pfsyncproduct', 'pfcatalogvariant', 'get_store_code',)
    list_filter = ('pfsyncproduct', 'pfcatalogvariant', 'synced', 'pfsyncproduct__pfstore')
admin.site.register(pfSyncVariant, pfSyncVariantAdmin)
