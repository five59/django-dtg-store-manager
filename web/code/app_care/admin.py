from django.contrib import admin
from .models import *


class CareInstructionsAdmin(admin.ModelAdmin):
    list_display = [
        'get_item_code',
        'icon_wash', 'icon_bleach',
        'icon_dry', 'icon_wring', 'icon_iron', 'icon_dryclean', ]

    # list_editable = [
    #     'icon_wash',
    #     'icon_bleach',
    #     'icon_dry',
    #     'icon_wring',
    #     'icon_iron',
    #     'icon_dryclean',
    # ]


admin.site.register(CareInstructions, CareInstructionsAdmin)


class CareComponentAdmin(admin.ModelAdmin):
    list_filter = ['category', ]
    list_display = ['code', 'name', 'category', 'has_icon', ]
    # list_editable = ['name',]
admin.site.register(CareComponent, CareComponentAdmin)


class CareLabelAdmin(admin.ModelAdmin):
    pass
admin.site.register(CareLabel, CareLabelAdmin)
