from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import RedirectView

from django_tables2 import *

from business.models import *
from business.forms import *
from business.tables import *

from business.helper_backend import commonListView, commonUpdateView, commonCreateView


class appListCommonListView(commonListView):
    active_app = 'lists'
    active_apptitle = 'List Management'
    object_icon = 'list'


class appListCommonUpdateView(commonUpdateView):
    active_app = 'lists'
    active_apptitle = 'List Management'
    object_icon = 'list'


class appListCommonCreateView(commonCreateView):
    active_app = 'lists'
    active_apptitle = 'List Management'
    object_icon = 'list'

 # App List


class appListsHome(View):
    def get(self, request):
        return redirect(reverse('business:app_list_cprod_list'))

# All List Geo


class appListGeoList(appListCommonListView):
    model = pfCountry
    table_class = pfCountryTable
    object_name = "Geographies"


class appListGeoDetail(TemplateView):
    pass


class appListGeoPull(View):
    pass

# App List Colour


class appListColorList(appListCommonListView):
    model = pfCatalogColor
    table_class = pfCatalogColorTable
    object_name = "Colour"


class appListColorUpdate(appListCommonUpdateView):
    model = pfCatalogColor
    form_class = pfCatalogColorForm
    object_name = "Colour"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_color_list")
    action_list = reverse_lazy("business:app_list_color_list")


class appListSizeList(appListCommonListView):
    model = pfCatalogSize
    table_class = pfCatalogSizeTable
    object_name = "Size"


class appListSizeUpdate(UpdateView):
    pass


class appListFileSpecList(appListCommonListView):
    model = pfCatalogFileSpec
    table_class = pfCatalogFileSpecTable
    object_name = "File Specification"


class appListFileSpecCreate(CreateView):
    pass


class appListFileSpecUpdate(UpdateView):
    pass


class appListShippingList(appListCommonListView):
    model = wooShippingClass
    table_class = wooShippingClassTable
    object_name = "Shipping Class"


class appListShippingCreate(CreateView):
    pass


class appListShippingUpdate(UpdateView):
    pass


class appListShippingPush(View):
    pass


class appListShippingPull(View):
    pass


class appListCategoryList(appListCommonListView):
    model = wooCategory
    table_class = wooCategoryTable
    object_name = "Product Category"


class appListCategoryCreate(CreateView):
    pass


class appListCategoryUpdate(UpdateView):
    pass


class appListCategoryPush(View):
    pass


class appListCategoryPull(View):
    pass


class appListTagList(appListCommonListView):
    model = wooTag
    table_class = wooTagTable
    object_name = "Product Tag"


class appListTagCreate(CreateView):
    pass


class appListTagUpdate(UpdateView):
    pass


class appListTagPush(View):
    pass


class appListTagPull(View):
    pass


class appListCatProductList(appListCommonListView):
    model = pfCatalogProduct
    table_class = pfCatalogProduct
    object_name = "Catalog Product"


class appListCatProductUpdate(UpdateView):
    pass


class appListAttributeList(appListCommonListView):
    model = wooAttribute
    table_class = wooAttributeTable
    object_name = "Product Attribute"


class appListAttributeUpdate(UpdateView):
    pass
