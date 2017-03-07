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


class appStoreBrandDetail(DetailView):
    template_name = "app_store/brand_detail.html"
    model = bzBrand

    def get_context_data(self, **kwargs):
        context = super(appStoreBrandDetail, self).get_context_data(**kwargs)
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Brands"
        return context


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
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Brands"
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
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Brands"
        context['action_list'] = reverse('business:app_store_brand_list')
        return context


class appStorePFList(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(appStorePFList, self).get_context_data(**kwargs)
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Printful Stores"
        context['action_new'] = reverse('business:app_store_pf_create')
        context['table'] = pfStoreTable(pfStore.objects.all())
        return context


class appStorePFDetail(DetailView):
    template_name = "app_store/pf_detail.html"
    model = pfStore

    def get_context_data(self, **kwargs):
        context = super(appStorePFDetail, self).get_context_data(**kwargs)
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Printful Stores"
        return context


class appStorePFCreate(CreateView):
    model = pfStore
    form_class = pfStoreForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_pf_list')

    def get_context_data(self, **kwargs):
        context = super(appStorePFCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Printful Stores"
        context['action_list'] = reverse('business:app_store_pf_list')
        return context


class appStorePFUpdate(UpdateView):
    model = pfStore
    form_class = pfStoreForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_pf_list')

    def get_context_data(self, **kwargs):
        context = super(appStorePFUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Printful Stores"
        context['action_list'] = reverse('business:app_store_pf_list')
        return context


class appStoreWPList(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(appStoreWPList, self).get_context_data(**kwargs)
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "WordPress Sites"
        context['action_new'] = reverse('business:app_store_wp_create')
        context['table'] = wooStoreTable(wooStore.objects.all())
        return context


class appStoreWPDetail(DetailView):
    template_name = "app_store/wp_detail.html"
    model = wooStore

    def get_context_data(self, **kwargs):
        context = super(appStoreWPDetail, self).get_context_data(**kwargs)
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "WordPress Sites"
        return context


class appStoreWPCreate(CreateView):
    model = wooStore
    form_class = wooStoreForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_wp_list')

    def get_context_data(self, **kwargs):
        context = super(appStoreWPCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "WordPress Sites"
        context['action_list'] = reverse('business:app_store_wp_list')
        return context


class appStoreWPUpdate(UpdateView):
    model = wooStore
    form_class = wooStoreForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_wp_list')

    def get_context_data(self, **kwargs):
        context = super(appStoreWPUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "WordPress Sites"
        context['action_list'] = reverse('business:app_store_wp_list')
        return context
