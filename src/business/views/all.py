from django.core.urlresolvers import reverse

from django.http import HttpResponse

from django.shortcuts import render

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from django_tables2 import *

from business.models import *
from business.forms import *
from business.tables import *


class bzHomeView(TemplateView):
    template_name = "home.html"


class bzBrandListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(bzBrandListView, self).get_context_data(**kwargs)
        context['table'] = bzBrandTable(bzBrand.objects.all())
        context['object_name'] = "Brand"
        context['object_group'] = "stores"
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_bzbrand_create')
        return context


class bzBrandCreateView(CreateView):
    model = bzBrand
    form_class = bzBrandForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzBrandCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Brand"
        context['object_group'] = "stores"
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_bzbrand_list')
        return context


class bzBrandDetailView(DetailView):
    model = bzBrand
    template_name = "business/bz/bzbrand_detail.html"


class bzBrandUpdateView(UpdateView):
    model = bzBrand
    form_class = bzBrandForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzBrandUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Brand"
        context['object_group'] = "stores"
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_bzbrand_list')
        return context


class bzCreativeCollectionListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeCollectionListView,
                        self).get_context_data(**kwargs)
        context['table'] = bzCreativeCollectionTable(
            bzCreativeCollection.objects.all())
        context['object_name'] = "Creative Collection"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_bzcreativecollection_create')
        return context


class bzCreativeCollectionCreateView(CreateView):
    model = bzCreativeCollection
    form_class = bzCreativeCollectionForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeCollectionCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Creative Collection"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzcreativecollection_list')
        return context


class bzCreativeCollectionDetailView(DetailView):
    model = bzCreativeCollection
    template_name = "business/bz/bzcreativecollection_detail.html"


class bzCreativeCollectionUpdateView(UpdateView):
    model = bzCreativeCollection
    form_class = bzCreativeCollectionForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeCollectionUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Creative Collection"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzcreativecollection_list')
        return context


class bzCreativeDesignListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeDesignListView,
                        self).get_context_data(**kwargs)
        context['table'] = bzCreativeDesignTable(
            bzCreativeDesign.objects.all())
        context['object_name'] = "Creative Design"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_bzcreativedesign_create')
        return context


class bzCreativeDesignCreateView(CreateView):
    model = bzCreativeDesign
    form_class = bzCreativeDesignForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeDesignCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Creative Design"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzcreativedesign_list')
        return context


class bzCreativeDesignDetailView(DetailView):
    model = bzCreativeDesign
    template_name = "business/bz/bzcreativedesign_detail.html"


class bzCreativeDesignUpdateView(UpdateView):
    model = bzCreativeDesign
    form_class = bzCreativeDesignForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeDesignUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Creative Design"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzcreativedesign_list')
        return context


class bzCreativeLayoutListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeLayoutListView,
                        self).get_context_data(**kwargs)
        context['table'] = bzCreativeLayoutTable(
            bzCreativeLayout.objects.all())
        context['object_name'] = "Creative Layout"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_bzcreativelayout_create')
        return context


class bzCreativeLayoutCreateView(CreateView):
    model = bzCreativeLayout
    form_class = bzCreativeLayoutForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeLayoutCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Creative Layout"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzcreativelayout_list')
        return context


class bzCreativeLayoutDetailView(DetailView):
    model = bzCreativeLayout
    template_name = "business/bz/bzcreativelayout_detail.html"


class bzCreativeLayoutUpdateView(UpdateView):
    model = bzCreativeLayout
    form_class = bzCreativeLayoutForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeLayoutUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Creative Layout"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzcreativelayout_list')
        return context


class bzCreativeRenderingListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeRenderingListView,
                        self).get_context_data(**kwargs)
        context['table'] = bzCreativeRenderingTable(
            bzCreativeRendering.objects.all())
        context['object_name'] = "Creative Rendering"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_bzcreativerendering_create')
        return context


class bzCreativeRenderingCreateView(CreateView):
    model = bzCreativeRendering
    form_class = bzCreativeRenderingForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeRenderingCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Creative Rendering"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzcreativerendering_list')
        return context


class bzCreativeRenderingDetailView(DetailView):
    model = bzCreativeRendering
    template_name = "business/bz/bzcreativerendering_detail.html"


class bzCreativeRenderingUpdateView(UpdateView):
    model = bzCreativeRendering
    form_class = bzCreativeRenderingForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzCreativeRenderingUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Creative Rendering"
        context['object_group'] = "creative"
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzcreativerendering_list')
        return context


class bzProductListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(bzProductListView, self).get_context_data(**kwargs)
        context['table'] = bzProductTable(bzProduct.objects.all())
        context['object_name'] = "Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_bzproduct_create')
        return context


class bzProductCreateView(CreateView):
    model = bzProduct
    form_class = bzProductForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzProductCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_bzproduct_list')
        return context


class bzProductDetailView(DetailView):
    model = bzProduct
    template_name = "business/bz/bzproduct_detail.html"


class bzProductUpdateView(UpdateView):
    model = bzProduct
    form_class = bzProductForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzProductUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_bzproduct_list')
        return context


class bzProductVariantListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(bzProductVariantListView,
                        self).get_context_data(**kwargs)
        context['table'] = bzProductVariantTable(
            bzProductVariant.objects.all())
        context['object_name'] = "Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_bzproductvariant_create')
        return context


class bzProductVariantCreateView(CreateView):
    model = bzProductVariant
    form_class = bzProductVariantForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzProductVariantCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzproductvariant_list')
        return context


class bzProductVariantDetailView(DetailView):
    model = bzProductVariant
    template_name = "business/bz/bzproductvariant_detail.html"


class bzProductVariantUpdateView(UpdateView):
    model = bzProductVariant
    form_class = bzProductVariantForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(bzProductVariantUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_bzproductvariant_list')
        return context


class pfCatalogColorListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogColorListView,
                        self).get_context_data(**kwargs)
        context['table'] = pfCatalogColorTable(pfCatalogColor.objects.all())
        context['object_name'] = "Printful Color"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfcatalogcolor_create')
        return context


class pfCatalogColorCreateView(CreateView):
    model = pfCatalogColor
    form_class = pfCatalogColorForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogColorCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Color"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogcolor_list')
        return context


class pfCatalogColorDetailView(DetailView):
    model = pfCatalogColor
    template_name = "business/pf/pfcatalogcolor_detail.html"


class pfCatalogColorUpdateView(UpdateView):
    model = pfCatalogColor
    form_class = pfCatalogColorForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogColorUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Color"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogcolor_list')
        return context


class pfCatalogFileSpecListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogFileSpecListView,
                        self).get_context_data(**kwargs)
        context['table'] = pfCatalogFileSpecTable(
            pfCatalogFileSpec.objects.all())
        context['object_name'] = "Printful File Spec"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfcatalogfilespec_create')
        return context


class pfCatalogFileSpecCreateView(CreateView):
    model = pfCatalogFileSpec
    form_class = pfCatalogFileSpecForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogFileSpecCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful File Spec"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogfilespec_list')
        return context


class pfCatalogFileSpecDetailView(DetailView):
    model = pfCatalogFileSpec
    template_name = "business/pf/pfcatalogfilespec_detail.html"


class pfCatalogFileSpecUpdateView(UpdateView):
    model = pfCatalogFileSpec
    form_class = pfCatalogFileSpecForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogFileSpecUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful File Spec"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogfilespec_list')
        return context


class pfCatalogFileTypeListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogFileTypeListView,
                        self).get_context_data(**kwargs)
        context['table'] = pfCatalogFileTypeTable(
            pfCatalogFileType.objects.all())
        context['object_name'] = "Printful File Type"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfcatalogfiletype_create')
        return context


class pfCatalogFileTypeCreateView(CreateView):
    model = pfCatalogFileType
    form_class = pfCatalogFileTypeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogFileTypeCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful File Type"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogfiletype_list')
        return context


class pfCatalogFileTypeDetailView(DetailView):
    model = pfCatalogFileType
    template_name = "business/pf/pfcatalogfiletype_detail.html"


class pfCatalogFileTypeUpdateView(UpdateView):
    model = pfCatalogFileType
    form_class = pfCatalogFileTypeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogFileTypeUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful File Type"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogfiletype_list')
        return context


class pfCatalogOptionTypeListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogOptionTypeListView,
                        self).get_context_data(**kwargs)
        context['table'] = pfCatalogOptionTypeTable(
            pfCatalogOptionType.objects.all())
        context['object_name'] = "Printful Option Type"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfcatalogoptiontype_create')
        return context


class pfCatalogOptionTypeCreateView(CreateView):
    model = pfCatalogOptionType
    form_class = pfCatalogOptionTypeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogOptionTypeCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Option Type"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogoptiontype_list')
        return context


class pfCatalogOptionTypeDetailView(DetailView):
    model = pfCatalogOptionType
    template_name = "business/pf/pfcatalogoptiontype_detail.html"


class pfCatalogOptionTypeUpdateView(UpdateView):
    model = pfCatalogOptionType
    form_class = pfCatalogOptionTypeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogOptionTypeUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Option Type"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogoptiontype_list')
        return context


class pfCatalogProductListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogProductListView,
                        self).get_context_data(**kwargs)
        context['table'] = pfCatalogProductTable(
            pfCatalogProduct.objects.all())
        context['object_name'] = "Printful Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfcatalogproduct_create')
        return context


class pfCatalogProductCreateView(CreateView):
    model = pfCatalogProduct
    form_class = pfCatalogProductForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogProductCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogproduct_list')
        return context


class pfCatalogProductDetailView(DetailView):
    model = pfCatalogProduct
    template_name = "business/pf/pfcatalogproduct_detail.html"


class pfCatalogProductUpdateView(UpdateView):
    model = pfCatalogProduct
    form_class = pfCatalogProductForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogProductUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogproduct_list')
        return context


class pfCatalogSizeListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogSizeListView, self).get_context_data(**kwargs)
        context['table'] = pfCatalogSizeTable(pfCatalogSize.objects.all())
        context['object_name'] = "Printful Size"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfcatalogsize_create')
        return context


class pfCatalogSizeCreateView(CreateView):
    model = pfCatalogSize
    form_class = pfCatalogSizeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogSizeCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Size"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogsize_list')
        return context


class pfCatalogSizeDetailView(DetailView):
    model = pfCatalogSize
    template_name = "business/pf/pfcatalogsize_detail.html"


class pfCatalogSizeUpdateView(UpdateView):
    model = pfCatalogSize
    form_class = pfCatalogSizeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogSizeUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Size"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogsize_list')
        return context


class pfCatalogVariantListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogVariantListView,
                        self).get_context_data(**kwargs)
        context['table'] = pfCatalogVariantTable(
            pfCatalogVariant.objects.all())
        context['object_name'] = "Printful Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfcatalogvariant_create')
        return context


class pfCatalogVariantCreateView(CreateView):
    model = pfCatalogVariant
    form_class = pfCatalogVariantForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogVariantCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogvariant_list')
        return context


class pfCatalogVariantDetailView(DetailView):
    model = pfCatalogVariant
    template_name = "business/pf/pfcatalogvariant_detail.html"


class pfCatalogVariantUpdateView(UpdateView):
    model = pfCatalogVariant
    form_class = pfCatalogVariantForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCatalogVariantUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfcatalogvariant_list')
        return context


class pfCountryListView(SingleTableView):
    template_name = "business/object_list.html"
    model = pfCountry
    table_class = pfCountryTable

    def get_context_data(self, **kwargs):
        context = super(pfCountryListView, self).get_context_data(**kwargs)
        context['object_name'] = "Country"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_pfcountry_create')
        return context


class pfCountryCreateView(CreateView):
    model = pfCountry
    form_class = pfCountryForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCountryCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Country"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_pfcountry_list')
        return context


class pfCountryDetailView(DetailView):
    model = pfCountry
    template_name = "business/pf/pfcountry_detail.html"


class pfCountryUpdateView(UpdateView):
    model = pfCountry
    form_class = pfCountryForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfCountryUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Country"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_pfcountry_list')
        return context


class pfPrintFileListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfPrintFileListView, self).get_context_data(**kwargs)
        context['table'] = pfPrintFileTable(pfPrintFile.objects.all())
        context['object_name'] = "Printful File"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_pfprintfile_create')
        return context


class pfPrintFileCreateView(CreateView):
    model = pfPrintFile
    form_class = pfPrintFileForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfPrintFileCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful File"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_pfprintfile_list')
        return context


class pfPrintFileDetailView(DetailView):
    model = pfPrintFile
    template_name = "business/pf/pfprintfile_detail.html"


class pfPrintFileUpdateView(UpdateView):
    model = pfPrintFile
    form_class = pfPrintFileForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfPrintFileUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful File"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_pfprintfile_list')
        return context


class pfStateListView(SingleTableView):
    template_name = "business/object_list.html"
    model = pfState
    table_class = pfStateTable

    def get_context_data(self, **kwargs):
        context = super(pfStateListView, self).get_context_data(**kwargs)
        context['object_name'] = "State"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_pfstate_create')
        context['active_app'] = "lists"
        return context


class pfStateCreateView(CreateView):
    model = pfState
    form_class = pfStateForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfStateCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "State"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_pfstate_list')
        return context


class pfStateDetailView(DetailView):
    model = pfState
    template_name = "business/pf/pfstate_detail.html"


class pfStateUpdateView(UpdateView):
    model = pfState
    form_class = pfStateForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfStateUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "State"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_pfstate_list')
        return context


class pfStoreListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfStoreListView, self).get_context_data(**kwargs)
        context['table'] = pfStoreTable(pfStore.objects.all())
        context['object_name'] = "Printful Store"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_pfstore_create')
        return context


class pfStoreCreateView(CreateView):
    model = pfStore
    form_class = pfStoreForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfStoreCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Store"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_pfstore_list')
        return context


class pfStoreDetailView(DetailView):
    model = pfStore
    template_name = "business/pf/pfstore_detail.html"


class pfStoreUpdateView(UpdateView):
    model = pfStore
    form_class = pfStoreForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfStoreUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Printful Store"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_pfstore_list')
        return context


class pfSyncItemOptionListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncItemOptionListView,
                        self).get_context_data(**kwargs)
        context['table'] = pfSyncItemOptionTable(
            pfSyncItemOption.objects.all())
        context['object_name'] = "Sync Item Option"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfsyncitemoption_create')
        return context


class pfSyncItemOptionCreateView(CreateView):
    model = pfSyncItemOption
    form_class = pfSyncItemOptionForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncItemOptionCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Sync Item Option"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfsyncitemoption_list')
        return context


class pfSyncItemOptionDetailView(DetailView):
    model = pfSyncItemOption
    template_name = "business/pf/pfsyncitemoption_detail.html"


class pfSyncItemOptionUpdateView(UpdateView):
    model = pfSyncItemOption
    form_class = pfSyncItemOptionForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncItemOptionUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Sync Item Option"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfsyncitemoption_list')
        return context


class pfSyncProductListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncProductListView, self).get_context_data(**kwargs)
        context['table'] = pfSyncProductTable(pfSyncProduct.objects.all())
        context['object_name'] = "Sync Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfsyncproduct_create')
        return context


class pfSyncProductCreateView(CreateView):
    model = pfSyncProduct
    form_class = pfSyncProductForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncProductCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Sync Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfsyncproduct_list')
        return context


class pfSyncProductDetailView(DetailView):
    model = pfSyncProduct
    template_name = "business/pf/pfsyncproduct_detail.html"


class pfSyncProductUpdateView(UpdateView):
    model = pfSyncProduct
    form_class = pfSyncProductForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncProductUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Sync Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfsyncproduct_list')
        return context


class pfSyncVariantListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncVariantListView, self).get_context_data(**kwargs)
        context['table'] = pfSyncVariantTable(pfSyncVariant.objects.all())
        context['object_name'] = "Sync Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_pfsyncvariant_create')
        return context


class pfSyncVariantCreateView(CreateView):
    model = pfSyncVariant
    form_class = pfSyncVariantForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncVariantCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Sync Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfsyncvariant_list')
        return context


class pfSyncVariantDetailView(DetailView):
    model = pfSyncVariant
    template_name = "business/pf/pfsyncvariant_detail.html"


class pfSyncVariantUpdateView(UpdateView):
    model = pfSyncVariant
    form_class = pfSyncVariantForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(pfSyncVariantUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Sync Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_pfsyncvariant_list')
        return context


class wooAttributeListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooAttributeListView, self).get_context_data(**kwargs)
        context['table'] = wooAttributeTable(wooAttribute.objects.all())
        context['object_name'] = "Wp Attribute"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_wooattribute_create')
        return context


class wooAttributeCreateView(CreateView):
    model = wooAttribute
    form_class = wooAttributeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooAttributeCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Attribute"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wooattribute_list')
        return context


class wooAttributeDetailView(DetailView):
    model = wooAttribute
    template_name = "business/woo/wooattribute_detail.html"


class wooAttributeUpdateView(UpdateView):
    model = wooAttribute
    form_class = wooAttributeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooAttributeUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Attribute"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wooattribute_list')
        return context


class wooCategoryListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooCategoryListView, self).get_context_data(**kwargs)
        context['table'] = wooCategoryTable(wooCategory.objects.all())
        context['object_name'] = "Wp Category"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_woocategory_create')
        return context


class wooCategoryCreateView(CreateView):
    model = wooCategory
    form_class = wooCategoryForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooCategoryCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Category"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_woocategory_list')
        return context


class wooCategoryDetailView(DetailView):
    model = wooCategory
    template_name = "business/woo/woocategory_detail.html"


class wooCategoryUpdateView(UpdateView):
    model = wooCategory
    form_class = wooCategoryForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooCategoryUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Category"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_woocategory_list')
        return context


class wooImageListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooImageListView, self).get_context_data(**kwargs)
        context['table'] = wooImageTable(wooImage.objects.all())
        context['object_name'] = "Wp Image"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_wooimage_create')
        return context


class wooImageCreateView(CreateView):
    model = wooImage
    form_class = wooImageForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooImageCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Image"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wooimage_list')
        return context


class wooImageDetailView(DetailView):
    model = wooImage
    template_name = "business/woo/wooimage_detail.html"


class wooImageUpdateView(UpdateView):
    model = wooImage
    form_class = wooImageForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooImageUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Image"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wooimage_list')
        return context


class wooProductListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooProductListView, self).get_context_data(**kwargs)
        context['table'] = wooProductTable(wooProduct.objects.all())
        context['object_name'] = "Wp Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_wooproduct_create')
        return context


class wooProductCreateView(CreateView):
    model = wooProduct
    form_class = wooProductForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooProductCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wooproduct_list')
        return context


class wooProductDetailView(DetailView):
    model = wooProduct
    template_name = "business/woo/wooproduct_detail.html"


class wooProductUpdateView(UpdateView):
    model = wooProduct
    form_class = wooProductForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooProductUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Product"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wooproduct_list')
        return context


class wooShippingClassListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooShippingClassListView,
                        self).get_context_data(**kwargs)
        context['table'] = wooShippingClassTable(
            wooShippingClass.objects.all())
        context['object_name'] = "Wp Shipping Class"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse(
            'business:business_wooshippingclass_create')
        return context


class wooShippingClassCreateView(CreateView):
    model = wooShippingClass
    form_class = wooShippingClassForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooShippingClassCreateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Shipping Class"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_wooshippingclass_list')
        return context


class wooShippingClassDetailView(DetailView):
    model = wooShippingClass
    template_name = "business/woo/wooshippingclass_detail.html"


class wooShippingClassUpdateView(UpdateView):
    model = wooShippingClass
    form_class = wooShippingClassForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooShippingClassUpdateView,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Shipping Class"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse(
            'business:business_wooshippingclass_list')
        return context


class wooStoreListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooStoreListView, self).get_context_data(**kwargs)
        context['table'] = wooStoreTable(wooStore.objects.all())
        context['object_name'] = "Wp Store"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_woostore_create')
        return context


class wooStoreCreateView(CreateView):
    model = wooStore
    form_class = wooStoreForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooStoreCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Store"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_woostore_list')
        return context


class wooStoreDetailView(DetailView):
    model = wooStore
    template_name = "business/woo/woostore_detail.html"


class wooStoreUpdateView(UpdateView):
    model = wooStore
    form_class = wooStoreForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooStoreUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Store"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_woostore_list')
        return context


class wooTagListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooTagListView, self).get_context_data(**kwargs)
        context['table'] = wooTagTable(wooTag.objects.all())
        context['object_name'] = "Wp Tag"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_wootag_create')
        return context


class wooTagCreateView(CreateView):
    model = wooTag
    form_class = wooTagForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooTagCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Tag"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wootag_list')
        return context


class wooTagDetailView(DetailView):
    model = wooTag
    template_name = "business/woo/wootag_detail.html"


class wooTagUpdateView(UpdateView):
    model = wooTag
    form_class = wooTagForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooTagUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Tag"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wootag_list')
        return context


class wooTermListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooTermListView, self).get_context_data(**kwargs)
        context['table'] = wooTermTable(wooTerm.objects.all())
        context['object_name'] = "Wp Term"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_wooterm_create')
        return context


class wooTermCreateView(CreateView):
    model = wooTerm
    form_class = wooTermForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooTermCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Term"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wooterm_list')
        return context


class wooTermDetailView(DetailView):
    model = wooTerm
    template_name = "business/woo/wooterm_detail.html"


class wooTermUpdateView(UpdateView):
    model = wooTerm
    form_class = wooTermForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooTermUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Term"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wooterm_list')
        return context


class wooVariantListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wooVariantListView, self).get_context_data(**kwargs)
        context['table'] = wooVariantTable(wooVariant.objects.all())
        context['object_name'] = "Wp Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_woovariant_create')
        return context


class wooVariantCreateView(CreateView):
    model = wooVariant
    form_class = wooVariantForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooVariantCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_woovariant_list')
        return context


class wooVariantDetailView(DetailView):
    model = wooVariant
    template_name = "business/woo/woovariant_detail.html"


class wooVariantUpdateView(UpdateView):
    model = wooVariant
    form_class = wooVariantForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wooVariantUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Variant"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_woovariant_list')
        return context


class wpMediaListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wpMediaListView, self).get_context_data(**kwargs)
        context['table'] = wpMediaTable(wpMedia.objects.all())
        context['object_name'] = "Wp Media"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_wpmedia_create')
        return context


class wpMediaCreateView(CreateView):
    model = wpMedia
    form_class = wpMediaForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wpMediaCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Media"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wpmedia_list')
        return context


class wpMediaDetailView(DetailView):
    model = wpMedia
    template_name = "business/wp/wpmedia_detail.html"


class wpMediaUpdateView(UpdateView):
    model = wpMedia
    form_class = wpMediaForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wpMediaUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Media"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wpmedia_list')
        return context


class wpMediaSizeListView(TemplateView):
    template_name = "business/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(wpMediaSizeListView, self).get_context_data(**kwargs)
        context['table'] = wpMediaSizeTable(wpMediaSize.objects.all())
        context['object_name'] = "Wp Media Size"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_new'] = reverse('business:business_wpmediasize_create')
        return context


class wpMediaSizeCreateView(CreateView):
    model = wpMediaSize
    form_class = wpMediaSizeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wpMediaSizeCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Media Size"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wpmediasize_list')
        return context


class wpMediaSizeDetailView(DetailView):
    model = wpMediaSize
    template_name = "business/wp/wpmediasize_detail.html"


class wpMediaSizeUpdateView(UpdateView):
    model = wpMediaSize
    form_class = wpMediaSizeForm
    template_name = "business/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(wpMediaSizeUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['object_name'] = "Wp Media Size"
        context['object_group'] = ""
        context['object_icon'] = None
        context['action_list'] = reverse('business:business_wpmediasize_list')
        return context
