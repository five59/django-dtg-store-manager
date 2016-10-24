from django.conf.urls import url, include
from printaura import views

urlpatterns = (
    url(r'^$', views.HomeView, name="printaura_home"),
)
