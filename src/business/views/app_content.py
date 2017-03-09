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
from business.helper_backend import commonListView


class appContentHome(TemplateView):
    template_name = "content/page.html"

    def get_context_data(self, **kwargs):
        context = super(appContentHome, self).get_context_data(**kwargs)
        context['active_app'] = "content"
        context['active_apptitle'] = "Content Editor"
        return context
