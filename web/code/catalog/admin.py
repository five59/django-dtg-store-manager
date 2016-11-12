from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import *
from .forms import *
from django.utils.translation import ugettext_lazy as _
from django_extensions.admin import ForeignKeyAutocompleteAdmin


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    fields = ['name', 'code', ]
    suit_classes = 'suit-tab suit-tab-products'


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'has_key', ]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['code', 'name', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['consumer_url', 'dashboard_url', 'apibase_url']
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['api_key', 'api_hash', ]
        }),
    ]
    suit_form_tabs = (
        ('info', _('Info')),
    )
admin.site.register(Manufacturer, ManufacturerAdmin)


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = [
        'tree_actions',
        'indented_title',
    ]
    # list_display_links = (
    #     'indented_title',
    # ),
admin.site.register(Category, CategoryAdmin)


class GoogleCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(GoogleCategory, GoogleCategoryAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'name',
        'pms_code', 'pms_family',
        'hex_code',
        'r_value', 'g_value', 'b_value',
    ]
    list_filter = ['pms_family', ]
    fieldsets = [
        (None, {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['code', 'name'],
        }),
        ("PANTONE", {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['pms_code', 'pms_family', ],
        }),
        ("Web Color", {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['hex_code', 'r_value', 'g_value', 'b_value', ],
        }),
    ]
    suit_form_tabs = (
        ('info', _('Info')),
    )
admin.site.register(Color, ColorAdmin)


class SizeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Size, SizeAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'has_logo', 'has_description',
        # 'num_vendors','get_num_products',
        'consumer_url', 'wholesale_url'
    ]
    # list_editable = ['code', ]
    inlines = [ItemInline, ]
    form = BrandForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['code', 'name', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width',),
            'fields': ['description', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-media',),
            'fields': ['image', 'consumer_url', 'wholesale_url', 'product_base_url', ]
        })
    ]
    suit_form_tabs = (
        ('info', _('Info')),
        ('media', _('Media & Web')),
        ('products', _('Items'))
    )
admin.site.register(Brand, BrandAdmin)


class ItemAdmin(ForeignKeyAutocompleteAdmin):
    list_display = [
        'code', 'name',
        'brand', 'category', 'googlecategory',
        'age_group', 'gender', 'size_type',
    ]
    # related_search_fields = {
    #     'brand': ('name',),
    #     'category': ('name',),
    #     'googlecategory': ('name',),
    # }
    list_filter = (
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('category', admin.RelatedOnlyFieldListFilter),
        ('googlecategory', admin.RelatedOnlyFieldListFilter),
        'age_group',
        'gender',
        'size_type',
    )

    form = ItemForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info', ),
            'fields': [
                'code',
                'brand',
                'name',
            ],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width', ),
            'fields': [
                'description',
            ],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-categorization', ),
            'fields': [
                'category',
                'googlecategory',
            ],
        }),
        ("Metadata", {
            'classes': ('suit-tab', 'suit-tab-categorization', ),
            'fields': [
                'age_group',
                'gender',
                'material',
                'pattern',
            ],
        }),
        ("Sizing", {
            'classes': ('suit-tab', 'suit-tab-categorization', ),
            'fields': [
                'size_type',
                'size_system',
            ],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-media', ),
            'fields': [
                'link',
                'mobile_link',
            ],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-media', ),
            'fields': [
                'image',
                'additional_image',
            ],
        }),
    ]
    suit_form_tabs = (
        ('info', _("Info")),
        ('categorization', _("Categorization")),
        ('media', _("Web & Media")),

    )
admin.site.register(Item, ItemAdmin)


class ItemVariantAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'product', 'color', 'size', ]
    fieldsets = [
        (None, {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['code', 'name', 'product', ],
        }),
        ("Attributes", {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['color', 'size', ],
        }),
        ("Media & Web", {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['image', 'link', ],
        }),
    ]
    suit_form_tabs = (
        ('info', _('Info')),
    )
admin.site.register(ItemVariant, ItemVariantAdmin)
