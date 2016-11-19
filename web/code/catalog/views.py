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


def ManufacturerItem_detail(request, id):
    mi = ManufacturerItem.objects.get(id=id)
    context = {
        'mi': mi,
    }
    return render(request, 'catalog/ManufacturerItem_detail.html', context)
