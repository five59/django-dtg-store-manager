# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 5
    fields = ['code', 'product', 'color', 'size', ]
    suit_classes = 'suit-tab suit-tab-variants'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'design', 'item', 'sales_channel',)
    list_filter = ('design', 'item')
    search_fields = ('name',)
    inlines = (VariantInline,)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ('code', 'name', 'design', 'item', 'sales_channel',),
        }),
    ]
    suit_form_tabs = (
        ('info', _("Info")),
        ('variants', _("Variants")),
    )
admin.site.register(Product, ProductAdmin)


class VariantAdmin(admin.ModelAdmin):
    list_display = ('code', 'product', 'color', 'size')
    list_filter = ('product', 'color', 'size')
admin.site.register(Variant, VariantAdmin)
