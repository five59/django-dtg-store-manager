# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
# from .forms import *
from django.utils.translation import ugettext_lazy as _


# class gCredentialAdmin(admin.ModelAdmin):
#     list_display = [
#         'code', 'name',
#         # 'cred_type',
#         # 'project_id',
#
#     ]
# admin.site.register(gCredential, gCredentialAdmin)

class DataFeedItemInline(admin.TabularInline):
    model = DataFeedItem
    extra = 0
    fields = ('identifier', 'title', 'color', 'size',)
    readonly_fields = ('identifier', 'title', 'color', 'size',)


class DataFeedAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'shop', 'get_num_items', 'date_lastgenerated',)
    # inlines = (DataFeedItemInline,)
admin.site.register(DataFeed, DataFeedAdmin)


class DataFeedItemAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'title', 'feed', 'product_type',)
    list_filter = ('feed',)
admin.site.register(DataFeedItem, DataFeedItemAdmin)
