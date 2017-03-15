from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from django.shortcuts import render

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from django_tables2 import *

from business.models import *
from business.forms import *
from business.tables import *

from business.helper_backend import commonListView


class appProductCommonListView(commonListView):
    active_app = 'product'
    active_apptitle = 'Product Catalog'
    object_icon = 'sunglasses'


class appProductCommonUpdateView(commonUpdateView):
    active_app = 'product'
    active_apptitle = 'Product Catalog'
    object_icon = 'sunglasses'


class appProductCommonCreateView(commonCreateView):
    active_app = 'product'
    active_apptitle = 'Product Catalog'
    object_icon = 'sunglasses'


class appProductHome(TemplateView):
    template_name = "app_product/home.html"

    def get_context_data(self, **kwargs):
        context = super(appProductHome, self).get_context_data(**kwargs)
        context['active_app'] = "product"
        context['active_apptitle'] = "Product Catalog"
        context['products'] = bzProduct.objects.all()
        if context['products']:
            try:
                if 'product' in self.kwargs:
                    context['active_product'] = bzProduct.objects.get(
                        pk=self.kwargs['product'])
                else:
                    context['active_product'] = context['products'][0]
            except ObjectDoesNotExist:
                context['active_product'] = context['products'][0]

            context['table_variants'] = bzProductVariantTable(
                bzProductVariant.objects.filter(
                    bzproduct=context['active_product'])
            )

        return context


class appProductDetail(TemplateView):
    template_name = "app_product/product_detail.html"
    model = bzProduct


# class appProductCreate(CreateView):
#     model = bzProduct
#     form_class = bzProductForm
#     template_name = "business/object_form.html"
#     success_url = reverse_lazy('business:app_product_home')
#
#     def get_context_data(self, **kwargs):
#         context = super(appProductCreate,
#                         self).get_context_data(**kwargs)
#         context['mode'] = "create"
#         context['active_app'] = "product"
#         context['object_name'] = "Product"
#         context['active_apptitle'] = "Product Catalog"
#         context['action_list'] = reverse('business:app_product_home')
#         return context


class appProductUpdate(appProductCommonUpdateView):
    model = bzProduct
    form_class = bzProductForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_product_home')

    def get_context_data(self, **kwargs):
        context = super(appProductUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['action_list'] = reverse('business:app_product_home')
        return context
