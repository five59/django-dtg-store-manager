from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from django_tables2 import *

from business.models import *
from business.forms import *
from business.tables import *


class appStoreHome(View):
    def get(self, request):
        return redirect(reverse('business:app_store_brand_list'))


class appStoreBrandList(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(appStoreBrandList, self).get_context_data(**kwargs)
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Brands"
        context['action_new'] = reverse('business:app_store_brand_create')
        context['table'] = bzBrandTable(bzBrand.objects.all())
        return context


class appStoreBrandDetail(TemplateView):
    template_name = "app_store/brand_detail.html"
    model = bzBrand


class appStoreBrandCreate(CreateView):
    model = bzBrand
    form_class = bzBrandForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_brand_list')

    def get_context_data(self, **kwargs):
        context = super(appStoreBrandCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "store"
        context['object_name'] = "Collection"
        context['active_apptitle'] = "Store Management"
        context['action_list'] = reverse('business:app_store_brand_list')
        return context


class appStoreBrandUpdate(UpdateView):
    model = bzBrand
    form_class = bzBrandForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_brand_list')

    def get_context_data(self, **kwargs):
        context = super(appStoreBrandUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "store"
        context['object_name'] = "Collection"
        context['active_apptitle'] = "Store Management"
        context['action_list'] = reverse('business:app_store_brand_list')
        return context
