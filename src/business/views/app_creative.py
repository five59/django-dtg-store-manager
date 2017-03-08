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


class appCreativeHome(TemplateView):
    template_name = "app_creative/home.html"

    def get_context_data(self, **kwargs):
        context = super(appCreativeHome, self).get_context_data(**kwargs)
        context['active_app'] = "creative"
        context['active_apptitle'] = "Creative Management"

        # TODO Incorporate Brand filtering
        # context['brands'] = bzBrand.objects.all()

        context['creativecollections'] = bzCreativeCollection.objects.all()

        # Don't do this if there's no collections.
        if len(context['creativecollections']) > 0:
            if 'collection' in self.kwargs:
                context['active_collection'] = bzCreativeCollection.objects.get(
                    pk=self.kwargs['collection'])
            else:
                context['active_collection'] = context['creativecollections'][0]

        if 'active_collection' in context:
            context['table_designs'] = bzCreativeDesignTable(
                bzCreativeDesign.objects.filter(bzcreativecollection=context['active_collection']))
            context['table_layouts'] = bzCreativeLayoutTable(
                bzCreativeLayout.objects.filter(bzcreativecollection=context['active_collection']))
        else:
            context['table_designs'] = bzCreativeDesignTable(
                bzCreativeDesign.objects.all())
            context['table_layouts'] = bzCreativeLayoutTable(
                bzCreativeLayout.objects.all())

        return context


class appCreativeCollectionDetail(TemplateView):
    template_name = "app_creative/design_detail.html"
    model = bzCreativeCollection


class appCreativeCollectionCreate(CreateView):
    model = bzCreativeCollection
    form_class = bzCreativeCollectionForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_creative_home')

    def get_context_data(self, **kwargs):
        context = super(appCreativeCollectionCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "creative"
        context['object_name'] = "Collection"
        context['active_apptitle'] = "Creative Management"
        context['action_list'] = reverse('business:app_creative_home')
        return context


class appCreativeCollectionUpdate(UpdateView):
    model = bzCreativeCollection
    form_class = bzCreativeCollectionForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_creative_home')

    def get_context_data(self, **kwargs):
        context = super(appCreativeCollectionUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "creative"
        context['object_name'] = "Collection"
        context['active_apptitle'] = "Creative Management"
        context['action_list'] = reverse('business:app_creative_home')
        return context


class appCreativeDesignDetail(TemplateView):
    template_name = "app_creative/design_detail.html"
    model = bzCreativeDesign


class appCreativeDesignCreate(CreateView):
    model = bzCreativeDesign
    form_class = bzCreativeDesignForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_creative_home')

    def get_context_data(self, **kwargs):
        context = super(appCreativeDesignCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "creative"
        context['object_name'] = "Design"
        context['active_apptitle'] = "Creative Management"
        context['action_list'] = reverse('business:app_creative_home')
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(appCreativeDesignCreate, self).get_form_kwargs()
        if 'collection' in self.request.GET:
            try:
                c = bzCreativeCollection.objects.get(
                    pk=self.request.GET['collection'])
                kwargs['initial'] = {
                    'bzcreativecollection': c.pk,
                }
            except Exception as e:
                pass
        return kwargs


class appCreativeDesignUpdate(UpdateView):
    model = bzCreativeDesign
    form_class = bzCreativeDesignForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_creative_home')

    def get_context_data(self, **kwargs):
        context = super(appCreativeDesignUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "creative"
        context['object_name'] = "Design"
        context['active_apptitle'] = "Creative Management"
        context['action_list'] = reverse('business:app_creative_home')
        return context


class appCreativeLayoutDetail(TemplateView):
    template_name = "app_creative/design_detail.html"
    model = bzCreativeLayout


class appCreativeLayoutCreate(CreateView):
    model = bzCreativeLayout
    form_class = bzCreativeLayoutForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_creative_home')

    def get_context_data(self, **kwargs):
        context = super(appCreativeLayoutCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "creative"
        context['object_name'] = "Layout"
        context['active_apptitle'] = "Creative Management"
        context['action_list'] = reverse('business:app_creative_home')
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(appCreativeLayoutCreate, self).get_form_kwargs()
        if 'collection' in self.request.GET:
            try:
                c = bzCreativeCollection.objects.get(
                    pk=self.request.GET['collection'])
                kwargs['initial'] = {
                    'bzcreativecollection': c.pk,
                }
            except Exception as e:
                pass
        return kwargs


class appCreativeLayoutUpdate(UpdateView):
    model = bzCreativeLayout
    form_class = bzCreativeLayoutForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_creative_home')

    def get_context_data(self, **kwargs):
        context = super(appCreativeLayoutUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['object_name'] = "Layout"
        context['active_app'] = "creative"
        context['active_apptitle'] = "Creative Management"
        context['action_list'] = reverse('business:app_creative_home')
        return context
