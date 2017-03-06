from django.core.urlresolvers import reverse, reverse_lazy

from django.http import HttpResponse

from django.shortcuts import render

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from django_tables2 import *

from business.models import *
from business.forms import *
from business.tables import *


class appProductHome(TemplateView):
    template_name = "app_product/home.html"

    def get_context_data(self, **kwargs):
        context = super(appProductHome, self).get_context_data(**kwargs)
        context['active_app'] = "product"
        context['active_apptitle'] = "Product Catalog"
        context['products'] = bzProduct.objects.all()
        if context['products']:
            context['active_product'] = context['products'][0]
            context['table_variants'] = bzProductVariantTable(
                bzProductVariant.objects.filter(
                    bzproduct=context['active_product'])
            )
        # TODO Do we need an else here?

        return context


class appProductDetail(TemplateView):
    template_name = "app_product/product_detail.html"
    model = bzProduct


class appProductCreate(CreateView):
    model = bzProduct
    form_class = bzProductForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_product_home')

    def get_context_data(self, **kwargs):
        context = super(appProductCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "product"
        context['object_name'] = "Product"
        context['active_apptitle'] = "Product Catalog"
        context['action_list'] = reverse('business:app_product_home')
        return context


class appProductUpdate(UpdateView):
    model = bzProduct
    form_class = bzProductForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_product_home')

    def get_context_data(self, **kwargs):
        context = super(appProductUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "product"
        context['object_name'] = "Product"
        context['active_apptitle'] = "Product Catalog"
        context['action_list'] = reverse('business:app_product_home')
        return context
