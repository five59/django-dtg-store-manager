from django.contrib import admin
from django import forms
from .models import Product, ProductImage, ProductCategory, ImageType, ProductInfo, ContentType, InfoContent, Variant, VariantOption, VariantTemplate, TemplateSpace, LayerType, SpaceLayer


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 0
    fields = ['sku', 'priceinfo_price', 'has_templates', 'is_active', 'max_images', ]
    readonly_fields = ('sku', 'priceinfo_price',
                       'has_templates', 'is_active', 'max_images',)
    can_delete = False


class VariantOptionInline(admin.TabularInline):
    model = VariantOption
    extra = 0
    fields = ('image_thumb', 'name', 'value',)
    readonly_fields = fields
    can_delete = False


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['id', 'name',
                    'is_featured', 'is_coming_soon',
                    'has_available_product_variants', 'has_product_templates',
                    'priceinfo_formattedprice']
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'id', 'uid', 'name', 'is_featured', 'is_coming_soon', 'has_available_product_variants', 'has_product_templates', 'description', 'max_zoom', 'priceinfo_price', 'priceinfo_currencycode',
                       'priceinfo_currencydigits', 'priceinfo_currencyformat', 'priceinfo_formattedprice', 'retailprice_price', 'retailprice_currencycode', 'retailprice_currencydigits', 'retailprice_currencyformat', 'retailprice_formattedprice']
    list_filter = ['is_featured', 'is_coming_soon',
                   'has_available_product_variants', 'has_product_templates', ]
    inlines = [VariantInline, ]
admin.site.register(Product, ProductAdmin)


class ProductImageAdminForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductImageAdmin(admin.ModelAdmin):
    form = ProductImageAdminForm
    list_display = ['id', 'index', 'has_image', 'url']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'id', 'index', 'url']

admin.site.register(ProductImage, ProductImageAdmin)


class ProductCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductCategoryAdmin(admin.ModelAdmin):
    form = ProductCategoryAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'id', 'name']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'id', 'name']

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ImageTypeAdminForm(forms.ModelForm):

    class Meta:
        model = ImageType
        fields = '__all__'


class ImageTypeAdmin(admin.ModelAdmin):
    form = ImageTypeAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'name']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'name']

admin.site.register(ImageType, ImageTypeAdmin)


class ProductInfoAdminForm(forms.ModelForm):

    class Meta:
        model = ProductInfo
        fields = '__all__'


class ProductInfoAdmin(admin.ModelAdmin):
    form = ProductInfoAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'info_key', 'index']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'info_key', 'index']

admin.site.register(ProductInfo, ProductInfoAdmin)


class ContentTypeAdminForm(forms.ModelForm):

    class Meta:
        model = ContentType
        fields = '__all__'


class ContentTypeAdmin(admin.ModelAdmin):
    form = ContentTypeAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'name']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'name']

admin.site.register(ContentType, ContentTypeAdmin)


class InfoContentAdminForm(forms.ModelForm):

    class Meta:
        model = InfoContent
        fields = '__all__'


class InfoContentAdmin(admin.ModelAdmin):
    form = InfoContentAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'text']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'text']

admin.site.register(InfoContent, InfoContentAdmin)


class VariantAdminForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = '__all__'


class VariantAdmin(admin.ModelAdmin):
    form = VariantAdminForm
    list_display = [
        # 'pkid', 'slug', 'created', 'last_updated',
        'sku', 'has_templates', 'max_images', 'priceinfo_price', ]
    # 'priceinfo_currencycode', 'priceinfo_currencydigits', 'priceinfo_currencyformat', 'priceinfo_formattedprice']
    readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'sku', 'has_templates', 'max_images', 'priceinfo_price',
                       'priceinfo_currencycode', 'priceinfo_currencydigits', 'priceinfo_currencyformat', 'priceinfo_formattedprice']
    inlines = (VariantOptionInline, )
admin.site.register(Variant, VariantAdmin)


class VariantOptionAdminForm(forms.ModelForm):

    class Meta:
        model = VariantOption
        fields = '__all__'


class VariantOptionAdmin(admin.ModelAdmin):
    form = VariantOptionAdminForm
    list_display = ['variant', 'name', 'has_image',
                    'value', 'image_type', 'image_url', 'sort_value', ]
    list_filter = ['variant', 'name', 'image_type', ]
    # list_display = ['pkid', 'slug', 'created', 'last_updated', 'option_id',
    #                 'name', 'sort_value', 'value', 'value_id', 'image_type', 'image_url']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'option_id', 'name', 'sort_value', 'value', 'value_id', 'image_type', 'image_url']

admin.site.register(VariantOption, VariantOptionAdmin)


class VariantTemplateAdminForm(forms.ModelForm):

    class Meta:
        model = VariantTemplate
        fields = '__all__'


class VariantTemplateAdmin(admin.ModelAdmin):
    form = VariantTemplateAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'name', 'is_default', 'image_url']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'name', 'is_default', 'image_url']

admin.site.register(VariantTemplate, VariantTemplateAdmin)


class TemplateSpaceAdminForm(forms.ModelForm):

    class Meta:
        model = TemplateSpace
        fields = '__all__'


class TemplateSpaceAdmin(admin.ModelAdmin):
    form = TemplateSpaceAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'id', 'index']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'id', 'index']

admin.site.register(TemplateSpace, TemplateSpaceAdmin)


class LayerTypeAdminForm(forms.ModelForm):

    class Meta:
        model = LayerType
        fields = '__all__'


class LayerTypeAdmin(admin.ModelAdmin):
    form = LayerTypeAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated', 'name']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'name']

admin.site.register(LayerType, LayerTypeAdmin)


class SpaceLayerAdminForm(forms.ModelForm):

    class Meta:
        model = SpaceLayer
        fields = '__all__'


class SpaceLayerAdmin(admin.ModelAdmin):
    form = SpaceLayerAdminForm
    list_display = ['pkid', 'slug', 'created', 'last_updated',
                    'include_in_print', 'x1', 'x2', 'y1', 'y2', 'zIndex']
    # readonly_fields = ['pkid', 'slug', 'created', 'last_updated', 'include_in_print', 'x1', 'x2', 'y1', 'y2', 'zIndex']

admin.site.register(SpaceLayer, SpaceLayerAdmin)
