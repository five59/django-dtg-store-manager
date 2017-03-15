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
from business.filters import *

from business.helper_backend import commonListView, commonUpdateView, commonCreateView
from django.contrib import messages


class appDAMSCommonListView(commonListView):
    active_app = 'dams'
    active_apptitle = 'Digital Asset Management'
    object_icon = 'picture'


class appDAMSCommonUpdateView(commonUpdateView):
    active_app = 'dams'
    active_apptitle = 'Digital Asset Management'
    object_icon = 'picture'


class appDAMSCommonCreateView(commonCreateView):
    active_app = 'dams'
    active_apptitle = 'Digital Asset Management'
    object_icon = 'picture'

# ======


class appDAMSHome(View):
    def get(self, request):
        return redirect(reverse('business:app_dams_pf_list'))


class appDAMSPFList(appDAMSCommonListView):
    model = pfPrintFile
    table_class = pfPrintFileTable
    object_name = "Printful File"
    action_list = [
        {
            'btn_class': 'default',
            'view': 'business:app_dams_pf_apipull',
            'text': 'Sync'
        },
    ]


class appDAMSPFDetail(appDAMSCommonUpdateView):
    model = pfPrintFile
    form_class = pfPrintFileForm
    object_name = "Print File"
    success_url = reverse_lazy("business:app_dams_pf_list")
    action_list = reverse_lazy("business:app_dams_pf_list")


class appDAMSPFCreate(appDAMSCommonCreateView):
    # TODO Implement appDAMSPFCreate View
    pass


class appDAMSPFApiPull(View):
    def get(self, request):
        try:
            sCounter = 0
            # TODO Add ability to sync only one Printful store's PrintFilesq
            # (currently syncs all stores).
            for s in pfStore.objects.all():
                pfPrintFile.api_pull(s)
                sCounter += 1
            messages.add_message(request, messages.SUCCESS,
                                 "Success! Updated print files for {} stores.".format(sCounter))
        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 'API call failed. {}'.format(e))
        return redirect('business:app_dams_pf_list')
