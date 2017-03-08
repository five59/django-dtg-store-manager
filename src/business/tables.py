import django_tables2 as tables
from .models import *
from django_tables2.utils import A
from django.utils.translation import ugettext_lazy as _
from django.contrib.humanize.templatetags.humanize import naturaltime


class commonBusinessTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:[M]_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:[M]_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''

    date_added = tables.Column()
    date_updated = tables.Column()

    def render_date_added(self, value):
        return naturaltime(value)

    def render_date_updated(self, value):
        return naturaltime(value)


class bzBrandTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_store_brand')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = bzBrand
        sequence = ('actions', 'code', 'name', 'vendor',
                    'outlet', 'date_added', 'date_updated',)
        exclude = ('id',)
        attrs = {'class': 'table table-striped table-hover'}


class bzCreativeCollectionTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'business_bzbrand')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = bzCreativeCollection
        sequence = ('actions', 'code', 'name', 'bzbrand',)
        exclude = ('date_added', 'date_updated', 'id',)
        attrs = {'class': 'table table-striped table-hover'}


class bzCreativeDesignTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_creative_design')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    product_count = tables.TemplateColumn("{{ record.num_products }}")

    class Meta:
        model = bzCreativeDesign
        sequence = ('actions', 'code', 'name', 'product_count', 'date_added',
                    'date_updated',)
        exclude = ('id', 'bzcreativecollection',)
        attrs = {'class': 'table table-striped table-hover'}
        empty_text = "No Designs Found."


class bzCreativeLayoutTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_creative_layout')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    product_count = tables.TemplateColumn("{{ record.num_products }}")

    class Meta:
        model = bzCreativeLayout
        sequence = ('actions', 'code', 'name', 'product_count',
                    'date_added', 'date_updated',)
        exclude = ('id', 'bzcreativecollection',)
        attrs = {'class': 'table table-striped table-hover'}
        empty_text = "No Layouts Found."


class bzCreativeRenderingTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_creative_rendering')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = bzCreativeRendering
        attrs = {'class': 'table table-striped table-hover'}


class bzProductTable(commonBusinessTable):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_bzbrand_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_bzbrand_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    variant_count = tables.TemplateColumn("{{ record.num_variants }}")

    class Meta:
        model = bzProduct
        attrs = {'class': 'table table-striped table-hover'}


class bzProductVariantTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'business_bzvariant')

    class Meta:
        model = bzProductVariant
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogColorTable(commonBusinessTable):

    class Meta:
        model = pfCatalogColor
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogFileSpecTable(commonBusinessTable):

    class Meta:
        model = pfCatalogFileSpec
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogFileTypeTable(commonBusinessTable):

    class Meta:
        model = pfCatalogFileType
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogOptionTypeTable(commonBusinessTable):

    class Meta:
        model = pfCatalogOptionType
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogProductTable(commonBusinessTable):

    class Meta:
        model = pfCatalogProduct
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogSizeTable(commonBusinessTable):

    class Meta:
        model = pfCatalogSize
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogVariantTable(commonBusinessTable):

    class Meta:
        model = pfCatalogVariant
        attrs = {'class': 'table table-striped table-hover'}


class pfCountryTable(commonBusinessTable):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_pfcountry_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_pfcountry_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    num_states = tables.Column(A('num_states'))

    class Meta:
        model = pfCountry
        sequence = ('actions', 'code', 'name', 'num_states')
        exclude = ('date_added', 'date_updated', 'id')
        attrs = {'class': 'table table-striped table-hover'}


class pfPrintFileTable(commonBusinessTable):

    class Meta:
        model = pfPrintFile
        attrs = {'class': 'table table-striped table-hover'}


class pfStateTable(commonBusinessTable):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:business_pfstate_detail' record.pk %}"><span class="glyphicon glyphicon-eye-open"></span></a>
       <a href="{% url 'business:business_pfstate_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = pfState
        sequence = ('actions', 'code', 'name', 'pfcountry',)
        exclude = ('date_added', 'date_updated', 'id')
        attrs = {'class': 'table table-striped table-hover'}


class pfStoreTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_store_pf')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    has_auth = tables.columns.BooleanColumn(A('has_auth'))

    class Meta:
        model = pfStore
        sequence = ('actions', 'code', 'name', 'has_auth',
                    'date_added', 'date_updated',)
        exclude = ('id', 'key',
                   'created', 'website',)
        attrs = {'class': 'table table-striped table-hover'}


class pfSyncItemOptionTable(commonBusinessTable):

    class Meta:
        model = pfSyncItemOption
        attrs = {'class': 'table table-striped table-hover'}


class pfSyncProductTable(commonBusinessTable):

    class Meta:
        model = pfSyncProduct
        attrs = {'class': 'table table-striped table-hover'}


class pfSyncVariantTable(commonBusinessTable):

    class Meta:
        model = pfSyncVariant
        attrs = {'class': 'table table-striped table-hover'}


class wooAttributeTable(commonBusinessTable):

    class Meta:
        model = wooAttribute
        attrs = {'class': 'table table-striped table-hover'}


class wooCategoryTable(commonBusinessTable):

    class Meta:
        model = wooCategory
        attrs = {'class': 'table table-striped table-hover'}


class wooImageTable(commonBusinessTable):

    class Meta:
        model = wooImage
        attrs = {'class': 'table table-striped table-hover'}


class wooProductTable(commonBusinessTable):

    class Meta:
        model = wooProduct
        attrs = {'class': 'table table-striped table-hover'}


class wooShippingClassTable(commonBusinessTable):

    class Meta:
        model = wooShippingClass
        attrs = {'class': 'table table-striped table-hover'}


class wooStoreTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_store_wp')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")

    class Meta:
        model = wooStore
        sequence = ('actions', 'code', 'base_url', 'timezone', 'verify_ssl',
                    'date_added', 'date_updated',)
        exclude = ('id', 'consumer_secret')
        attrs = {'class': 'table table-striped table-hover'}


class wooTagTable(commonBusinessTable):

    class Meta:
        model = wooTag
        attrs = {'class': 'table table-striped table-hover'}


class wooTermTable(commonBusinessTable):

    class Meta:
        model = wooTerm
        attrs = {'class': 'table table-striped table-hover'}


class wooVariantTable(commonBusinessTable):

    class Meta:
        model = wooVariant
        attrs = {'class': 'table table-striped table-hover'}


class wpMediaTable(commonBusinessTable):

    class Meta:
        model = wpMedia
        attrs = {'class': 'table table-striped table-hover'}


class wpMediaSizeTable(commonBusinessTable):

    class Meta:
        model = wpMediaSize
        attrs = {'class': 'table table-striped table-hover'}
