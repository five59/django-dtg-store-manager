from django.shortcuts import render
from .models import *


def ManufacturerItem_list(request):
    categories = Category.objects.all()
    mis = ManufacturerItem.objects.filter(
        is_active=True).order_by(
        'item__category', 'item__brand', 'item__code')
    context = {
        'mis': mis,
        'categories': categories,
    }
    return render(request, 'catalog/ManufacturerItem_list.html', context)

def ManufacturerItem_export(request):
    categories = Category.objects.all()
    mis = ManufacturerItem.objects.filter(
        is_active=True).order_by(
        'item__category', 'item__brand', 'item__code')
    context = {
        'mis': mis,
        'categories': categories,
    }
    return render(request, 'catalog/ManufacturerItem_export.html', context)


def ManufacturerItem_detail(request, id):
    mi = ManufacturerItem.objects.get(id=id)
    context = {
        'mi': mi,
    }
    return render(request, 'catalog/ManufacturerItem_detail.html', context)

def ManufacturerVariant_list(request, manufacturercode=None, brandcode=None):
    # TODO Until I can figure out a better way, only let "MEDIUMS" through if apparel-size-based
    mv = ManufacturerVariant.objects.exclude(size__in=[
        'XXS','XS','S','L','XL','2XL','3XL','4XL','5XL', #'M'
        '6-12m','12-18m','18-24m', #'3-6m'
        '4yrs','6yrs' #'2yrs'
        '10yrs','12yrs', #'8yrs'
    ])
    if manufacturercode:
        mv = mv.filter(manufacturer__code=manufacturercode)
    if brandcode:
        mv = mv.filter(product__item__brand__code=brandcode)

    context = {
        'mv': mv.order_by('product__item__category','product__item__brand','product__item__code','color','size',),
    }
    return render(request, 'catalog/ManufacturerVariant_list.html', context)