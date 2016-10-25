from django.conf.urls import url, include
from printaura import views

urlpatterns = (
    url(r'^$', views.HomeView, name="printaura_home"),
    # url(r'^local-product-group/$', views.LocalProductGroupListView, name='printaura_lpg_list'),
    url(r'^local-product-group/(?P<slug>\S+)/$', views.LPGDetailView, name='printaura_lpg_detail'),

    url(r'^product/(?P<slug>\S+)/$', views.ProductDetailView, name='printaura_product_detail'),

    url(r'^brand/(?P<slug>\S+)/$', views.BrandDetailView, name='printaura_brand_detail'),

)
