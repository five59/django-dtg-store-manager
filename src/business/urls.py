from django.conf.urls import url, include
from rest_framework import routers
from business import api, views

router = routers.DefaultRouter()
router.register(r'bzbrand', api.bzBrandViewSet)
router.register(r'bzcreativecollection', api.bzCreativeCollectionViewSet)
router.register(r'bzcreativedesign', api.bzCreativeDesignViewSet)
router.register(r'bzcreativelayout', api.bzCreativeLayoutViewSet)
router.register(r'bzcreativerendering', api.bzCreativeRenderingViewSet)
router.register(r'bzproduct', api.bzProductViewSet)
router.register(r'bzproductvariant', api.bzProductVariantViewSet)
router.register(r'wooattribute', api.wooAttributeViewSet)
router.register(r'woocategory', api.wooCategoryViewSet)
router.register(r'wooimage', api.wooImageViewSet)
router.register(r'wooproduct', api.wooProductViewSet)
router.register(r'wooshippingclass', api.wooShippingClassViewSet)
router.register(r'woostore', api.wooStoreViewSet)
router.register(r'wootag', api.wooTagViewSet)
router.register(r'wooterm', api.wooTermViewSet)
router.register(r'woovariant', api.wooVariantViewSet)
router.register(r'wpmedia', api.wpMediaViewSet)
router.register(r'wpmediasize', api.wpMediaSizeViewSet)
router.register(r'pfcountry', api.pfCountryViewSet)
router.register(r'pfstate', api.pfStateViewSet)
router.register(r'pfsyncproduct', api.pfSyncProductViewSet)
router.register(r'pfsyncvariant', api.pfSyncVariantViewSet)
router.register(r'pfsyncitemoption', api.pfSyncItemOptionViewSet)
router.register(r'pfcatalogcolor', api.pfCatalogColorViewSet)
router.register(r'pfcatalogsize', api.pfCatalogSizeViewSet)
router.register(r'pfcatalogfilespec', api.pfCatalogFileSpecViewSet)
router.register(r'pfcatalogfiletype', api.pfCatalogFileTypeViewSet)
router.register(r'pfcatalogoptiontype', api.pfCatalogOptionTypeViewSet)
router.register(r'pfcatalogproduct', api.pfCatalogProductViewSet)
router.register(r'pfcatalogvariant', api.pfCatalogVariantViewSet)
router.register(r'pfstore', api.pfStoreViewSet)
router.register(r'pfprintfile', api.pfPrintFileViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for bzBrand
    url(r'^bzbrand/$', views.bzBrandListView.as_view(),
        name='business_bzbrand_list'),
    url(r'^bzbrand/create/$', views.bzBrandCreateView.as_view(),
        name='business_bzbrand_create'),
    url(r'^bzbrand/detail/(?P<pk>\S+)/$',
        views.bzBrandDetailView.as_view(), name='business_bzbrand_detail'),
    url(r'^bzbrand/update/(?P<pk>\S+)/$',
        views.bzBrandUpdateView.as_view(), name='business_bzbrand_update'),
)

urlpatterns += (
    # urls for bzCreativeCollection
    url(r'^bzcreativecollection/$', views.bzCreativeCollectionListView.as_view(),
        name='business_bzcreativecollection_list'),
    url(r'^bzcreativecollection/create/$',
        views.bzCreativeCollectionCreateView.as_view(), name='business_bzcreativecollection_create'),
    url(r'^bzcreativecollection/detail/(?P<pk>\S+)/$',
        views.bzCreativeCollectionDetailView.as_view(), name='business_bzcreativecollection_detail'),
    url(r'^bzcreativecollection/update/(?P<pk>\S+)/$',
        views.bzCreativeCollectionUpdateView.as_view(), name='business_bzcreativecollection_update'),
)

urlpatterns += (
    # urls for bzCreativeDesign
    url(r'^bzcreativedesign/$', views.bzCreativeDesignListView.as_view(),
        name='business_bzcreativedesign_list'),
    url(r'^bzcreativedesign/create/$', views.bzCreativeDesignCreateView.as_view(),
        name='business_bzcreativedesign_create'),
    url(r'^bzcreativedesign/detail/(?P<pk>\S+)/$',
        views.bzCreativeDesignDetailView.as_view(), name='business_bzcreativedesign_detail'),
    url(r'^bzcreativedesign/update/(?P<pk>\S+)/$',
        views.bzCreativeDesignUpdateView.as_view(), name='business_bzcreativedesign_update'),
)

urlpatterns += (
    # urls for bzCreativeLayout
    url(r'^bzcreativelayout/$', views.bzCreativeLayoutListView.as_view(),
        name='business_bzcreativelayout_list'),
    url(r'^bzcreativelayout/create/$', views.bzCreativeLayoutCreateView.as_view(),
        name='business_bzcreativelayout_create'),
    url(r'^bzcreativelayout/detail/(?P<pk>\S+)/$',
        views.bzCreativeLayoutDetailView.as_view(), name='business_bzcreativelayout_detail'),
    url(r'^bzcreativelayout/update/(?P<pk>\S+)/$',
        views.bzCreativeLayoutUpdateView.as_view(), name='business_bzcreativelayout_update'),
)

urlpatterns += (
    # urls for bzCreativeRendering
    url(r'^bzcreativerendering/$', views.bzCreativeRenderingListView.as_view(),
        name='business_bzcreativerendering_list'),
    url(r'^bzcreativerendering/create/$',
        views.bzCreativeRenderingCreateView.as_view(), name='business_bzcreativerendering_create'),
    url(r'^bzcreativerendering/detail/(?P<pk>\S+)/$',
        views.bzCreativeRenderingDetailView.as_view(), name='business_bzcreativerendering_detail'),
    url(r'^bzcreativerendering/update/(?P<pk>\S+)/$',
        views.bzCreativeRenderingUpdateView.as_view(), name='business_bzcreativerendering_update'),
)

urlpatterns += (
    # urls for bzProduct
    url(r'^bzproduct/$', views.bzProductListView.as_view(),
        name='business_bzproduct_list'),
    url(r'^bzproduct/create/$', views.bzProductCreateView.as_view(),
        name='business_bzproduct_create'),
    url(r'^bzproduct/detail/(?P<pk>\S+)/$',
        views.bzProductDetailView.as_view(), name='business_bzproduct_detail'),
    url(r'^bzproduct/update/(?P<pk>\S+)/$',
        views.bzProductUpdateView.as_view(), name='business_bzproduct_update'),
)

urlpatterns += (
    # urls for bzProductVariant
    url(r'^bzproductvariant/$', views.bzProductVariantListView.as_view(),
        name='business_bzproductvariant_list'),
    url(r'^bzproductvariant/create/$', views.bzProductVariantCreateView.as_view(),
        name='business_bzproductvariant_create'),
    url(r'^bzproductvariant/detail/(?P<pk>\S+)/$',
        views.bzProductVariantDetailView.as_view(), name='business_bzproductvariant_detail'),
    url(r'^bzproductvariant/update/(?P<pk>\S+)/$',
        views.bzProductVariantUpdateView.as_view(), name='business_bzproductvariant_update'),
)

urlpatterns += (
    # urls for wooAttribute
    url(r'^wooattribute/$', views.wooAttributeListView.as_view(),
        name='business_wooattribute_list'),
    url(r'^wooattribute/create/$', views.wooAttributeCreateView.as_view(),
        name='business_wooattribute_create'),
    url(r'^wooattribute/detail/(?P<slug>\S+)/$',
        views.wooAttributeDetailView.as_view(), name='business_wooattribute_detail'),
    url(r'^wooattribute/update/(?P<slug>\S+)/$',
        views.wooAttributeUpdateView.as_view(), name='business_wooattribute_update'),
)

urlpatterns += (
    # urls for wooCategory
    url(r'^woocategory/$', views.wooCategoryListView.as_view(),
        name='business_woocategory_list'),
    url(r'^woocategory/create/$', views.wooCategoryCreateView.as_view(),
        name='business_woocategory_create'),
    url(r'^woocategory/detail/(?P<slug>\S+)/$',
        views.wooCategoryDetailView.as_view(), name='business_woocategory_detail'),
    url(r'^woocategory/update/(?P<slug>\S+)/$',
        views.wooCategoryUpdateView.as_view(), name='business_woocategory_update'),
)

urlpatterns += (
    # urls for wooImage
    url(r'^wooimage/$', views.wooImageListView.as_view(),
        name='business_wooimage_list'),
    url(r'^wooimage/create/$', views.wooImageCreateView.as_view(),
        name='business_wooimage_create'),
    url(r'^wooimage/detail/(?P<pk>\S+)/$',
        views.wooImageDetailView.as_view(), name='business_wooimage_detail'),
    url(r'^wooimage/update/(?P<pk>\S+)/$',
        views.wooImageUpdateView.as_view(), name='business_wooimage_update'),
)

urlpatterns += (
    # urls for wooProduct
    url(r'^wooproduct/$', views.wooProductListView.as_view(),
        name='business_wooproduct_list'),
    url(r'^wooproduct/create/$', views.wooProductCreateView.as_view(),
        name='business_wooproduct_create'),
    url(r'^wooproduct/detail/(?P<slug>\S+)/$',
        views.wooProductDetailView.as_view(), name='business_wooproduct_detail'),
    url(r'^wooproduct/update/(?P<slug>\S+)/$',
        views.wooProductUpdateView.as_view(), name='business_wooproduct_update'),
)

urlpatterns += (
    # urls for wooShippingClass
    url(r'^wooshippingclass/$', views.wooShippingClassListView.as_view(),
        name='business_wooshippingclass_list'),
    url(r'^wooshippingclass/create/$', views.wooShippingClassCreateView.as_view(),
        name='business_wooshippingclass_create'),
    url(r'^wooshippingclass/detail/(?P<slug>\S+)/$',
        views.wooShippingClassDetailView.as_view(), name='business_wooshippingclass_detail'),
    url(r'^wooshippingclass/update/(?P<slug>\S+)/$',
        views.wooShippingClassUpdateView.as_view(), name='business_wooshippingclass_update'),
)

urlpatterns += (
    # urls for wooStore
    url(r'^woostore/$', views.wooStoreListView.as_view(),
        name='business_woostore_list'),
    url(r'^woostore/create/$', views.wooStoreCreateView.as_view(),
        name='business_woostore_create'),
    url(r'^woostore/detail/(?P<pk>\S+)/$',
        views.wooStoreDetailView.as_view(), name='business_woostore_detail'),
    url(r'^woostore/update/(?P<pk>\S+)/$',
        views.wooStoreUpdateView.as_view(), name='business_woostore_update'),
)

urlpatterns += (
    # urls for wooTag
    url(r'^wootag/$', views.wooTagListView.as_view(), name='business_wootag_list'),
    url(r'^wootag/create/$', views.wooTagCreateView.as_view(),
        name='business_wootag_create'),
    url(r'^wootag/detail/(?P<slug>\S+)/$',
        views.wooTagDetailView.as_view(), name='business_wootag_detail'),
    url(r'^wootag/update/(?P<slug>\S+)/$',
        views.wooTagUpdateView.as_view(), name='business_wootag_update'),
)

urlpatterns += (
    # urls for wooTerm
    url(r'^wooterm/$', views.wooTermListView.as_view(),
        name='business_wooterm_list'),
    url(r'^wooterm/create/$', views.wooTermCreateView.as_view(),
        name='business_wooterm_create'),
    url(r'^wooterm/detail/(?P<slug>\S+)/$',
        views.wooTermDetailView.as_view(), name='business_wooterm_detail'),
    url(r'^wooterm/update/(?P<slug>\S+)/$',
        views.wooTermUpdateView.as_view(), name='business_wooterm_update'),
)

urlpatterns += (
    # urls for wooVariant
    url(r'^woovariant/$', views.wooVariantListView.as_view(),
        name='business_woovariant_list'),
    url(r'^woovariant/create/$', views.wooVariantCreateView.as_view(),
        name='business_woovariant_create'),
    url(r'^woovariant/detail/(?P<pk>\S+)/$',
        views.wooVariantDetailView.as_view(), name='business_woovariant_detail'),
    url(r'^woovariant/update/(?P<pk>\S+)/$',
        views.wooVariantUpdateView.as_view(), name='business_woovariant_update'),
)

urlpatterns += (
    # urls for wpMedia
    url(r'^wpmedia/$', views.wpMediaListView.as_view(),
        name='business_wpmedia_list'),
    url(r'^wpmedia/create/$', views.wpMediaCreateView.as_view(),
        name='business_wpmedia_create'),
    url(r'^wpmedia/detail/(?P<slug>\S+)/$',
        views.wpMediaDetailView.as_view(), name='business_wpmedia_detail'),
    url(r'^wpmedia/update/(?P<slug>\S+)/$',
        views.wpMediaUpdateView.as_view(), name='business_wpmedia_update'),
)

urlpatterns += (
    # urls for wpMediaSize
    url(r'^wpmediasize/$', views.wpMediaSizeListView.as_view(),
        name='business_wpmediasize_list'),
    url(r'^wpmediasize/create/$', views.wpMediaSizeCreateView.as_view(),
        name='business_wpmediasize_create'),
    url(r'^wpmediasize/detail/(?P<pk>\S+)/$',
        views.wpMediaSizeDetailView.as_view(), name='business_wpmediasize_detail'),
    url(r'^wpmediasize/update/(?P<pk>\S+)/$',
        views.wpMediaSizeUpdateView.as_view(), name='business_wpmediasize_update'),
)

urlpatterns += (
    # urls for pfCountry
    url(r'^pfcountry/$', views.pfCountryListView.as_view(),
        name='business_pfcountry_list'),
    url(r'^pfcountry/create/$', views.pfCountryCreateView.as_view(),
        name='business_pfcountry_create'),
    url(r'^pfcountry/detail/(?P<pk>\S+)/$',
        views.pfCountryDetailView.as_view(), name='business_pfcountry_detail'),
    url(r'^pfcountry/update/(?P<pk>\S+)/$',
        views.pfCountryUpdateView.as_view(), name='business_pfcountry_update'),
)

urlpatterns += (
    # urls for pfState
    url(r'^pfstate/$', views.pfStateListView.as_view(),
        name='business_pfstate_list'),
    url(r'^pfstate/create/$', views.pfStateCreateView.as_view(),
        name='business_pfstate_create'),
    url(r'^pfstate/detail/(?P<pk>\S+)/$',
        views.pfStateDetailView.as_view(), name='business_pfstate_detail'),
    url(r'^pfstate/update/(?P<pk>\S+)/$',
        views.pfStateUpdateView.as_view(), name='business_pfstate_update'),
)

urlpatterns += (
    # urls for pfSyncProduct
    url(r'^pfsyncproduct/$', views.pfSyncProductListView.as_view(),
        name='business_pfsyncproduct_list'),
    url(r'^pfsyncproduct/create/$', views.pfSyncProductCreateView.as_view(),
        name='business_pfsyncproduct_create'),
    url(r'^pfsyncproduct/detail/(?P<pk>\S+)/$',
        views.pfSyncProductDetailView.as_view(), name='business_pfsyncproduct_detail'),
    url(r'^pfsyncproduct/update/(?P<pk>\S+)/$',
        views.pfSyncProductUpdateView.as_view(), name='business_pfsyncproduct_update'),
)

urlpatterns += (
    # urls for pfSyncVariant
    url(r'^pfsyncvariant/$', views.pfSyncVariantListView.as_view(),
        name='business_pfsyncvariant_list'),
    url(r'^pfsyncvariant/create/$', views.pfSyncVariantCreateView.as_view(),
        name='business_pfsyncvariant_create'),
    url(r'^pfsyncvariant/detail/(?P<pk>\S+)/$',
        views.pfSyncVariantDetailView.as_view(), name='business_pfsyncvariant_detail'),
    url(r'^pfsyncvariant/update/(?P<pk>\S+)/$',
        views.pfSyncVariantUpdateView.as_view(), name='business_pfsyncvariant_update'),
)

urlpatterns += (
    # urls for pfSyncItemOption
    url(r'^pfsyncitemoption/$', views.pfSyncItemOptionListView.as_view(),
        name='business_pfsyncitemoption_list'),
    url(r'^pfsyncitemoption/create/$', views.pfSyncItemOptionCreateView.as_view(),
        name='business_pfsyncitemoption_create'),
    url(r'^pfsyncitemoption/detail/(?P<pk>\S+)/$',
        views.pfSyncItemOptionDetailView.as_view(), name='business_pfsyncitemoption_detail'),
    url(r'^pfsyncitemoption/update/(?P<pk>\S+)/$',
        views.pfSyncItemOptionUpdateView.as_view(), name='business_pfsyncitemoption_update'),
)

urlpatterns += (
    # urls for pfCatalogColor
    url(r'^pfcatalogcolor/$', views.pfCatalogColorListView.as_view(),
        name='business_pfcatalogcolor_list'),
    url(r'^pfcatalogcolor/create/$', views.pfCatalogColorCreateView.as_view(),
        name='business_pfcatalogcolor_create'),
    url(r'^pfcatalogcolor/detail/(?P<pk>\S+)/$',
        views.pfCatalogColorDetailView.as_view(), name='business_pfcatalogcolor_detail'),
    url(r'^pfcatalogcolor/update/(?P<pk>\S+)/$',
        views.pfCatalogColorUpdateView.as_view(), name='business_pfcatalogcolor_update'),
)

urlpatterns += (
    # urls for pfCatalogSize
    url(r'^pfcatalogsize/$', views.pfCatalogSizeListView.as_view(),
        name='business_pfcatalogsize_list'),
    url(r'^pfcatalogsize/create/$', views.pfCatalogSizeCreateView.as_view(),
        name='business_pfcatalogsize_create'),
    url(r'^pfcatalogsize/detail/(?P<pk>\S+)/$',
        views.pfCatalogSizeDetailView.as_view(), name='business_pfcatalogsize_detail'),
    url(r'^pfcatalogsize/update/(?P<pk>\S+)/$',
        views.pfCatalogSizeUpdateView.as_view(), name='business_pfcatalogsize_update'),
)

urlpatterns += (
    # urls for pfCatalogFileSpec
    url(r'^pfcatalogfilespec/$', views.pfCatalogFileSpecListView.as_view(),
        name='business_pfcatalogfilespec_list'),
    url(r'^pfcatalogfilespec/create/$', views.pfCatalogFileSpecCreateView.as_view(),
        name='business_pfcatalogfilespec_create'),
    url(r'^pfcatalogfilespec/detail/(?P<pk>\S+)/$',
        views.pfCatalogFileSpecDetailView.as_view(), name='business_pfcatalogfilespec_detail'),
    url(r'^pfcatalogfilespec/update/(?P<pk>\S+)/$',
        views.pfCatalogFileSpecUpdateView.as_view(), name='business_pfcatalogfilespec_update'),
)

urlpatterns += (
    # urls for pfCatalogFileType
    url(r'^pfcatalogfiletype/$', views.pfCatalogFileTypeListView.as_view(),
        name='business_pfcatalogfiletype_list'),
    url(r'^pfcatalogfiletype/create/$', views.pfCatalogFileTypeCreateView.as_view(),
        name='business_pfcatalogfiletype_create'),
    url(r'^pfcatalogfiletype/detail/(?P<pk>\S+)/$',
        views.pfCatalogFileTypeDetailView.as_view(), name='business_pfcatalogfiletype_detail'),
    url(r'^pfcatalogfiletype/update/(?P<pk>\S+)/$',
        views.pfCatalogFileTypeUpdateView.as_view(), name='business_pfcatalogfiletype_update'),
)

urlpatterns += (
    # urls for pfCatalogOptionType
    url(r'^pfcatalogoptiontype/$', views.pfCatalogOptionTypeListView.as_view(),
        name='business_pfcatalogoptiontype_list'),
    url(r'^pfcatalogoptiontype/create/$',
        views.pfCatalogOptionTypeCreateView.as_view(), name='business_pfcatalogoptiontype_create'),
    url(r'^pfcatalogoptiontype/detail/(?P<pk>\S+)/$',
        views.pfCatalogOptionTypeDetailView.as_view(), name='business_pfcatalogoptiontype_detail'),
    url(r'^pfcatalogoptiontype/update/(?P<pk>\S+)/$',
        views.pfCatalogOptionTypeUpdateView.as_view(), name='business_pfcatalogoptiontype_update'),
)

urlpatterns += (
    # urls for pfCatalogProduct
    url(r'^pfcatalogproduct/$', views.pfCatalogProductListView.as_view(),
        name='business_pfcatalogproduct_list'),
    url(r'^pfcatalogproduct/create/$', views.pfCatalogProductCreateView.as_view(),
        name='business_pfcatalogproduct_create'),
    url(r'^pfcatalogproduct/detail/(?P<pk>\S+)/$',
        views.pfCatalogProductDetailView.as_view(), name='business_pfcatalogproduct_detail'),
    url(r'^pfcatalogproduct/update/(?P<pk>\S+)/$',
        views.pfCatalogProductUpdateView.as_view(), name='business_pfcatalogproduct_update'),
)

urlpatterns += (
    # urls for pfCatalogVariant
    url(r'^pfcatalogvariant/$', views.pfCatalogVariantListView.as_view(),
        name='business_pfcatalogvariant_list'),
    url(r'^pfcatalogvariant/create/$', views.pfCatalogVariantCreateView.as_view(),
        name='business_pfcatalogvariant_create'),
    url(r'^pfcatalogvariant/detail/(?P<pk>\S+)/$',
        views.pfCatalogVariantDetailView.as_view(), name='business_pfcatalogvariant_detail'),
    url(r'^pfcatalogvariant/update/(?P<pk>\S+)/$',
        views.pfCatalogVariantUpdateView.as_view(), name='business_pfcatalogvariant_update'),
)

urlpatterns += (
    # urls for pfStore
    url(r'^pfstore/$', views.pfStoreListView.as_view(),
        name='business_pfstore_list'),
    url(r'^pfstore/create/$', views.pfStoreCreateView.as_view(),
        name='business_pfstore_create'),
    url(r'^pfstore/detail/(?P<pk>\S+)/$',
        views.pfStoreDetailView.as_view(), name='business_pfstore_detail'),
    url(r'^pfstore/update/(?P<pk>\S+)/$',
        views.pfStoreUpdateView.as_view(), name='business_pfstore_update'),
)

urlpatterns += (
    # urls for pfPrintFile
    url(r'^pfprintfile/$', views.pfPrintFileListView.as_view(),
        name='business_pfprintfile_list'),
    url(r'^pfprintfile/create/$', views.pfPrintFileCreateView.as_view(),
        name='business_pfprintfile_create'),
    url(r'^pfprintfile/detail/(?P<pk>\S+)/$',
        views.pfPrintFileDetailView.as_view(), name='business_pfprintfile_detail'),
    url(r'^pfprintfile/update/(?P<pk>\S+)/$',
        views.pfPrintFileUpdateView.as_view(), name='business_pfprintfile_update'),
)
