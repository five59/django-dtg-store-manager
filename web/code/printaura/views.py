# from django.shortcuts import render, get_object_or_404
# from .models import *
# # from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
#
# def HomeView(request):
#     template = 'printaura/home.html'
#     context = {
#         'localproductgroups': LocalProductGroup.objects.all(),
#     }
#     return render(request, template, context)
#
# def LPGDetailView(request, slug):
#     template = 'printaura/lpg_detail.html'
#     context = {
#         'group': get_object_or_404(LocalProductGroup, slug=slug),
#     }
#     return render(request, template, context)
#
# def ProductDetailView(request, slug):
#     template = 'printaura/product_detail.html'
#     context = {
#         'product': get_object_or_404(Product, slug=slug),
#     }
#     return render(request, template, context)
#
# def BrandDetailView(request, slug):
#     template = 'printaura/brand_detail.html'
#     context = {
#         'brand': get_object_or_404(Brand, slug=slug),
#     }
#     return render(request, template, context)
#
# def PriceListView(request):
#     template = 'printaura/price_list.html'
#     context = {
#         'groups': LocalProductGroup.objects.all(),
#     }
#     return render(request, template, context)
