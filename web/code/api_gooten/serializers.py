from . import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'is_active',
            'id',
            'uid',
            'name',
            'is_featured',
            'is_coming_soon',
            'has_available_product_variants',
            'has_product_templates',
            'description',
            'max_zoom',
            'priceinfo_price',
            'priceinfo_currencycode',
            'priceinfo_currencydigits',
            'priceinfo_currencyformat',
            'priceinfo_formattedprice',
            'retailprice_currencycode',
            'retailprice_currencydigits',
            'retailprice_currencyformat',
            'retailprice_formattedprice',
        )


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductImage
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'id',
            'index',
            'url',
            'is_active',
            'image_height',
        )


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductCategory
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'id',
            'name',
        )


class ImageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ImageType
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'name',
        )


class ProductInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductInfo
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'info_key',
            'index',
        )


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContentType
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'name',
        )


class InfoContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InfoContent
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'text',
        )


class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Variant
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'is_active',
            'sku',
            'has_templates',
            'max_images',
            'priceinfo_price',
            'priceinfo_currencycode',
            'priceinfo_currencydigits',
            'priceinfo_currencyformat',
            'priceinfo_formattedprice',
        )


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Attribute
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'option_id',
            'name',
        )


class AttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AttributeValue
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'value',
            'value_id',
            'sort_value',
            'image_type',
            'image_url',
            'image_height',
        )


class VariantOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VariantOption
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
        )


class VariantTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VariantTemplate
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'name',
            'is_default',
            'image_url',
            'image_height',
        )


class TemplateSpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TemplateSpace
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'id',
            'index',
        )


class LayerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LayerType
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'name',
        )


class SpaceLayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SpaceLayer
        fields = (
            'slug',
            'pkid',
            'created',
            'last_updated',
            'include_in_print',
            'x1',
            'x2',
            'y1',
            'y2',
            'zIndex',
        )
