from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'product', api.ProductViewSet)
router.register(r'productimage', api.ProductImageViewSet)
router.register(r'productcategory', api.ProductCategoryViewSet)
router.register(r'imagetype', api.ImageTypeViewSet)
router.register(r'productinfo', api.ProductInfoViewSet)
router.register(r'contenttype', api.ContentTypeViewSet)
router.register(r'infocontent', api.InfoContentViewSet)
router.register(r'variant', api.VariantViewSet)
router.register(r'attribute', api.AttributeViewSet)
router.register(r'attributevalue', api.AttributeValueViewSet)
router.register(r'variantoption', api.VariantOptionViewSet)
router.register(r'varianttemplate', api.VariantTemplateViewSet)
router.register(r'templatespace', api.TemplateSpaceViewSet)
router.register(r'layertype', api.LayerTypeViewSet)
router.register(r'spacelayer', api.SpaceLayerViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Product
    url(r'^api_gooten/product/$', views.ProductListView.as_view(), name='api_gooten_product_list'),
    url(r'^api_gooten/product/create/$', views.ProductCreateView.as_view(),
        name='api_gooten_product_create'),
    url(r'^api_gooten/product/detail/(?P<slug>\S+)/$',
        views.ProductDetailView.as_view(), name='api_gooten_product_detail'),
    url(r'^api_gooten/product/update/(?P<slug>\S+)/$',
        views.ProductUpdateView.as_view(), name='api_gooten_product_update'),
)

urlpatterns += (
    # urls for ProductImage
    url(r'^api_gooten/productimage/$', views.ProductImageListView.as_view(),
        name='api_gooten_productimage_list'),
    url(r'^api_gooten/productimage/create/$', views.ProductImageCreateView.as_view(),
        name='api_gooten_productimage_create'),
    url(r'^api_gooten/productimage/detail/(?P<slug>\S+)/$',
        views.ProductImageDetailView.as_view(), name='api_gooten_productimage_detail'),
    url(r'^api_gooten/productimage/update/(?P<slug>\S+)/$',
        views.ProductImageUpdateView.as_view(), name='api_gooten_productimage_update'),
)

urlpatterns += (
    # urls for ProductCategory
    url(r'^api_gooten/productcategory/$', views.ProductCategoryListView.as_view(),
        name='api_gooten_productcategory_list'),
    url(r'^api_gooten/productcategory/create/$', views.ProductCategoryCreateView.as_view(),
        name='api_gooten_productcategory_create'),
    url(r'^api_gooten/productcategory/detail/(?P<slug>\S+)/$',
        views.ProductCategoryDetailView.as_view(), name='api_gooten_productcategory_detail'),
    url(r'^api_gooten/productcategory/update/(?P<slug>\S+)/$',
        views.ProductCategoryUpdateView.as_view(), name='api_gooten_productcategory_update'),
)

urlpatterns += (
    # urls for ImageType
    url(r'^api_gooten/imagetype/$', views.ImageTypeListView.as_view(), name='api_gooten_imagetype_list'),
    url(r'^api_gooten/imagetype/create/$', views.ImageTypeCreateView.as_view(),
        name='api_gooten_imagetype_create'),
    url(r'^api_gooten/imagetype/detail/(?P<slug>\S+)/$',
        views.ImageTypeDetailView.as_view(), name='api_gooten_imagetype_detail'),
    url(r'^api_gooten/imagetype/update/(?P<slug>\S+)/$',
        views.ImageTypeUpdateView.as_view(), name='api_gooten_imagetype_update'),
)

urlpatterns += (
    # urls for ProductInfo
    url(r'^api_gooten/productinfo/$', views.ProductInfoListView.as_view(),
        name='api_gooten_productinfo_list'),
    url(r'^api_gooten/productinfo/create/$', views.ProductInfoCreateView.as_view(),
        name='api_gooten_productinfo_create'),
    url(r'^api_gooten/productinfo/detail/(?P<slug>\S+)/$',
        views.ProductInfoDetailView.as_view(), name='api_gooten_productinfo_detail'),
    url(r'^api_gooten/productinfo/update/(?P<slug>\S+)/$',
        views.ProductInfoUpdateView.as_view(), name='api_gooten_productinfo_update'),
)

urlpatterns += (
    # urls for ContentType
    url(r'^api_gooten/contenttype/$', views.ContentTypeListView.as_view(),
        name='api_gooten_contenttype_list'),
    url(r'^api_gooten/contenttype/create/$', views.ContentTypeCreateView.as_view(),
        name='api_gooten_contenttype_create'),
    url(r'^api_gooten/contenttype/detail/(?P<slug>\S+)/$',
        views.ContentTypeDetailView.as_view(), name='api_gooten_contenttype_detail'),
    url(r'^api_gooten/contenttype/update/(?P<slug>\S+)/$',
        views.ContentTypeUpdateView.as_view(), name='api_gooten_contenttype_update'),
)

urlpatterns += (
    # urls for InfoContent
    url(r'^api_gooten/infocontent/$', views.InfoContentListView.as_view(),
        name='api_gooten_infocontent_list'),
    url(r'^api_gooten/infocontent/create/$', views.InfoContentCreateView.as_view(),
        name='api_gooten_infocontent_create'),
    url(r'^api_gooten/infocontent/detail/(?P<slug>\S+)/$',
        views.InfoContentDetailView.as_view(), name='api_gooten_infocontent_detail'),
    url(r'^api_gooten/infocontent/update/(?P<slug>\S+)/$',
        views.InfoContentUpdateView.as_view(), name='api_gooten_infocontent_update'),
)

urlpatterns += (
    # urls for Variant
    url(r'^api_gooten/variant/$', views.VariantListView.as_view(), name='api_gooten_variant_list'),
    url(r'^api_gooten/variant/create/$', views.VariantCreateView.as_view(),
        name='api_gooten_variant_create'),
    url(r'^api_gooten/variant/detail/(?P<slug>\S+)/$',
        views.VariantDetailView.as_view(), name='api_gooten_variant_detail'),
    url(r'^api_gooten/variant/update/(?P<slug>\S+)/$',
        views.VariantUpdateView.as_view(), name='api_gooten_variant_update'),
)

urlpatterns += (
    # urls for Attribute
    url(r'^api_gooten/attribute/$', views.AttributeListView.as_view(), name='api_gooten_attribute_list'),
    url(r'^api_gooten/attribute/create/$', views.AttributeCreateView.as_view(),
        name='api_gooten_attribute_create'),
    url(r'^api_gooten/attribute/detail/(?P<slug>\S+)/$',
        views.AttributeDetailView.as_view(), name='api_gooten_attribute_detail'),
    url(r'^api_gooten/attribute/update/(?P<slug>\S+)/$',
        views.AttributeUpdateView.as_view(), name='api_gooten_attribute_update'),
)

urlpatterns += (
    # urls for AttributeValue
    url(r'^api_gooten/attributevalue/$', views.AttributeValueListView.as_view(),
        name='api_gooten_attributevalue_list'),
    url(r'^api_gooten/attributevalue/create/$', views.AttributeValueCreateView.as_view(),
        name='api_gooten_attributevalue_create'),
    url(r'^api_gooten/attributevalue/detail/(?P<slug>\S+)/$',
        views.AttributeValueDetailView.as_view(), name='api_gooten_attributevalue_detail'),
    url(r'^api_gooten/attributevalue/update/(?P<slug>\S+)/$',
        views.AttributeValueUpdateView.as_view(), name='api_gooten_attributevalue_update'),
)

urlpatterns += (
    # urls for VariantOption
    url(r'^api_gooten/variantoption/$', views.VariantOptionListView.as_view(),
        name='api_gooten_variantoption_list'),
    url(r'^api_gooten/variantoption/create/$', views.VariantOptionCreateView.as_view(),
        name='api_gooten_variantoption_create'),
    url(r'^api_gooten/variantoption/detail/(?P<slug>\S+)/$',
        views.VariantOptionDetailView.as_view(), name='api_gooten_variantoption_detail'),
    url(r'^api_gooten/variantoption/update/(?P<slug>\S+)/$',
        views.VariantOptionUpdateView.as_view(), name='api_gooten_variantoption_update'),
)

urlpatterns += (
    # urls for VariantTemplate
    url(r'^api_gooten/varianttemplate/$', views.VariantTemplateListView.as_view(),
        name='api_gooten_varianttemplate_list'),
    url(r'^api_gooten/varianttemplate/create/$', views.VariantTemplateCreateView.as_view(),
        name='api_gooten_varianttemplate_create'),
    url(r'^api_gooten/varianttemplate/detail/(?P<slug>\S+)/$',
        views.VariantTemplateDetailView.as_view(), name='api_gooten_VariantTemplate_detail'),
    url(r'^api_gooten/varianttemplate/update/(?P<slug>\S+)/$',
        views.VariantTemplateUpdateView.as_view(), name='api_gooten_VariantTemplate_update'),
)

urlpatterns += (
    # urls for TemplateSpace
    url(r'^api_gooten/templatespace/$', views.TemplateSpaceListView.as_view(),
        name='api_gooten_templatespace_list'),
    url(r'^api_gooten/templatespace/create/$', views.TemplateSpaceCreateView.as_view(),
        name='api_gooten_templatespace_create'),
    url(r'^api_gooten/templatespace/detail/(?P<slug>\S+)/$',
        views.TemplateSpaceDetailView.as_view(), name='api_gooten_templatespace_detail'),
    url(r'^api_gooten/templatespace/update/(?P<slug>\S+)/$',
        views.TemplateSpaceUpdateView.as_view(), name='api_gooten_templatespace_update'),
)

urlpatterns += (
    # urls for LayerType
    url(r'^api_gooten/layertype/$', views.LayerTypeListView.as_view(), name='api_gooten_layertype_list'),
    url(r'^api_gooten/layertype/create/$', views.LayerTypeCreateView.as_view(),
        name='api_gooten_layertype_create'),
    url(r'^api_gooten/layertype/detail/(?P<slug>\S+)/$',
        views.LayerTypeDetailView.as_view(), name='api_gooten_layertype_detail'),
    url(r'^api_gooten/layertype/update/(?P<slug>\S+)/$',
        views.LayerTypeUpdateView.as_view(), name='api_gooten_layertype_update'),
)

urlpatterns += (
    # urls for SpaceLayer
    url(r'^api_gooten/spacelayer/$', views.SpaceLayerListView.as_view(), name='api_gooten_spacelayer_list'),
    url(r'^api_gooten/spacelayer/create/$', views.SpaceLayerCreateView.as_view(),
        name='api_gooten_spacelayer_create'),
    url(r'^api_gooten/spacelayer/detail/(?P<slug>\S+)/$',
        views.SpaceLayerDetailView.as_view(), name='api_gooten_spacelayer_detail'),
    url(r'^api_gooten/spacelayer/update/(?P<slug>\S+)/$',
        views.SpaceLayerUpdateView.as_view(), name='api_gooten_spacelayer_update'),
)
