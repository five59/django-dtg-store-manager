from business import models

from rest_framework import serializers


class bzBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bzBrand
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'name',
        )


class bzCreativeCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bzCreativeCollection
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'name',
        )


class bzCreativeDesignSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bzCreativeDesign
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'name',
        )


class bzCreativeLayoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bzCreativeLayout
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'name',
        )


class bzCreativeRenderingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bzCreativeRendering
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
        )


class bzProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bzProduct
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'name',
            'status',
        )


class bzProductVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bzProductVariant
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'is_active',
        )


class wooAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooAttribute
        fields = (
            'slug',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'wid',
            'name',
            'type',
            'has_archives',
        )


class wooCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooCategory
        fields = (
            'slug',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'wid',
            'name',
            'parent',
            'description',
            'display',
            'count',
            'image_id',
            'image_date_created',
        )


class wooImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooImage
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'wid',
            'date_created',
            'alt',
            'position',
        )


class wooProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooProduct
        fields = (
            'slug',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'wid',
            'permalink',
            'date_created',
            'dimension_length',
            'dimension_width',
            'dimension_height',
            'weight',
            'reviews_allowed',
        )


class wooShippingClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooShippingClass
        fields = (
            'slug',
            'id',
            'wid',
            'name',
            'description',
            'count',
        )


class wooStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooStore
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'base_url',
            'consumer_secret',
            'timezone',
            'verify_ssl',
        )


class wooTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooTag
        fields = (
            'slug',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'wid',
            'name',
            'description',
            'count',
        )


class wooTermSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooTerm
        fields = (
            'slug',
            'id',
            'date_added',
            'date_updated',
            'wid',
            'name',
            'menu_order',
            'count',
            'wr_tooltip',
            'wr_label',
        )


class wooVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wooVariant
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'wid',
            'date_created',
            'permalink',
            'sku',
            'price',
            'dimension_length',
            'dimension_width',
            'dimension_height',
            'weight',
        )


class wpMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wpMedia
        fields = (
            'slug',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'alt_text',
            'width',
            'height',
            'file',
            'author',
            'mime_type',
            'comment_status',
            'wid',
            'source_url',
            'template',
            'ping_status',
            'caption',
            'link',
            'modified',
            'guid',
            'description',
            'modified_gmt',
            'title',
            'date_gmt',
            'type',
        )


class wpMediaSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.wpMediaSize
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'name',
            'file',
            'mime_type',
            'width',
            'height',
            'source_url',
        )


class pfCountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfCountry
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'name',
        )


class pfStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfState
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'name',
        )


class pfSyncProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfSyncProduct
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'pid',
            'external_id',
            'variants',
            'synced',
        )


class pfSyncVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfSyncVariant
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'pid',
            'external_id',
            'synced',
        )


class pfSyncItemOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfSyncItemOption
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'pid',
            'value',
        )


class pfCatalogColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfCatalogColor
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'label',
            'label_clean',
            'hex_code',
        )


class pfCatalogSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfCatalogSize
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'label',
            'label_clean',
            'sort_group',
            'sort_order',
        )


class pfCatalogFileSpecSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfCatalogFileSpec
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'name',
            'note',
            'width',
            'height',
            'width_in',
            'height_in',
            'ratio',
            'colorsystem',
        )


class pfCatalogFileTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfCatalogFileType
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'pid',
            'title',
            'additional_price',
        )


class pfCatalogOptionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfCatalogOptionType
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'pid',
            'title',
            'type',
            'additional_price',
        )


class pfCatalogProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfCatalogProduct
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'pid',
            'type',
            'brand',
            'model',
            'image',
            'variant_count',
        )


class pfCatalogVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfCatalogVariant
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'is_active',
            'pid',
            'name',
            'image',
            'price',
            'in_stock',
            'weight',
        )


class pfStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfStore
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'code',
            'name',
            'website',
            'created',
            'consumer_key',
            'consumer_secret',
        )


class pfPrintFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pfPrintFile
        fields = (
            'pk',
            'id',
            'date_added',
            'date_updated',
            'pid',
            'type',
            'hash',
            'url',
            'filename',
            'mime_type',
            'size',
            'width',
            'height',
            'dpi',
            'status',
            'created',
            'thumbnail_url',
            'visible',
        )
