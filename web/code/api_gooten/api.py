from . import models
from . import serializers
from rest_framework import viewsets, permissions


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product class"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProductImage class"""

    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProductCategory class"""

    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the ImageType class"""

    queryset = models.ImageType.objects.all()
    serializer_class = serializers.ImageTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProductInfo class"""

    queryset = models.ProductInfo.objects.all()
    serializer_class = serializers.ProductInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContentTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the ContentType class"""

    queryset = models.ContentType.objects.all()
    serializer_class = serializers.ContentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class InfoContentViewSet(viewsets.ModelViewSet):
    """ViewSet for the InfoContent class"""

    queryset = models.InfoContent.objects.all()
    serializer_class = serializers.InfoContentSerializer
    permission_classes = [permissions.IsAuthenticated]


class VariantViewSet(viewsets.ModelViewSet):
    """ViewSet for the Variant class"""

    queryset = models.Variant.objects.all()
    serializer_class = serializers.VariantSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttributeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Attribute class"""

    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttributeValueViewSet(viewsets.ModelViewSet):
    """ViewSet for the AttributeValue class"""

    queryset = models.AttributeValue.objects.all()
    serializer_class = serializers.AttributeValueSerializer
    permission_classes = [permissions.IsAuthenticated]


class VariantOptionViewSet(viewsets.ModelViewSet):
    """ViewSet for the VariantOption class"""

    queryset = models.VariantOption.objects.all()
    serializer_class = serializers.VariantOptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class VariantTemplateViewSet(viewsets.ModelViewSet):
    """ViewSet for the VariantTemplate class"""

    queryset = models.VariantTemplate.objects.all()
    serializer_class = serializers.VariantTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]


class TemplateSpaceViewSet(viewsets.ModelViewSet):
    """ViewSet for the TemplateSpace class"""

    queryset = models.TemplateSpace.objects.all()
    serializer_class = serializers.TemplateSpaceSerializer
    permission_classes = [permissions.IsAuthenticated]


class LayerTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the LayerType class"""

    queryset = models.LayerType.objects.all()
    serializer_class = serializers.LayerTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpaceLayerViewSet(viewsets.ModelViewSet):
    """ViewSet for the SpaceLayer class"""

    queryset = models.SpaceLayer.objects.all()
    serializer_class = serializers.SpaceLayerSerializer
    permission_classes = [permissions.IsAuthenticated]
