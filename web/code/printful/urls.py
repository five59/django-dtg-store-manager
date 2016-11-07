from django.conf.urls import url, include
from printful import views

urlpatterns = (
    url(r'^', views.Home, name='printful_home'),
    # url(r'^product', views.Product_List, name='printful_product_list'),
)
