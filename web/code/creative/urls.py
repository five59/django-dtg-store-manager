from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.Dashboard_list, name='Dashboard_list'),
    # url(r'^dashboard/(?P<id>[^/]+)/$',
    #     views.Dashboard_detail, name='Dashboard_detail'),
]
