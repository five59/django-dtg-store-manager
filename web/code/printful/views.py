from django.shortcuts import *
from .models import *

def Home(request):
    template = 'printful/home.html'
    context = {}
    return render(request, template, context)

# def Product_List(request):
#     template = 'printful/product_list.html'
#     context = {
#         'products': pfProduct.objects.all().order_by('product_type','brand',),
#     }
#     return render(request, template, context)
