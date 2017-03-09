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


class appListSizeUpdate(appListCommonUpdateView):
    model = pfCatalogSize
    form_class = pfCatalogSizeForm
    object_name = "Size"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_size_list")
    action_list = success_url


class appListFileSpecList(appListCommonListView):
    model = pfCatalogFileSpec
    table_class = pfCatalogFileSpecTable
    object_name = "File Specification"
    action_new = reverse_lazy("business:app_list_filespec_create")


class appListFileSpecCreate(appListCommonCreateView):
    model = pfCatalogFileSpec
    form_class = pfCatalogFileSpecForm
    object_name = "File Spec"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_filespec_list")
    action_list = reverse_lazy("business:app_list_filespec_list")


class appListFileSpecUpdate(appListCommonUpdateView):
    model = pfCatalogFileSpec
    form_class = pfCatalogFileSpecForm
    object_name = "File Spec"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_filespec_list")
    action_list = reverse_lazy("business:app_list_filespec_list")


class appListShippingList(appListCommonListView):
    model = wooShippingClass
    table_class = wooShippingClassTable
    object_name = "Shipping Class"
    action_new = reverse_lazy("business:app_list_shipping_create")


class appListShippingCreate(appListCommonCreateView):
    model = wooShippingClass
    form_class = wooShippingClassForm
    object_name = "Shipping Class"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_shipping_list")
    action_list = reverse_lazy("business:app_list_shipping_list")


class appListShippingUpdate(appListCommonUpdateView):
    model = wooShippingClass
    form_class = wooShippingClassTable
    object_name = "Shipping Class"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_shipping_list")
    action_list = reverse_lazy("business:app_list_shipping_list")


class appListShippingPush(View):
    pass


class appListShippingPull(View):
    pass


class appListCategoryList(appListCommonListView):
    model = wooCategory
    table_class = wooCategoryTable
    object_name = "Product Category"
    action_new = reverse_lazy("business:app_list_category_create")


class appListCategoryCreate(appListCommonCreateView):
    model = wooCategory
    form_class = wooCategoryForm
    object_name = "Product Category"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_category_list")
    action_list = reverse_lazy("business:app_list_category_list")


class appListCategoryUpdate(appListCommonUpdateView):
    model = wooCategory
    form_class = wooCategoryForm
    object_name = "Product Category"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_category_list")
    action_list = reverse_lazy("business:app_list_category_list")


class appListCategoryPush(View):
    pass


class appListCategoryPull(View):
    pass


class appListTagList(appListCommonListView):
    model = wooTag
    table_class = wooTagTable
    object_name = "Product Tag"
    action_new = reverse_lazy("business:app_list_tag_createeeeee")


class appListTagCreate(appListCommonCreateView):
    model = wooTag
    form_class = wooTagForm
    object_name = "Product Tag"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_tag_list")
    action_list = reverse_lazy("business:app_list_tag_list")


class appListTagUpdate(appListCommonUpdateView):
    model = wooTag
    form_class = wooTagForm
    object_name = "Product Tag"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_tag_list")
    action_list = reverse_lazy("business:app_list_tag_list")


class appListTagPush(View):
    pass


class appListTagPull(View):
    pass


class appListCatProductList(appListCommonListView):
    model = pfCatalogProduct
    table_class = pfCatalogProductTable
    object_name = "Catalog Product"


class appListCatProductUpdate(appListCommonUpdateView):
    model = pfCatalogProduct
    form_class = pfCatalogProductForm
    object_name = "Catalog Product"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_cprod_list")
    action_list = reverse_lazy("business:app_list_cprod_list")


class appListAttributeList(appListCommonListView):
    model = wooAttribute
    table_class = wooAttributeTable
    object_name = "Product Attribute"


class appListAttributeUpdate(appListCommonUpdateView):
    model = wooAttribute
    form_class = wooAttributeForm
    object_name = "Product Attribute"
    object_icon = ""
    success_url = reverse_lazy("business:app_list_attribute_list")
    action_list = reverse_lazy("business:app_list_attribute_list")
