from django.contrib import admin
# from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import *
from .forms import *
from django.utils.translation import ugettext_lazy as _
from django_extensions.admin import ForeignKeyAutocompleteAdmin


# INLINES

class bzCreativeDesignInline(admin.TabularInline):
    model = bzCreativeDesign
    extra = 0
    suit_classes = "suit-tab suit-tab-bzCreativeDesign"


class bzCreativeLayoutInline(admin.TabularInline):
    model = bzCreativeLayout
    extra = 0
    suit_classes = "suit-tab suit-tab-bzCreativeLayout"


class bzProductVariantInline(admin.TabularInline):
    model = bzProductVariant
    extra = 0
    can_delete = False
    fields = ('code', 'pfcatalogvariant', 'is_active', 'get_color', 'get_size',)
    readonly_fields = fields
    suit_classes = "suit-tab suit-tab-bzProductVariant"


# ADMINS

class bzBrandAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "vendor", "outlet", )

admin.site.register(bzBrand, bzBrandAdmin)


class bzProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'bzDesign', 'bzLayout',
                    'pfProduct', 'wcProduct', 'num_pfvariants',)
    list_filter = ('bzDesign', 'pfProduct', 'bzDesign__bzcreativecollection__bzbrand')
    readonly_fields = ('code', 'num_pfvariants', 'get_pfvariants',)
    inlines = (bzProductVariantInline, )
    fieldsets = [
        ("Basics", {
            'classes': ('suit-tab', 'suit-tab-step1',),
            'fields': ('code', 'name', ),
        }),
        ("Product Configuration", {
            'classes': ('suit-tab', 'suit-tab-step1',),
            'fields': ('bzDesign', 'bzLayout', 'pfProduct', ),
        }),
        ("Product Publishing", {
            'classes': ('suit-tab', 'suit-tab-step1',),
            'fields': ('wcProduct', ),
        }),

        (None, {
            'classes': ('suit-tab', 'suit-tab-step2',),
            'fields': ('num_pfvariants',),
        }),
        ("Colors", {
            'classes': ('suit-tab', 'suit-tab-step2',),
            'fields': ('pfColors',),
        }),
        ("Sizes", {
            'classes': ('suit-tab', 'suit-tab-step2',),
            'fields': ('pfSizes', ),
        }),

        (None, {
            'classes': ('suit-tab', 'suit-tab-step3',),
            'fields': ('get_pfvariants',),
        }),
    ]

    suit_form_tabs = (
        ('step1', "Step 1"),
        ('step2', "Step 2"),
        ('bzProductVariant', "Variants"),
    )
    form = bzProductForm
admin.site.register(bzProduct, bzProductAdmin)


class bzProductVariantAdmin(admin.ModelAdmin):
    list_display = ("code", "is_active", 'bzproduct', 'pfcatalogvariant', 'get_color', 'get_size',)
    list_filter = ('is_active', 'bzproduct', )
    search_fields = ("code",)
admin.site.register(bzProductVariant, bzProductVariantAdmin)


class bzCreativeCollectionAdmin(admin.ModelAdmin):
    list_display = ("code", "name", )
    inlines = (bzCreativeDesignInline, bzCreativeLayoutInline, )
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-basic',),
            'fields': ('code', 'name',),
        }),
    ]
    suit_form_tabs = (
        ("basic", "Basic"),
        ("bzCreativeDesign", _("Designs")),
        ("bzCreativeLayout", _("Layouts")),
    )
admin.site.register(bzCreativeCollection, bzCreativeCollectionAdmin)


class bzCreativeDesignAdmin(admin.ModelAdmin):
    list_display = ("code", "name", )
    list_filter = ("bzcreativecollection",)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-basic',),
            'fields': ('code', 'name',),
        }),
    ]
    suit_form_tabs = (
        ("basic", "Basic"),
    )
admin.site.register(bzCreativeDesign, bzCreativeDesignAdmin)


class bzCreativeLayoutAdmin(admin.ModelAdmin):
    list_display = ("code", "name", )
    list_filter = ("bzcreativecollection",)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-basic',),
            'fields': ('code', 'name',),
        }),
    ]
    suit_form_tabs = (
        ("basic", "Basic"),
    )
admin.site.register(bzCreativeLayout, bzCreativeLayoutAdmin)


class bzCreativeRenderingAdmin(admin.ModelAdmin):
    list_display = ('bzcreativedesign', 'bzcreativelayout', 'pfcatalogfilespec', 'pfprintfile',)
    list_filter = ('bzcreativedesign', 'bzcreativelayout', 'pfcatalogfilespec',)
    fieldsets = [
        ("Step 1", {
            'fields': ['bzcreativedesign', ],
        }),
        ("Step 2", {
            'fields': ['bzcreativelayout', 'pfcatalogfilespec', 'pfprintfile', ],
        }),
    ]
    form = bzCreativeRenderingForm
admin.site.register(bzCreativeRendering, bzCreativeRenderingAdmin)
