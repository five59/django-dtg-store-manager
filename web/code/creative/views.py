from django.shortcuts import render
from .models import *


def Dashboard_list(request):
    series = Series.objects.all()
    context = {
        'series': series,
    }
    return render(request, 'creative/Dashboard_list.html', context)
