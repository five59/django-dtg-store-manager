from django.contrib import admin
from .models import *

class AttributeAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'name',
        'is_variant_key',
    ]
admin.site.register(Attribute, AttributeAdmin)

class AttributeValueAdmin(admin.ModelAdmin):
    pass
admin.site.register(AttributeValue, AttributeValueAdmin)

class CollectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Collection, CollectionAdmin)

class CreativeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Creative, CreativeAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Manufacturer, ManufacturerAdmin)

class OutletAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'name',
        'public_url',
        ]
admin.site.register(Outlet, OutletAdmin)

class PartAdmin(admin.ModelAdmin):
    pass
admin.site.register(Part, PartAdmin)

class ProducerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Producer, ProducerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)
