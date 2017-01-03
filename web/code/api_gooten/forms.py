from django import forms
from .models import Product, ProductImage, ProductCategory, ImageType, ProductInfo, ContentType, InfoContent, Variant, Attribute, AttributeValue, VariantOption, VariantTemplate, TemplateSpace, LayerType, SpaceLayer


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'is_active',
            'id',
            'uid',
            'name',
            'is_featured',
            'is_coming_soon',
            'has_available_product_variants', 'has_product_templates', 'description', 'max_zoom', 'priceinfo_price', 'priceinfo_currencycode',
            'priceinfo_currencydigits', 'priceinfo_currencyformat', 'priceinfo_formattedprice', 'retailprice_currencycode', 'retailprice_currencydigits', 'retailprice_currencyformat', 'retailprice_formattedprice', 'categories']


class ProductImageForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        fields = [
            'id', 'index', 'url', 'is_active',
                  'image_height', 'product', 'imagetypes']


class ProductCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ImageTypeForm(forms.ModelForm):

    class Meta:
        model = ImageType
        fields = ['name']


class ProductInfoForm(forms.ModelForm):

    class Meta:
        model = ProductInfo
        fields = ['info_key', 'index', 'product', 'content_type']


class ContentTypeForm(forms.ModelForm):

    class Meta:
        model = ContentType
        fields = ['name']


class InfoContentForm(forms.ModelForm):

    class Meta:
        model = InfoContent
        fields = ['text', 'productinfo']


class VariantForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = ['is_active', 'sku', 'has_templates', 'max_images', 'priceinfo_price', 'priceinfo_currencycode',
                  'priceinfo_currencydigits', 'priceinfo_currencyformat', 'priceinfo_formattedprice', 'product']


class AttributeForm(forms.ModelForm):

    class Meta:
        model = Attribute
        fields = ['option_id', 'name']


class AttributeValueForm(forms.ModelForm):

    class Meta:
        model = AttributeValue
        fields = ['value', 'value_id', 'sort_value',
                  'image_type', 'image_url', 'image_height', 'attribute']


class VariantOptionForm(forms.ModelForm):

    class Meta:
        model = VariantOption
        fields = ['value', 'variant']


class VariantTemplateForm(forms.ModelForm):

    class Meta:
        model = VariantTemplate
        fields = ['name', 'is_default', 'image_url', 'image_height', 'variant']


class TemplateSpaceForm(forms.ModelForm):

    class Meta:
        model = TemplateSpace
        fields = ['id', 'index', 'variant_template']


class LayerTypeForm(forms.ModelForm):

    class Meta:
        model = LayerType
        fields = ['name']


class SpaceLayerForm(forms.ModelForm):

    class Meta:
        model = SpaceLayer
        fields = ['include_in_print', 'x1', 'x2', 'y1',
                  'y2', 'zIndex', 'templatespace', 'layer_type']
