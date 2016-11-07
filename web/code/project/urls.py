"""
project URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from master.views import Global_Home

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^vendor/printaura/', include('printaura.urls')),
    # url(r'^vendor/printful/', include('printful.urls')),

    url(r'^', include('master.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
