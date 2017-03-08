from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *
from .forms import *

# Inlines


class pfCatalogFileTypeInline(admin.TabularInline):
    model = pfCatalogFileType
    fields = ('pid', 'title', 'additional_price', 'pfcatalogfilespec',)
    readonly_fields = ('pid', 'title', 'additional_price',)
    can_delete = False
    extra = 0


class pfCatalogOptionTypeInline(admin.TabularInline):
    model = pfCatalogOptionType
    fields = ('pid', 'type', 'title', 'additional_price',)
    readonly_fields = fields
    can_delete = False
    extra = 0


class pfCatalogVariantInline(admin.TabularInline):
    model = pfCatalogVariant
    fields = ('get_sku_part', 'pfsize', 'pfcolor', 'price', 'in_stock',)
    readonly_fields = fields
    can_delete = False
    extra = 0


class pfStateInline(admin.TabularInline):
    model = pfState
    fields = ('code', 'name',)
    readonly_fields = fields
    can_delete = False
    extra = 0


# Standard Admins

class bzBrandAdmin(admin.ModelAdmin):
    form = bzBrandForm
    list_display = ['code', 'name', 'vendor', 'outlet', ]
    readonly_fields = ['id', 'date_added', 'date_updated']
    list_filter = ['vendor', 'outlet', ]
    search_fields = ['id', 'code', 'name', ]


admin.site.register(bzBrand, bzBrandAdmin)


class bzCreativeCollectionAdmin(admin.ModelAdmin):
    form = bzCreativeCollectionForm
    list_display = [
        'id', 'date_added', 'date_updated',
        'code', 'name', 'bzbrand',
    ]
    readonly_fields = ['id', 'date_added', 'date_updated']
    list_filter = ['bzbrand', ]
    search_fields = ['id', 'name', 'code', ]


admin.site.register(bzCreativeCollection, bzCreativeCollectionAdmin)


class bzCreativeDesignAdmin(admin.ModelAdmin):
    form = bzCreativeDesignForm
    list_display = [
        'id', 'date_added', 'date_updated',
        'code', 'name', 'bzcreativecollection',
    ]
    readonly_fields = ['id', 'date_added', 'date_updated', ]
    list_filter = ['bzcreativecollection', ]
    search_fields = ['id', 'name', 'code', ]


admin.site.register(bzCreativeDesign, bzCreativeDesignAdmin)


class bzCreativeLayoutAdmin(admin.ModelAdmin):
    form = bzCreativeLayoutForm
    list_display = [
        'id', 'date_added', 'date_updated',
        'code', 'name', 'bzcreativecollection',
    ]
    readonly_fields = ['id', 'date_added', 'date_updated', ]
    list_filter = ['bzcreativecollection', ]
    search_fields = ['id', 'name', 'code', ]


admin.site.register(bzCreativeLayout, bzCreativeLayoutAdmin)


class bzCreativeRenderingAdmin(admin.ModelAdmin):
    form = bzCreativeRenderingForm
    list_display = [
        'id', 'date_added', 'date_updated',
        'bzcreativedesign', 'bzcreativelayout',
    ]
    readonly_fields = ['id', 'date_added', 'date_updated', ]
    list_filter = ['bzcreativedesign', 'bzcreativelayout', ]
    search_fields = ['id', ]


admin.site.register(bzCreativeRendering, bzCreativeRenderingAdmin)


class bzProductAdmin(admin.ModelAdmin):
    form = bzProductForm
    list_display = [
        'id', 'date_added', 'date_updated',
        'code', 'name', 'status',
        'bzDesign', 'pfProduct', 'wooProduct', 'pfSyncProduct',
    ]
    readonly_fields = ['id', 'date_added', 'date_updated', ]
    list_filter = [
        'status', 'bzDesign', 'pfProduct', 'wooProduct', 'pfSyncProduct',
    ]
    search_fields = ['id', 'name', 'code', ]


admin.site.register(bzProduct, bzProductAdmin)


class bzProductVariantAdmin(admin.ModelAdmin):
    form = bzProductVariantForm
    list_display = [
        'id', 'date_added', 'date_updated',
        'code', 'is_active',
        'bzproduct', 'pfcatalogvariant', 'pfcolor', 'pfsize', 'price',
    ]
    readonly_fields = ['id', 'date_added', 'date_updated', ]
    list_filter = [
        'bzproduct', 'pfcatalogvariant', 'pfcolor', 'pfsize',
    ]
    search_fields = ['id', 'code', ]


admin.site.register(bzProductVariant, bzProductVariantAdmin)


class wooAttributeAdminForm(forms.ModelForm):

    class Meta:
        model = wooAttribute
        fields = '__all__'


class wooAttributeAdmin(admin.ModelAdmin):
    form = wooAttributeAdminForm
    list_display = ['id', 'date_added', 'date_updated',
                    'is_active', 'wid', 'name', 'slug', 'type', 'has_archives']
    readonly_fields = ['id', 'date_added', 'date_updated',
                       'is_active', 'wid', 'name', 'slug',
                       'type', 'has_archives']


admin.site.register(wooAttribute, wooAttributeAdmin)


class wooCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = wooCategory
        fields = '__all__'


class wooCategoryAdmin(admin.ModelAdmin):
    form = wooCategoryAdminForm
    list_display = ['id', 'date_added', 'date_updated',
                    'is_active', 'wid', 'name', 'slug',
                    'parent', 'description', 'display', 'count',
                    'image_id', 'image_date_created']
    readonly_fields = ['id', 'date_added', 'date_updated',
                       'is_active', 'wid', 'name',
                       'slug', 'parent', 'description', 'display',
                       'count', 'image_id', 'image_date_created']


admin.site.register(wooCategory, wooCategoryAdmin)


class wooImageAdminForm(forms.ModelForm):

    class Meta:
        model = wooImage
        fields = '__all__'


class wooImageAdmin(admin.ModelAdmin):
    form = wooImageAdminForm
    list_display = ['id', 'date_added', 'date_updated',
                    'is_active', 'wid', 'date_created', 'alt', 'position']
    readonly_fields = ['id', 'date_added', 'date_updated',
                       'is_active', 'wid', 'date_created', 'alt', 'position']


admin.site.register(wooImage, wooImageAdmin)


class wooProductAdminForm(forms.ModelForm):

    class Meta:
        model = wooProduct
        fields = '__all__'


class wooProductAdmin(admin.ModelAdmin):
    form = wooProductAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'is_active',
                    'wid', 'slug', 'permalink',
                    'date_created', 'dimension_length', 'dimension_width',
                    'dimension_height', 'weight', 'reviews_allowed']
    readonly_fields = ['id', 'date_added', 'date_updated', 'is_active', 'wid',
                       'slug', 'permalink',
                       'date_created', 'dimension_length', 'dimension_width',
                       'dimension_height', 'weight', 'reviews_allowed']


admin.site.register(wooProduct, wooProductAdmin)


class wooShippingClassAdminForm(forms.ModelForm):

    class Meta:
        model = wooShippingClass
        fields = '__all__'


class wooShippingClassAdmin(admin.ModelAdmin):
    form = wooShippingClassAdminForm
    list_display = ['id', 'wid', 'name', 'slug', 'description', 'count']
    readonly_fields = ['id', 'wid', 'name', 'slug', 'description', 'count']


admin.site.register(wooShippingClass, wooShippingClassAdmin)


class wooStoreAdminForm(forms.ModelForm):

    class Meta:
        model = wooStore
        fields = '__all__'


class wooStoreAdmin(admin.ModelAdmin):
    form = wooStoreAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'code',
                    'base_url', 'consumer_secret', 'timezone', 'verify_ssl']
    readonly_fields = ['id', 'date_added', 'date_updated', ]
    search_fields = ['id', 'code', ]
    list_filter = (
        ('timezone', admin.RelatedOnlyFieldListFilter),
    )


admin.site.register(wooStore, wooStoreAdmin)


class wooTagAdminForm(forms.ModelForm):

    class Meta:
        model = wooTag
        fields = '__all__'


class wooTagAdmin(admin.ModelAdmin):
    form = wooTagAdminForm
    list_display = ['id', 'date_added', 'date_updated',
                    'is_active', 'wid', 'name', 'slug', 'description', 'count']
    readonly_fields = ['id', 'date_added', 'date_updated',
                       'is_active', 'wid', 'name', 'slug',
                       'description', 'count']


admin.site.register(wooTag, wooTagAdmin)


class wooTermAdminForm(forms.ModelForm):

    class Meta:
        model = wooTerm
        fields = '__all__'


class wooTermAdmin(admin.ModelAdmin):
    form = wooTermAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'wid', 'name',
                    'slug', 'menu_order', 'count', 'wr_tooltip', 'wr_label']
    readonly_fields = ['id', 'date_added', 'date_updated', 'wid',
                       'name', 'slug', 'menu_order', 'count', 'wr_tooltip',
                       'wr_label']


admin.site.register(wooTerm, wooTermAdmin)


class wooVariantAdminForm(forms.ModelForm):

    class Meta:
        model = wooVariant
        fields = '__all__'


class wooVariantAdmin(admin.ModelAdmin):
    form = wooVariantAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'is_active',
                    'wid', 'date_created',
                    'permalink', 'sku', 'price', 'dimension_length',
                    'dimension_width', 'dimension_height', 'weight']
    readonly_fields = ['id', 'date_added', 'date_updated', 'is_active',
                       'wid', 'date_created',
                       'permalink', 'sku', 'price', 'dimension_length',
                       'dimension_width', 'dimension_height', 'weight']


admin.site.register(wooVariant, wooVariantAdmin)


class wpMediaAdminForm(forms.ModelForm):

    class Meta:
        model = wpMedia
        fields = '__all__'


class wpMediaAdmin(admin.ModelAdmin):
    form = wpMediaAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'is_active',
                    'alt_text', 'width', 'height', 'file', 'author',
                    'mime_type', 'comment_status', 'wid',
                    'source_url', 'template', 'ping_status', 'caption',
                    'link', 'slug', 'modified', 'guid', 'description',
                    'modified_gmt', 'title', 'date_gmt', 'type']
    readonly_fields = ['id', 'date_added', 'date_updated', 'is_active',
                       'alt_text', 'width', 'height', 'file', 'author',
                       'mime_type', 'comment_status', 'wid',
                       'source_url', 'template', 'ping_status', 'caption',
                       'link', 'slug', 'modified', 'guid', 'description',
                       'modified_gmt', 'title', 'date_gmt', 'type']


admin.site.register(wpMedia, wpMediaAdmin)


class wpMediaSizeAdminForm(forms.ModelForm):

    class Meta:
        model = wpMediaSize
        fields = '__all__'


class wpMediaSizeAdmin(admin.ModelAdmin):
    form = wpMediaSizeAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'is_active',
                    'name', 'file', 'mime_type',
                    'width', 'height', 'source_url']
    readonly_fields = ['id', 'date_added', 'date_updated', 'is_active',
                       'name', 'file', 'mime_type',
                       'width', 'height', 'source_url']


admin.site.register(wpMediaSize, wpMediaSizeAdmin)


class pfCountryAdminForm(forms.ModelForm):

    class Meta:
        model = pfCountry
        fields = '__all__'


class pfCountryAdmin(admin.ModelAdmin):
    form = pfCountryAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'code', 'name']
    readonly_fields = ['id', 'date_added', 'date_updated', 'code', 'name']


admin.site.register(pfCountry, pfCountryAdmin)


class pfStateAdminForm(forms.ModelForm):

    class Meta:
        model = pfState
        fields = '__all__'


class pfStateAdmin(admin.ModelAdmin):
    form = pfStateAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'code', 'name']
    readonly_fields = ['id', 'date_added', 'date_updated', 'code', 'name']


admin.site.register(pfState, pfStateAdmin)


class pfSyncProductAdminForm(forms.ModelForm):

    class Meta:
        model = pfSyncProduct
        fields = '__all__'


class pfSyncProductAdmin(admin.ModelAdmin):
    form = pfSyncProductAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'pid', 'external_id',
                    'variants', 'synced']
    readonly_fields = ['id', 'date_added', 'date_updated',
                       'pid', 'external_id', 'variants', 'synced']


admin.site.register(pfSyncProduct, pfSyncProductAdmin)


class pfSyncVariantAdminForm(forms.ModelForm):

    class Meta:
        model = pfSyncVariant
        fields = '__all__'


class pfSyncVariantAdmin(admin.ModelAdmin):
    form = pfSyncVariantAdminForm
    list_display = ['id', 'date_added', 'date_updated',
                    'pid', 'external_id', 'synced']
    readonly_fields = ['id', 'date_added', 'date_updated',
                       'pid', 'external_id', 'synced']


admin.site.register(pfSyncVariant, pfSyncVariantAdmin)


class pfSyncItemOptionAdminForm(forms.ModelForm):

    class Meta:
        model = pfSyncItemOption
        fields = '__all__'


class pfSyncItemOptionAdmin(admin.ModelAdmin):
    form = pfSyncItemOptionAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'pid', 'value']
    readonly_fields = ['id', 'date_added', 'date_updated', 'pid', 'value']


admin.site.register(pfSyncItemOption, pfSyncItemOptionAdmin)


class pfCatalogColorAdminForm(forms.ModelForm):

    class Meta:
        model = pfCatalogColor
        fields = '__all__'


class pfCatalogColorAdmin(admin.ModelAdmin):
    form = pfCatalogColorAdminForm
    list_display = ['label', 'code', 'label_clean', 'hex_code', ]
    readonly_fields = ['label', 'hex_code', ]
    list_editable = ['code', 'label_clean', ]
    search_fields = ['label', 'code', 'label_clean', 'hex_code', ]


admin.site.register(pfCatalogColor, pfCatalogColorAdmin)


class pfCatalogSizeAdminForm(forms.ModelForm):

    class Meta:
        model = pfCatalogSize
        fields = '__all__'


class pfCatalogSizeAdmin(admin.ModelAdmin):
    form = pfCatalogSizeAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'code',
                    'label', 'label_clean', 'sort_group', 'sort_order']
    readonly_fields = ['id', 'date_added', 'date_updated', 'code',
                       'label', 'label_clean', 'sort_group', 'sort_order']


admin.site.register(pfCatalogSize, pfCatalogSizeAdmin)


class pfCatalogFileSpecAdminForm(forms.ModelForm):

    class Meta:
        model = pfCatalogFileSpec
        fields = '__all__'


class pfCatalogFileSpecAdmin(admin.ModelAdmin):
    form = pfCatalogFileSpecAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'name', 'note',
                    'width', 'height',
                    'width_in', 'height_in', 'ratio', 'colorsystem']
    readonly_fields = ['id', 'date_added', 'date_updated', 'name', 'note',
                       'width', 'height',
                       'width_in', 'height_in', 'ratio', 'colorsystem']


admin.site.register(pfCatalogFileSpec, pfCatalogFileSpecAdmin)


class pfCatalogFileTypeAdminForm(forms.ModelForm):

    class Meta:
        model = pfCatalogFileType
        fields = '__all__'


class pfCatalogFileTypeAdmin(admin.ModelAdmin):
    form = pfCatalogFileTypeAdminForm
    list_display = ['id', 'date_added', 'date_updated',
                    'pid', 'title', 'additional_price']
    readonly_fields = ['id', 'date_added', 'date_updated',
                       'pid', 'title', 'additional_price']


admin.site.register(pfCatalogFileType, pfCatalogFileTypeAdmin)


class pfCatalogOptionTypeAdminForm(forms.ModelForm):

    class Meta:
        model = pfCatalogOptionType
        fields = '__all__'


class pfCatalogOptionTypeAdmin(admin.ModelAdmin):
    form = pfCatalogOptionTypeAdminForm
    list_display = ['id', 'date_added', 'date_updated',
                    'pid', 'title', 'type', 'additional_price']
    readonly_fields = ['id', 'date_added', 'date_updated',
                       'pid', 'title', 'type', 'additional_price']


admin.site.register(pfCatalogOptionType, pfCatalogOptionTypeAdmin)


class pfCatalogProductAdminForm(forms.ModelForm):

    class Meta:
        model = pfCatalogProduct
        fields = '__all__'


class pfCatalogProductAdmin(admin.ModelAdmin):
    form = pfCatalogProductAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'is_active',
                    'pid', 'type', 'brand', 'model', 'image', 'variant_count']
    readonly_fields = ['id', 'date_added', 'date_updated', 'is_active',
                       'pid', 'type', 'brand', 'model',
                       'image', 'variant_count']


admin.site.register(pfCatalogProduct, pfCatalogProductAdmin)


class pfCatalogVariantAdminForm(forms.ModelForm):

    class Meta:
        model = pfCatalogVariant
        fields = '__all__'


class pfCatalogVariantAdmin(admin.ModelAdmin):
    form = pfCatalogVariantAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'is_active',
                    'pid', 'name', 'image', 'price', 'in_stock', 'weight']
    readonly_fields = ['id', 'date_added', 'date_updated', 'is_active',
                       'pid', 'name', 'image', 'price', 'in_stock', 'weight']


admin.site.register(pfCatalogVariant, pfCatalogVariantAdmin)


class pfStoreAdminForm(forms.ModelForm):

    class Meta:
        model = pfStore
        fields = '__all__'


class pfStoreAdmin(admin.ModelAdmin):
    form = pfStoreAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'code', 'name',
                    'website', 'created', 'key']
    readonly_fields = ['id', 'date_added', 'date_updated', 'code',
                       'name', 'website', 'created', 'key']


admin.site.register(pfStore, pfStoreAdmin)


class pfPrintFileAdminForm(forms.ModelForm):

    class Meta:
        model = pfPrintFile
        fields = '__all__'


class pfPrintFileAdmin(admin.ModelAdmin):
    form = pfPrintFileAdminForm
    list_display = ['id', 'date_added', 'date_updated', 'pid', 'type',
                    'hash', 'url', 'filename',
                    'mime_type', 'size', 'width', 'height', 'dpi',
                    'status', 'created', 'thumbnail_url', 'visible']
    readonly_fields = ['id', 'date_added', 'date_updated', 'pid',
                       'type', 'hash', 'url', 'filename',
                       'mime_type', 'size', 'width', 'height', 'dpi',
                       'status', 'created', 'thumbnail_url', 'visible']


admin.site.register(pfPrintFile, pfPrintFileAdmin)
