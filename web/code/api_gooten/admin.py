from django.contrib import admin
from django import forms
from .models import Product, ProductImage, ProductCategory, ImageType, ProductInfo, ContentType, InfoContent, Variant, Attribute, AttributeValue, VariantOption, VariantTemplate, TemplateSpace, LayerType, SpaceLayer
from django.utils.translation import ugettext_lazy as _

# Inlines


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 0
    fields = ['sku', 'priceinfo_price', 'has_templates', 'is_active', 'max_images', ]
    readonly_fields = ('sku', 'priceinfo_price',
                       'has_templates', 'is_active', 'max_images',)
    can_delete = False
    show_change_link = True
    suit_classes = 'suit-tab suit-tab-Variant'


class VariantOptionsInline(admin.TabularInline):
    model = VariantOption
    extra = 0
    fields = ('get_sort_value', 'get_image_thumb', 'get_attribute', 'value',)
    readonly_fields = fields
    can_delete = False
    show_change_link = True
    suit_classes = 'suit-tab suit-tab-VariantOptions'


class VariantTemplateInline(admin.TabularInline):
    model = VariantTemplate
    extra = 0
    fields = ('name', 'is_default',)
    readonly_fields = fields
    can_delete = False
    show_change_link = True
    suit_classes = 'suit-tab suit-tab-VariantTemplate'


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 0
    fields = (
        'sort_value',
        'value',
        'image_type',
    )
    readonly_fields = fields
    can_delete = False


# Forms and Admins


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = (
        'name',
        'priceinfo_price',
        'is_active',
        'is_featured',
        'is_coming_soon',
        'has_available_product_variants',
    )
    readonly_fields = ('pkid', 'slug', 'created', 'last_updated', 'is_active', 'id', 'uid', 'name', 'is_featured', 'is_coming_soon',
                       'has_available_product_variants', 'has_product_templates', 'description', 'max_zoom', 'priceinfo_price',
                       'priceinfo_currencycode', 'priceinfo_currencydigits', 'priceinfo_currencyformat', 'priceinfo_formattedprice',
                       'retailprice_price', 'retailprice_currencycode', 'retailprice_currencydigits', 'retailprice_currencyformat', 'retailprice_formattedprice')
    list_filter = ('is_featured', 'is_coming_soon', 'has_available_product_variants',)
    inlines = (VariantInline, )

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['name', 'description', ]
        }),
        ("Info", {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['id', 'uid', 'max_zoom', ],
        }),
        ("Flags", {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['is_active', 'is_featured', 'is_coming_soon',
                       'has_available_product_variants', 'has_product_templates', ]
        }),
        ("Cost", {
            'classes': ('suit-tab', 'suit-tab-money',),
            'fields': ['priceinfo_price',
                       'priceinfo_currencycode', 'priceinfo_currencydigits', 'priceinfo_currencyformat', 'priceinfo_formattedprice', ]
        }),
        ("Retail", {
            'classes': ('suit-tab', 'suit-tab-money',),
            'fields': ['retailprice_price', 'retailprice_currencycode', 'retailprice_currencydigits', 'retailprice_currencyformat', 'retailprice_formattedprice']
        }),

        (None, {
            'classes': ('suit-tab', 'suit-tab-meta',),
            'fields': ['pkid', 'slug', 'created', 'last_updated', ]
        }),

    ]
    suit_form_tabs = (
        ('info', _('Info')),
        ('money', _("Money")),
        ('Variant', _("Variants")),
        ('meta', _("Metadata")),
    )


admin.site.register(Product, ProductAdmin)


class ProductImageAdminForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductImageAdmin(admin.ModelAdmin):
    form = ProductImageAdminForm
    list_display = ('index', 'url', 'is_active', 'has_image', 'image_thumb', 'get_product',)
    list_filter = (
        'is_active',
        ('product', admin.RelatedOnlyFieldListFilter),
    )
    readonly_fields = ('pkid', 'slug', 'created', 'last_updated',
                       'id', 'index', 'url', 'is_active', 'image_height',)
admin.site.register(ProductImage, ProductImageAdmin)


class ProductCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductCategoryAdmin(admin.ModelAdmin):
    form = ProductCategoryAdminForm
    list_display = ('id', 'name',)
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'id', 'name']
admin.site.register(ProductCategory, ProductCategoryAdmin)


class ImageTypeAdminForm(forms.ModelForm):

    class Meta:
        model = ImageType
        fields = '__all__'


class ImageTypeAdmin(admin.ModelAdmin):
    form = ImageTypeAdminForm
    list_display = ('name', 'friendly_name')
    readonly_fields = ('pkid', 'slug', 'created', 'last_updated', 'name',)
admin.site.register(ImageType, ImageTypeAdmin)


class ProductInfoAdminForm(forms.ModelForm):

    class Meta:
        model = ProductInfo
        fields = '__all__'


class ProductInfoAdmin(admin.ModelAdmin):
    form = ProductInfoAdminForm
    list_display = ('index', 'get_product', 'info_key', 'get_content_type',  'get_text',)
    list_filter = ('product', 'content_type',)
    readonly_fields = ('pkid', 'slug', 'created', 'last_updated', 'info_key', 'index',)
admin.site.register(ProductInfo, ProductInfoAdmin)


class ContentTypeAdminForm(forms.ModelForm):

    class Meta:
        model = ContentType
        fields = '__all__'


class ContentTypeAdmin(admin.ModelAdmin):
    form = ContentTypeAdminForm
    list_display = ('name',)
    readonly_fields = ('pkid', 'slug', 'created', 'last_updated', 'name',)
admin.site.register(ContentType, ContentTypeAdmin)


class InfoContentAdminForm(forms.ModelForm):

    class Meta:
        model = InfoContent
        fields = '__all__'


class InfoContentAdmin(admin.ModelAdmin):
    form = InfoContentAdminForm
    list_display = ('text',)
    readonly_fields = ('pkid', 'slug', 'created', 'last_updated', 'text')
admin.site.register(InfoContent, InfoContentAdmin)


class VariantAdminForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = '__all__'


class VariantAdmin(admin.ModelAdmin):
    form = VariantAdminForm
    list_display = (
        # 'sku',
        'friendly_name',
        'get_product',
        'c_brand',
        'c_item',
        'c_color',
        'c_size',
        'priceinfo_price',
        'is_active',
        'has_templates',
        'max_images',
        'num_options',
        'num_templates',
    )
    list_editable = ('c_item',)
    readonly_fields = ('pkid', 'slug', 'created', 'last_updated', 'is_active', 'sku', 'has_templates', 'max_images',
                       'priceinfo_price', 'priceinfo_currencycode', 'priceinfo_currencydigits', 'priceinfo_currencyformat',
                       'priceinfo_formattedprice', 'num_options', 'num_templates', 'get_product',)
    inlines = (VariantOptionsInline, VariantTemplateInline,)
    list_filter = (
        'is_active',
        'has_templates',
        ('product', admin.RelatedOnlyFieldListFilter),
        ('c_brand', admin.RelatedOnlyFieldListFilter),
        ('c_item', admin.RelatedOnlyFieldListFilter),
        ('c_color', admin.RelatedOnlyFieldListFilter),
        ('c_size', admin.RelatedOnlyFieldListFilter),

    )
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['c_brand', 'c_item', 'c_color', 'c_size', 'get_product', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['sku', 'has_templates', 'max_images', 'num_options', 'num_templates', ]
        }),
        ("Price Info", {
            'classes': ('suit-tab', 'suit-tab-money',),
            'fields': ['priceinfo_price', 'priceinfo_currencycode', 'priceinfo_currencydigits',
                       'priceinfo_currencyformat', 'priceinfo_formattedprice', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-meta',),
            'fields': ['pkid', 'slug', 'created', 'last_updated', 'is_active', ]
        }),

    ]
    suit_form_tabs = (
        ('info', _('Info')),
        ('money', _("Money")),
        ('VariantOptions', _("Options")),
        ('VariantTemplate', _("Templates")),
        ('meta', _("Metadata")),
    )


admin.site.register(Variant, VariantAdmin)


class AttributeAdminForm(forms.ModelForm):

    class Meta:
        model = Attribute
        fields = '__all__'


class AttributeAdmin(admin.ModelAdmin):
    form = AttributeAdminForm
    list_display = ('name', 'grouping', 'get_num_values', )
    list_filter = ('grouping', )
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'option_id', 'name']
    inlines = (AttributeValueInline,)
admin.site.register(Attribute, AttributeAdmin)


class AttributeValueAdminForm(forms.ModelForm):

    class Meta:
        model = AttributeValue
        fields = '__all__'


class AttributeValueAdmin(admin.ModelAdmin):
    form = AttributeValueAdminForm
    list_display = ('sort_value', 'image_thumb', 'get_attribute', 'value',)
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'value',
                       'value_id', 'sort_value', 'image_type', 'image_url', 'image_height', 'image_width', ]
    list_filter = ('attribute',)
admin.site.register(AttributeValue, AttributeValueAdmin)


class VariantOptionAdminForm(forms.ModelForm):

    class Meta:
        model = VariantOption
        fields = '__all__'


class VariantOptionAdmin(admin.ModelAdmin):
    form = VariantOptionAdminForm
    list_display = ('get_sort_value', 'get_attribute', 'get_value',)
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated']
admin.site.register(VariantOption, VariantOptionAdmin)


class VariantTemplateAdminForm(forms.ModelForm):

    class Meta:
        model = VariantTemplate
        fields = '__all__'


class VariantTemplateAdmin(admin.ModelAdmin):
    form = VariantTemplateAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated',
                    'name', 'is_default', 'image_url', 'image_height']
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated',
                       'name', 'is_default', 'image_url', 'image_height']
    list_filter = ('variant',)
admin.site.register(VariantTemplate, VariantTemplateAdmin)


class TemplateSpaceAdminForm(forms.ModelForm):

    class Meta:
        model = TemplateSpace
        fields = '__all__'


class TemplateSpaceAdmin(admin.ModelAdmin):
    form = TemplateSpaceAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'id', 'index']
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'id', 'index']

admin.site.register(TemplateSpace, TemplateSpaceAdmin)


class LayerTypeAdminForm(forms.ModelForm):

    class Meta:
        model = LayerType
        fields = '__all__'


class LayerTypeAdmin(admin.ModelAdmin):
    form = LayerTypeAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'name']
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'name']

admin.site.register(LayerType, LayerTypeAdmin)


class SpaceLayerAdminForm(forms.ModelForm):

    class Meta:
        model = SpaceLayer
        fields = '__all__'


class SpaceLayerAdmin(admin.ModelAdmin):
    form = SpaceLayerAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated',
                    'include_in_print', 'x1', 'x2', 'y1', 'y2', 'zIndex']
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated',
                       'include_in_print', 'x1', 'x2', 'y1', 'y2', 'zIndex']

admin.site.register(SpaceLayer, SpaceLayerAdmin)
