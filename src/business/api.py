from business import models
from business import serializers
from rest_framework import viewsets, permissions


class bzBrandViewSet(viewsets.ModelViewSet):
    """ViewSet for the bzBrand class"""

    queryset = models.bzBrand.objects.all()
    serializer_class = serializers.bzBrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class bzCreativeCollectionViewSet(viewsets.ModelViewSet):
    """ViewSet for the bzCreativeCollection class"""

    queryset = models.bzCreativeCollection.objects.all()
    serializer_class = serializers.bzCreativeCollectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class bzCreativeDesignViewSet(viewsets.ModelViewSet):
    """ViewSet for the bzCreativeDesign class"""

    queryset = models.bzCreativeDesign.objects.all()
    serializer_class = serializers.bzCreativeDesignSerializer
    permission_classes = [permissions.IsAuthenticated]


class bzCreativeLayoutViewSet(viewsets.ModelViewSet):
    """ViewSet for the bzCreativeLayout class"""

    queryset = models.bzCreativeLayout.objects.all()
    serializer_class = serializers.bzCreativeLayoutSerializer
    permission_classes = [permissions.IsAuthenticated]


class bzCreativeRenderingViewSet(viewsets.ModelViewSet):
    """ViewSet for the bzCreativeRendering class"""

    queryset = models.bzCreativeRendering.objects.all()
    serializer_class = serializers.bzCreativeRenderingSerializer
    permission_classes = [permissions.IsAuthenticated]


class bzProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the bzProduct class"""

    queryset = models.bzProduct.objects.all()
    serializer_class = serializers.bzProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class bzProductVariantViewSet(viewsets.ModelViewSet):
    """ViewSet for the bzProductVariant class"""

    queryset = models.bzProductVariant.objects.all()
    serializer_class = serializers.bzProductVariantSerializer
    permission_classes = [permissions.IsAuthenticated]


class wooAttributeViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooAttribute class"""

    queryset = models.wooAttribute.objects.all()
    serializer_class = serializers.wooAttributeSerializer
    permission_classes = [permissions.IsAuthenticated]


class wooCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooCategory class"""

    queryset = models.wooCategory.objects.all()
    serializer_class = serializers.wooCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class wooImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooImage class"""

    queryset = models.wooImage.objects.all()
    serializer_class = serializers.wooImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class wooProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooProduct class"""

    queryset = models.wooProduct.objects.all()
    serializer_class = serializers.wooProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class wooShippingClassViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooShippingClass class"""

    queryset = models.wooShippingClass.objects.all()
    serializer_class = serializers.wooShippingClassSerializer
    permission_classes = [permissions.IsAuthenticated]


class wooStoreViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooStore class"""

    queryset = models.wooStore.objects.all()
    serializer_class = serializers.wooStoreSerializer
    permission_classes = [permissions.IsAuthenticated]


class wooTagViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooTag class"""

    queryset = models.wooTag.objects.all()
    serializer_class = serializers.wooTagSerializer
    permission_classes = [permissions.IsAuthenticated]


class wooTermViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooTerm class"""

    queryset = models.wooTerm.objects.all()
    serializer_class = serializers.wooTermSerializer
    permission_classes = [permissions.IsAuthenticated]


class wooVariantViewSet(viewsets.ModelViewSet):
    """ViewSet for the wooVariant class"""

    queryset = models.wooVariant.objects.all()
    serializer_class = serializers.wooVariantSerializer
    permission_classes = [permissions.IsAuthenticated]


class wpMediaViewSet(viewsets.ModelViewSet):
    """ViewSet for the wpMedia class"""

    queryset = models.wpMedia.objects.all()
    serializer_class = serializers.wpMediaSerializer
    permission_classes = [permissions.IsAuthenticated]


class wpMediaSizeViewSet(viewsets.ModelViewSet):
    """ViewSet for the wpMediaSize class"""

    queryset = models.wpMediaSize.objects.all()
    serializer_class = serializers.wpMediaSizeSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfCountryViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfCountry class"""

    queryset = models.pfCountry.objects.all()
    serializer_class = serializers.pfCountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class pfStateViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfState class"""

    queryset = models.pfState.objects.all()
    serializer_class = serializers.pfStateSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfSyncProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfSyncProduct class"""

    queryset = models.pfSyncProduct.objects.all()
    serializer_class = serializers.pfSyncProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfSyncVariantViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfSyncVariant class"""

    queryset = models.pfSyncVariant.objects.all()
    serializer_class = serializers.pfSyncVariantSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfSyncItemOptionViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfSyncItemOption class"""

    queryset = models.pfSyncItemOption.objects.all()
    serializer_class = serializers.pfSyncItemOptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfCatalogColorViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfCatalogColor class"""

    queryset = models.pfCatalogColor.objects.all()
    serializer_class = serializers.pfCatalogColorSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfCatalogSizeViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfCatalogSize class"""

    queryset = models.pfCatalogSize.objects.all()
    serializer_class = serializers.pfCatalogSizeSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfCatalogFileSpecViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfCatalogFileSpec class"""

    queryset = models.pfCatalogFileSpec.objects.all()
    serializer_class = serializers.pfCatalogFileSpecSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfCatalogFileTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfCatalogFileType class"""

    queryset = models.pfCatalogFileType.objects.all()
    serializer_class = serializers.pfCatalogFileTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfCatalogOptionTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfCatalogOptionType class"""

    queryset = models.pfCatalogOptionType.objects.all()
    serializer_class = serializers.pfCatalogOptionTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfCatalogProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfCatalogProduct class"""

    queryset = models.pfCatalogProduct.objects.all()
    serializer_class = serializers.pfCatalogProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfCatalogVariantViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfCatalogVariant class"""

    queryset = models.pfCatalogVariant.objects.all()
    serializer_class = serializers.pfCatalogVariantSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfStoreViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfStore class"""

    queryset = models.pfStore.objects.all()
    serializer_class = serializers.pfStoreSerializer
    permission_classes = [permissions.IsAuthenticated]


class pfPrintFileViewSet(viewsets.ModelViewSet):
    """ViewSet for the pfPrintFile class"""

    queryset = models.pfPrintFile.objects.all()
    serializer_class = serializers.pfPrintFileSerializer
    permission_classes = [permissions.IsAuthenticated]
