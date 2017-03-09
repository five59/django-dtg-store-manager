from django.conf.urls import url, include
from rest_framework import routers
from business import api
from business.views import *

# router = routers.DefaultRouter()
# router.register(r'bzbrand', api.bzBrandViewSet)
# router.register(r'bzcreativecollection', api.bzCreativeCollectionViewSet)
# router.register(r'bzcreativedesign', api.bzCreativeDesignViewSet)
# router.register(r'bzcreativelayout', api.bzCreativeLayoutViewSet)
# router.register(r'bzcreativerendering', api.bzCreativeRenderingViewSet)
# router.register(r'bzproduct', api.bzProductViewSet)
# router.register(r'bzproductvariant', api.bzProductVariantViewSet)
# router.register(r'wooattribute', api.wooAttributeViewSet)
# router.register(r'woocategory', api.wooCategoryViewSet)
# router.register(r'wooimage', api.wooImageViewSet)
# router.register(r'wooproduct', api.wooProductViewSet)
# router.register(r'wooshippingclass', api.wooShippingClassViewSet)
# router.register(r'woostore', api.wooStoreViewSet)
# router.register(r'wootag', api.wooTagViewSet)
# router.register(r'wooterm', api.wooTermViewSet)
# router.register(r'woovariant', api.wooVariantViewSet)
# router.register(r'wpmedia', api.wpMediaViewSet)
# router.register(r'wpmediasize', api.wpMediaSizeViewSet)
# router.register(r'pfcountry', api.pfCountryViewSet)
# router.register(r'pfstate', api.pfStateViewSet)
# router.register(r'pfsyncproduct', api.pfSyncProductViewSet)
# router.register(r'pfsyncvariant', api.pfSyncVariantViewSet)
# router.register(r'pfsyncitemoption', api.pfSyncItemOptionViewSet)
# router.register(r'pfcatalogcolor', api.pfCatalogColorViewSet)
# router.register(r'pfcatalogsize', api.pfCatalogSizeViewSet)
# router.register(r'pfcatalogfilespec', api.pfCatalogFileSpecViewSet)
# router.register(r'pfcatalogfiletype', api.pfCatalogFileTypeViewSet)
# router.register(r'pfcatalogoptiontype', api.pfCatalogOptionTypeViewSet)
# router.register(r'pfcatalogproduct', api.pfCatalogProductViewSet)
# router.register(r'pfcatalogvariant', api.pfCatalogVariantViewSet)
# router.register(r'pfstore', api.pfStoreViewSet)
# router.register(r'pfprintfile', api.pfPrintFileViewSet)
#
#
urlpatterns = (
    #     # urls for Django Rest Framework API
    #     url(r'^api/v1/', include(router.urls)),
)
#

# urls for Home Page et al.
urlpatterns += (
    url(r'^$', bzHomeView.as_view(), name='business_home_view'),
)

# URLs for Dashboard App
urlpatterns += (
    url(r'^dashboard/$', appDashboardHome.as_view(), name='app_dashboard_home'),
    # url(r'^/$', appHome.as_view(), name='app__home'),
    # url(r'^/$', appHome.as_view(), name='app__home'),
)

# URLs for Creative App
urlpatterns += (
    url(r'^creative/$',
        appCreativeHome.as_view(), name='app_creative_home'),
    url(r'^creative/collection-(?P<collection>\S+)/$',
        appCreativeHome.as_view(), name='app_creative_home'),

    url(r'^creative/collection/update/(?P<pk>\S+)/$',
        appCreativeCollectionUpdate.as_view(), name='app_creative_collection_update'),
    url(r'^creative/design/update/(?P<pk>\S+)/$',
        appCreativeDesignUpdate.as_view(), name='app_creative_design_update'),
    url(r'^creative/layout/update/(?P<pk>\S+)/$',
        appCreativeLayoutUpdate.as_view(), name='app_creative_layout_update'),

    url(r'^creative/collection/create/$',
        appCreativeCollectionCreate.as_view(), name='app_creative_collection_create'),
    url(r'^creative/design/create/$',
        appCreativeDesignCreate.as_view(), name='app_creative_design_create'),
    url(r'^creative/layout/create/$',
        appCreativeLayoutCreate.as_view(), name='app_creative_layout_create'),
)

# URLs for Product
urlpatterns += (
    url(r'^product/$', appProductHome.as_view(), name='app_product_home'),
    url(r'^product/detail-(?P<product>\S+)/$',
        appProductHome.as_view(), name="app_product_home"),
    url(r'^product/create/$',
        appProductCreate.as_view(), name="app_product_create"),
    url(r'^product/update/(?P<pk>\S+)/$',
        appProductUpdate.as_view(), name="app_product_update"),
)

# URLs for Store App
urlpatterns += (
    url(r'^store/$', appStoreHome.as_view(), name='app_store_home'),

    url(r'^store/brand/$', appStoreBrandList.as_view(),
        name='app_store_brand_list'),
    url(r'^store/brand/create/$', appStoreBrandCreate.as_view(),
        name='app_store_brand_create'),
    url(r'^store/brand/update/(?P<pk>\S+)/$',
        appStoreBrandUpdate.as_view(), name='app_store_brand_update'),

    url(r'^store/printful/$', appStorePFList.as_view(), name='app_store_pf_list'),
    url(r'^store/printful/create/$',
        appStorePFCreate.as_view(), name='app_store_pf_create'),
    url(r'^store/printful/update/(?P<pk>\S+)/$',
        appStorePFUpdate.as_view(), name='app_store_pf_update'),

    url(r'^store/wordpress/$', appStoreWPList.as_view(), name='app_store_wp_list'),
    url(r'^store/wordpress/create/$',
        appStoreWPCreate.as_view(), name='app_store_wp_create'),
    url(r'^store/wordpress/update/(?P<pk>\S+)/$',
        appStoreWPUpdate.as_view(), name='app_store_wp_update'),
)

# URLs for DAMS App
urlpatterns += (
    url(r'^dams/$', appDAMSHome.as_view(), name='app_dams_home'),
    # url(r'^/$', appHome.as_view(), name='app__home'),
    # url(r'^/$', appHome.as_view(), name='app__home'),
)

# URLs for Content App
urlpatterns += (
    url(r'^content/$', appContentHome.as_view(), name='app_content_home'),
)

# URLs for List App
urlpatterns += (
    url(r'^lists/$', appListsHome.as_view(), name='app_lists_home'),

    url(r'^lists/geo/$', appListGeoList.as_view(), name='app_list_geo_list'),
    url(r'^lists/geo/(?P<pk>\S+)/$',
        appListGeoDetail.as_view(), name='app_list_geo_detail'),
    url(r'^lists/geo/$', appListGeoPull.as_view(), name='app_list_geo_pull'),

    url(r'^lists/color/$', appListColorList.as_view(), name='app_list_color_list'),
    url(r'^lists/color/(?P<pk>\S+)/$',
        appListColorUpdate.as_view(), name='app_list_color_update'),

    url(r'^lists/size/$', appListSizeList.as_view(), name='app_list_size_list'),
    url(r'^lists/size/(?P<pk>\S+)/$',
        appListSizeUpdate.as_view(), name='app_list_size_update'),

    url(r'^lists/filespec/$', appListFileSpecList.as_view(),
        name='app_list_filespec_list'),
    url(r'^lists/filespec/create/$',
        appListFileSpecCreate.as_view(), name='app_list_filespec_create'),
    url(r'^lists/filespec/(?P<pk>\S+)/$',
        appListFileSpecUpdate.as_view(), name='app_list_filespec_update'),

    url(r'^lists/shipping/$', appListShippingList.as_view(),
        name='app_list_shipping_list'),
    url(r'^lists/shipping/create/$', appListShippingCreate.as_view(),
        name='app_list_shipping_create'),
    url(r'^lists/shipping/(?P<pk>\S+)/$',
        appListShippingUpdate.as_view(), name='app_list_shipping_update'),
    url(r'^lists/shipping/$', appListShippingPush.as_view(),
        name='app_list_shipping_push'),
    url(r'^lists/shipping/$', appListShippingPull.as_view(),
        name='app_list_shipping_pull'),

    url(r'^lists/category/$', appListCategoryList.as_view(),
        name='app_list_category_list'),
    url(r'^lists/category/create/$', appListCategoryCreate.as_view(),
        name='app_list_category_create'),
    url(r'^lists/category/(?P<pk>\S+)/$',
        appListCategoryUpdate.as_view(), name='app_list_category_update'),
    url(r'^lists/category/$', appListCategoryPush.as_view(),
        name='app_list_category_push'),
    url(r'^lists/category/$', appListCategoryPull.as_view(),
        name='app_list_category_pull'),

    url(r'^lists/tag/$', appListTagList.as_view(), name='app_list_tag_list'),
    url(r'^lists/tag/create/$', appListTagCreate.as_view(),
        name='app_list_tag_create'),
    url(r'^lists/tag/(?P<pk>\S+)/$',
        appListTagUpdate.as_view(), name='app_list_tag_update'),
    url(r'^lists/tag/$', appListTagPush.as_view(), name='app_list_tag_push'),
    url(r'^lists/tag/$', appListTagPull.as_view(), name='app_list_tag_pull'),

    url(r'^lists/cprod/$', appListCatProductList.as_view(),
        name='app_list_cprod_list'),
    url(r'^lists/cprod/(?P<pk>\S+)/$',
        appListCatProductUpdate.as_view(), name='app_list_cprod_update'),

    url(r'^lists/attribute/$', appListAttributeList.as_view(),
        name='app_list_attribute_list'),
    url(r'^lists/attribute/(?P<pk>\S+)/$',
        appListAttributeUpdate.as_view(), name='app_list_attribute_update'),
)


# Old data patterns

urlpatterns += (
    # urls for bzBrand
    url(r'^bzbrand/$', bzBrandListView.as_view(), name='business_bzbrand_list'),
    url(r'^bzbrand/create/$', bzBrandCreateView.as_view(),
        name='business_bzbrand_create'),
    url(r'^bzbrand/detail/(?P<pk>\S+)/$',
        bzBrandDetailView.as_view(), name='business_bzbrand_detail'),
    url(r'^bzbrand/update/(?P<pk>\S+)/$',
        bzBrandUpdateView.as_view(), name='business_bzbrand_update'),
)

urlpatterns += (
    # urls for bzCreativeCollection
    url(r'^bzcreativecollection/$', bzCreativeCollectionListView.as_view(),
        name='business_bzcreativecollection_list'),
    url(r'^bzcreativecollection/create/$',
        bzCreativeCollectionCreateView.as_view(), name='business_bzcreativecollection_create'),
    url(r'^bzcreativecollection/detail/(?P<pk>\S+)/$',
        bzCreativeCollectionDetailView.as_view(), name='business_bzcreativecollection_detail'),
    url(r'^bzcreativecollection/update/(?P<pk>\S+)/$',
        bzCreativeCollectionUpdateView.as_view(), name='business_bzcreativecollection_update'),
)

urlpatterns += (
    # urls for bzCreativeDesign
    url(r'^bzcreativedesign/$', bzCreativeDesignListView.as_view(),
        name='business_bzcreativedesign_list'),
    url(r'^bzcreativedesign/create/$', bzCreativeDesignCreateView.as_view(),
        name='business_bzcreativedesign_create'),
    url(r'^bzcreativedesign/detail/(?P<pk>\S+)/$',
        bzCreativeDesignDetailView.as_view(), name='business_bzcreativedesign_detail'),
    url(r'^bzcreativedesign/update/(?P<pk>\S+)/$',
        bzCreativeDesignUpdateView.as_view(), name='business_bzcreativedesign_update'),
)

urlpatterns += (
    # urls for bzCreativeLayout
    url(r'^bzcreativelayout/$', bzCreativeLayoutListView.as_view(),
        name='business_bzcreativelayout_list'),
    url(r'^bzcreativelayout/create/$', bzCreativeLayoutCreateView.as_view(),
        name='business_bzcreativelayout_create'),
    url(r'^bzcreativelayout/detail/(?P<pk>\S+)/$',
        bzCreativeLayoutDetailView.as_view(), name='business_bzcreativelayout_detail'),
    url(r'^bzcreativelayout/update/(?P<pk>\S+)/$',
        bzCreativeLayoutUpdateView.as_view(), name='business_bzcreativelayout_update'),
)

urlpatterns += (
    # urls for bzCreativeRendering
    url(r'^bzcreativerendering/$', bzCreativeRenderingListView.as_view(),
        name='business_bzcreativerendering_list'),
    url(r'^bzcreativerendering/create/$',
        bzCreativeRenderingCreateView.as_view(), name='business_bzcreativerendering_create'),
    url(r'^bzcreativerendering/detail/(?P<pk>\S+)/$',
        bzCreativeRenderingDetailView.as_view(), name='business_bzcreativerendering_detail'),
    url(r'^bzcreativerendering/update/(?P<pk>\S+)/$',
        bzCreativeRenderingUpdateView.as_view(), name='business_bzcreativerendering_update'),
)

urlpatterns += (
    # urls for bzProduct
    url(r'^bzproduct/$', bzProductListView.as_view(),
        name='business_bzproduct_list'),
    url(r'^bzproduct/create/$', bzProductCreateView.as_view(),
        name='business_bzproduct_create'),
    url(r'^bzproduct/detail/(?P<pk>\S+)/$',
        bzProductDetailView.as_view(), name='business_bzproduct_detail'),
    url(r'^bzproduct/update/(?P<pk>\S+)/$',
        bzProductUpdateView.as_view(), name='business_bzproduct_update'),
)

urlpatterns += (
    # urls for bzProductVariant
    url(r'^bzproductvariant/$', bzProductVariantListView.as_view(),
        name='business_bzproductvariant_list'),
    url(r'^bzproductvariant/create/$', bzProductVariantCreateView.as_view(),
        name='business_bzproductvariant_create'),
    url(r'^bzproductvariant/detail/(?P<pk>\S+)/$',
        bzProductVariantDetailView.as_view(), name='business_bzproductvariant_detail'),
    url(r'^bzproductvariant/update/(?P<pk>\S+)/$',
        bzProductVariantUpdateView.as_view(), name='business_bzproductvariant_update'),
)

urlpatterns += (
    # urls for wooAttribute
    url(r'^wooattribute/$', wooAttributeListView.as_view(),
        name='business_wooattribute_list'),
    url(r'^wooattribute/create/$', wooAttributeCreateView.as_view(),
        name='business_wooattribute_create'),
    url(r'^wooattribute/detail/(?P<slug>\S+)/$',
        wooAttributeDetailView.as_view(), name='business_wooattribute_detail'),
    url(r'^wooattribute/update/(?P<slug>\S+)/$',
        wooAttributeUpdateView.as_view(), name='business_wooattribute_update'),
)

urlpatterns += (
    # urls for wooCategory
    url(r'^woocategory/$', wooCategoryListView.as_view(),
        name='business_woocategory_list'),
    url(r'^woocategory/create/$', wooCategoryCreateView.as_view(),
        name='business_woocategory_create'),
    url(r'^woocategory/detail/(?P<slug>\S+)/$',
        wooCategoryDetailView.as_view(), name='business_woocategory_detail'),
    url(r'^woocategory/update/(?P<slug>\S+)/$',
        wooCategoryUpdateView.as_view(), name='business_woocategory_update'),
)

urlpatterns += (
    # urls for wooImage
    url(r'^wooimage/$', wooImageListView.as_view(), name='business_wooimage_list'),
    url(r'^wooimage/create/$', wooImageCreateView.as_view(),
        name='business_wooimage_create'),
    url(r'^wooimage/detail/(?P<pk>\S+)/$',
        wooImageDetailView.as_view(), name='business_wooimage_detail'),
    url(r'^wooimage/update/(?P<pk>\S+)/$',
        wooImageUpdateView.as_view(), name='business_wooimage_update'),
)

urlpatterns += (
    # urls for wooProduct
    url(r'^wooproduct/$', wooProductListView.as_view(),
        name='business_wooproduct_list'),
    url(r'^wooproduct/create/$', wooProductCreateView.as_view(),
        name='business_wooproduct_create'),
    url(r'^wooproduct/detail/(?P<slug>\S+)/$',
        wooProductDetailView.as_view(), name='business_wooproduct_detail'),
    url(r'^wooproduct/update/(?P<slug>\S+)/$',
        wooProductUpdateView.as_view(), name='business_wooproduct_update'),
)

urlpatterns += (
    # urls for wooShippingClass
    url(r'^wooshippingclass/$', wooShippingClassListView.as_view(),
        name='business_wooshippingclass_list'),
    url(r'^wooshippingclass/create/$', wooShippingClassCreateView.as_view(),
        name='business_wooshippingclass_create'),
    url(r'^wooshippingclass/detail/(?P<slug>\S+)/$',
        wooShippingClassDetailView.as_view(), name='business_wooshippingclass_detail'),
    url(r'^wooshippingclass/update/(?P<slug>\S+)/$',
        wooShippingClassUpdateView.as_view(), name='business_wooshippingclass_update'),
)

urlpatterns += (
    # urls for wooStore
    url(r'^woostore/$', wooStoreListView.as_view(), name='business_woostore_list'),
    url(r'^woostore/create/$', wooStoreCreateView.as_view(),
        name='business_woostore_create'),
    url(r'^woostore/detail/(?P<pk>\S+)/$',
        wooStoreDetailView.as_view(), name='business_woostore_detail'),
    url(r'^woostore/update/(?P<pk>\S+)/$',
        wooStoreUpdateView.as_view(), name='business_woostore_update'),
)

urlpatterns += (
    # urls for wooTag
    url(r'^wootag/$', wooTagListView.as_view(), name='business_wootag_list'),
    url(r'^wootag/create/$', wooTagCreateView.as_view(),
        name='business_wootag_create'),
    url(r'^wootag/detail/(?P<slug>\S+)/$',
        wooTagDetailView.as_view(), name='business_wootag_detail'),
    url(r'^wootag/update/(?P<slug>\S+)/$',
        wooTagUpdateView.as_view(), name='business_wootag_update'),
)

urlpatterns += (
    # urls for wooTerm
    url(r'^wooterm/$', wooTermListView.as_view(), name='business_wooterm_list'),
    url(r'^wooterm/create/$', wooTermCreateView.as_view(),
        name='business_wooterm_create'),
    url(r'^wooterm/detail/(?P<slug>\S+)/$',
        wooTermDetailView.as_view(), name='business_wooterm_detail'),
    url(r'^wooterm/update/(?P<slug>\S+)/$',
        wooTermUpdateView.as_view(), name='business_wooterm_update'),
)

urlpatterns += (
    # urls for wooVariant
    url(r'^woovariant/$', wooVariantListView.as_view(),
        name='business_woovariant_list'),
    url(r'^woovariant/create/$', wooVariantCreateView.as_view(),
        name='business_woovariant_create'),
    url(r'^woovariant/detail/(?P<pk>\S+)/$',
        wooVariantDetailView.as_view(), name='business_woovariant_detail'),
    url(r'^woovariant/update/(?P<pk>\S+)/$',
        wooVariantUpdateView.as_view(), name='business_woovariant_update'),
)

urlpatterns += (
    # urls for wpMedia
    url(r'^wpmedia/$', wpMediaListView.as_view(), name='business_wpmedia_list'),
    url(r'^wpmedia/create/$', wpMediaCreateView.as_view(),
        name='business_wpmedia_create'),
    url(r'^wpmedia/detail/(?P<slug>\S+)/$',
        wpMediaDetailView.as_view(), name='business_wpmedia_detail'),
    url(r'^wpmedia/update/(?P<slug>\S+)/$',
        wpMediaUpdateView.as_view(), name='business_wpmedia_update'),
)

urlpatterns += (
    # urls for wpMediaSize
    url(r'^wpmediasize/$', wpMediaSizeListView.as_view(),
        name='business_wpmediasize_list'),
    url(r'^wpmediasize/create/$', wpMediaSizeCreateView.as_view(),
        name='business_wpmediasize_create'),
    url(r'^wpmediasize/detail/(?P<pk>\S+)/$',
        wpMediaSizeDetailView.as_view(), name='business_wpmediasize_detail'),
    url(r'^wpmediasize/update/(?P<pk>\S+)/$',
        wpMediaSizeUpdateView.as_view(), name='business_wpmediasize_update'),
)

urlpatterns += (
    # urls for pfCountry
    url(r'^pfcountry/$', pfCountryListView.as_view(),
        name='business_pfcountry_list'),
    url(r'^pfcountry/create/$', pfCountryCreateView.as_view(),
        name='business_pfcountry_create'),
    url(r'^pfcountry/detail/(?P<pk>\S+)/$',
        pfCountryDetailView.as_view(), name='business_pfcountry_detail'),
    url(r'^pfcountry/update/(?P<pk>\S+)/$',
        pfCountryUpdateView.as_view(), name='business_pfcountry_update'),
)

urlpatterns += (
    # urls for pfState
    url(r'^pfstate/$', pfStateListView.as_view(), name='business_pfstate_list'),
    url(r'^pfstate/create/$', pfStateCreateView.as_view(),
        name='business_pfstate_create'),
    url(r'^pfstate/detail/(?P<pk>\S+)/$',
        pfStateDetailView.as_view(), name='business_pfstate_detail'),
    url(r'^pfstate/update/(?P<pk>\S+)/$',
        pfStateUpdateView.as_view(), name='business_pfstate_update'),
)

urlpatterns += (
    # urls for pfSyncProduct
    url(r'^pfsyncproduct/$', pfSyncProductListView.as_view(),
        name='business_pfsyncproduct_list'),
    url(r'^pfsyncproduct/create/$', pfSyncProductCreateView.as_view(),
        name='business_pfsyncproduct_create'),
    url(r'^pfsyncproduct/detail/(?P<pk>\S+)/$',
        pfSyncProductDetailView.as_view(), name='business_pfsyncproduct_detail'),
    url(r'^pfsyncproduct/update/(?P<pk>\S+)/$',
        pfSyncProductUpdateView.as_view(), name='business_pfsyncproduct_update'),
)

urlpatterns += (
    # urls for pfSyncVariant
    url(r'^pfsyncvariant/$', pfSyncVariantListView.as_view(),
        name='business_pfsyncvariant_list'),
    url(r'^pfsyncvariant/create/$', pfSyncVariantCreateView.as_view(),
        name='business_pfsyncvariant_create'),
    url(r'^pfsyncvariant/detail/(?P<pk>\S+)/$',
        pfSyncVariantDetailView.as_view(), name='business_pfsyncvariant_detail'),
    url(r'^pfsyncvariant/update/(?P<pk>\S+)/$',
        pfSyncVariantUpdateView.as_view(), name='business_pfsyncvariant_update'),
)

urlpatterns += (
    # urls for pfSyncItemOption
    url(r'^pfsyncitemoption/$', pfSyncItemOptionListView.as_view(),
        name='business_pfsyncitemoption_list'),
    url(r'^pfsyncitemoption/create/$', pfSyncItemOptionCreateView.as_view(),
        name='business_pfsyncitemoption_create'),
    url(r'^pfsyncitemoption/detail/(?P<pk>\S+)/$',
        pfSyncItemOptionDetailView.as_view(), name='business_pfsyncitemoption_detail'),
    url(r'^pfsyncitemoption/update/(?P<pk>\S+)/$',
        pfSyncItemOptionUpdateView.as_view(), name='business_pfsyncitemoption_update'),
)

urlpatterns += (
    # urls for pfCatalogColor
    url(r'^pfcatalogcolor/$', pfCatalogColorListView.as_view(),
        name='business_pfcatalogcolor_list'),
    url(r'^pfcatalogcolor/create/$', pfCatalogColorCreateView.as_view(),
        name='business_pfcatalogcolor_create'),
    url(r'^pfcatalogcolor/detail/(?P<pk>\S+)/$',
        pfCatalogColorDetailView.as_view(), name='business_pfcatalogcolor_detail'),
    url(r'^pfcatalogcolor/update/(?P<pk>\S+)/$',
        pfCatalogColorUpdateView.as_view(), name='business_pfcatalogcolor_update'),
)

urlpatterns += (
    # urls for pfCatalogSize
    url(r'^pfcatalogsize/$', pfCatalogSizeListView.as_view(),
        name='business_pfcatalogsize_list'),
    url(r'^pfcatalogsize/create/$', pfCatalogSizeCreateView.as_view(),
        name='business_pfcatalogsize_create'),
    url(r'^pfcatalogsize/detail/(?P<pk>\S+)/$',
        pfCatalogSizeDetailView.as_view(), name='business_pfcatalogsize_detail'),
    url(r'^pfcatalogsize/update/(?P<pk>\S+)/$',
        pfCatalogSizeUpdateView.as_view(), name='business_pfcatalogsize_update'),
)

urlpatterns += (
    # urls for pfCatalogFileSpec
    url(r'^pfcatalogfilespec/$', pfCatalogFileSpecListView.as_view(),
        name='business_pfcatalogfilespec_list'),
    url(r'^pfcatalogfilespec/create/$', pfCatalogFileSpecCreateView.as_view(),
        name='business_pfcatalogfilespec_create'),
    url(r'^pfcatalogfilespec/detail/(?P<pk>\S+)/$',
        pfCatalogFileSpecDetailView.as_view(), name='business_pfcatalogfilespec_detail'),
    url(r'^pfcatalogfilespec/update/(?P<pk>\S+)/$',
        pfCatalogFileSpecUpdateView.as_view(), name='business_pfcatalogfilespec_update'),
)

urlpatterns += (
    # urls for pfCatalogFileType
    url(r'^pfcatalogfiletype/$', pfCatalogFileTypeListView.as_view(),
        name='business_pfcatalogfiletype_list'),
    url(r'^pfcatalogfiletype/create/$', pfCatalogFileTypeCreateView.as_view(),
        name='business_pfcatalogfiletype_create'),
    url(r'^pfcatalogfiletype/detail/(?P<pk>\S+)/$',
        pfCatalogFileTypeDetailView.as_view(), name='business_pfcatalogfiletype_detail'),
    url(r'^pfcatalogfiletype/update/(?P<pk>\S+)/$',
        pfCatalogFileTypeUpdateView.as_view(), name='business_pfcatalogfiletype_update'),
)

urlpatterns += (
    # urls for pfCatalogOptionType
    url(r'^pfcatalogoptiontype/$', pfCatalogOptionTypeListView.as_view(),
        name='business_pfcatalogoptiontype_list'),
    url(r'^pfcatalogoptiontype/create/$',
        pfCatalogOptionTypeCreateView.as_view(), name='business_pfcatalogoptiontype_create'),
    url(r'^pfcatalogoptiontype/detail/(?P<pk>\S+)/$',
        pfCatalogOptionTypeDetailView.as_view(), name='business_pfcatalogoptiontype_detail'),
    url(r'^pfcatalogoptiontype/update/(?P<pk>\S+)/$',
        pfCatalogOptionTypeUpdateView.as_view(), name='business_pfcatalogoptiontype_update'),
)

urlpatterns += (
    # urls for pfCatalogProduct
    url(r'^pfcatalogproduct/$', pfCatalogProductListView.as_view(),
        name='business_pfcatalogproduct_list'),
    url(r'^pfcatalogproduct/create/$', pfCatalogProductCreateView.as_view(),
        name='business_pfcatalogproduct_create'),
    url(r'^pfcatalogproduct/detail/(?P<pk>\S+)/$',
        pfCatalogProductDetailView.as_view(), name='business_pfcatalogproduct_detail'),
    url(r'^pfcatalogproduct/update/(?P<pk>\S+)/$',
        pfCatalogProductUpdateView.as_view(), name='business_pfcatalogproduct_update'),
)

urlpatterns += (
    # urls for pfCatalogVariant
    url(r'^pfcatalogvariant/$', pfCatalogVariantListView.as_view(),
        name='business_pfcatalogvariant_list'),
    url(r'^pfcatalogvariant/create/$', pfCatalogVariantCreateView.as_view(),
        name='business_pfcatalogvariant_create'),
    url(r'^pfcatalogvariant/detail/(?P<pk>\S+)/$',
        pfCatalogVariantDetailView.as_view(), name='business_pfcatalogvariant_detail'),
    url(r'^pfcatalogvariant/update/(?P<pk>\S+)/$',
        pfCatalogVariantUpdateView.as_view(), name='business_pfcatalogvariant_update'),
)

urlpatterns += (
    # urls for pfStore
    url(r'^pfstore/$', pfStoreListView.as_view(), name='business_pfstore_list'),
    url(r'^pfstore/create/$', pfStoreCreateView.as_view(),
        name='business_pfstore_create'),
    url(r'^pfstore/detail/(?P<pk>\S+)/$',
        pfStoreDetailView.as_view(), name='business_pfstore_detail'),
    url(r'^pfstore/update/(?P<pk>\S+)/$',
        pfStoreUpdateView.as_view(), name='business_pfstore_update'),
)

urlpatterns += (
    # urls for pfPrintFile
    url(r'^pfprintfile/$', pfPrintFileListView.as_view(),
        name='business_pfprintfile_list'),
    url(r'^pfprintfile/create/$', pfPrintFileCreateView.as_view(),
        name='business_pfprintfile_create'),
    url(r'^pfprintfile/detail/(?P<pk>\S+)/$',
        pfPrintFileDetailView.as_view(), name='business_pfprintfile_detail'),
    url(r'^pfprintfile/update/(?P<pk>\S+)/$',
        pfPrintFileUpdateView.as_view(), name='business_pfprintfile_update'),
)
