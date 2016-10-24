from django.shortcuts import render
from .models import *
# from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView

def HomeView(request):
    template = 'printaura/home.html'
    g = LocalProductGroup.objects.all()

    context = {
        'localproductgroups': g
    }
    return render(request, template, context)
