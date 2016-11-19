from django.contrib import admin
from .models import *
from .forms import *
from django.utils.translation import ugettext_lazy as _


class SalesChannelInline(admin.TabularInline):
    model = SalesChannel
    extra = 0
    fields = ['name', 'code', ]
    suit_classes = 'suit-tab suit-tab-saleschannels'


class SeriesInline(admin.TabularInline):
    model = Series
    extra = 0
    fields = ['name', 'code', ]
    suit_classes = 'suit-tab suit-tab-series'


class ArtistInline(admin.TabularInline):
    model = Artist
    extra = 0
    fields = ['name', 'code', ]
    suit_classes = 'suit-tab suit-tab-artists'


class DesignInline(admin.TabularInline):
    model = Design
    extra = 0
    fields = ['name', 'code', 'note', ]
    suit_classes = 'suit-tab suit-tab-design'


class SalesChannelAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'web_url', ]
    list_filter = ['category', ]
    inlines = (SeriesInline,)
    form = SalesChannelForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': ['code', 'name', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': [
                'category',
                'web_url',
            ]
        }),
        (_("Description"), {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width'),
            'fields': [
                'description',
            ]
        })
    ]
    suit_form_tabs = (
        ('info', _("Info")),
        ('series', _("Series")),
    )
admin.site.register(SalesChannel, SalesChannelAdmin)


class SeriesAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'sales_channel',
                    'creative_lead', 'num_designs',  'percent_designs_live', ]
    list_filter = ['sales_channel', 'creative_lead', ]
    inlines = (DesignInline,)
    form = SeriesForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': ['code', 'name', 'creative_lead', 'sales_channel', ]
        }),
        ("Note", {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width'),
            'fields': ['note', ]
        })
    ]
    suit_form_tabs = (
        ('info', _("Info")),
        ('design', _("Design")),
    )
admin.site.register(Series, SeriesAdmin)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'location']
    list_filter = ['location', ]
    inlines = (DesignInline, SeriesInline,)
    form = ArtistForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': [
                'code', 'name',
            ]
        }),
        (_("Location"), {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': [
                'location',
            ]
        }),
        (_("Contact Info"), {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': [
                'web', 'phone', 'email',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-legal',),
            'fields': [
                'has_agreement',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-legal', 'full-width',),
            'fields': [
                'agreement',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-notes', 'full-width',),
            'fields': [
                'notes',
            ]
        }),
    ]
    suit_form_tabs = (
        ('info', _("Info")),
        ('legal', _("Legal")),
        ('notes', _("Notes")),
        ('design', _("Design")),
        ('series', _("Series Leaderships")),
    )
admin.site.register(Artist, ArtistAdmin)


class DesignAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'status_tag',
        'series',
        'artist',
    ]
    # list_editable = ['code', ]
    list_filter = [
        'series', 'status'
    ]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': [
                'code', 'name',
                'series',
                'artist',
                'status',
            ]
        })
    ]
    suit_form_tabs = (
        ('info', _("Info")),
    )
admin.site.register(Design, DesignAdmin)
