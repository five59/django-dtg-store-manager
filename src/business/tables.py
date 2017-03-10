import django_tables2 as tables
from .models import *
from django_tables2.utils import A
from django.utils.translation import ugettext_lazy as _
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.template.defaultfilters import title as titlecase

# Master Table Class


class commonBusinessTable(tables.Table):
    ACTION_TEMPLATE = '''
       <a href="{% url 'business:[M]_update' record.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    '''

    # Used as the attrs of the primary link.
    PRIMARY_BUTTON_ATTRS = {'a': {'class': 'btn btn-primary btn-xs'}}

    date_added = tables.Column()
    date_updated = tables.Column()

    def render_date_added(self, value):
        return titlecase(naturaltime(value))

    def render_date_updated(self, value):
        return titlecase(naturaltime(value))

# App Store


class bzBrandTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_store_brand')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    code = tables.LinkColumn(
        viewname='business:app_store_brand_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzBrand
        fields = ('code', 'name', 'vendor',
                  'outlet', 'date_added', 'date_updated', 'actions', )
        sequence = fields
        attrs = {'class': 'table table-striped table-hover'}


class pfStoreTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_store_pf')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    has_auth = tables.columns.BooleanColumn(A('has_auth'))
    code = tables.LinkColumn(
        viewname='business:app_store_pf_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = pfStore
        fields = ('code', 'name', 'has_auth', 'pid',
                  'date_added', 'date_updated', 'actions',)
        sequence = fields
        attrs = {'class': 'table table-striped table-hover'}


class wooStoreTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_store_wp')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    base_url = tables.Column()
    code = tables.LinkColumn(
        viewname='business:app_store_wp_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = wooStore
        fields = ('code', 'base_url', 'timezone', 'verify_ssl',
                  'date_added', 'date_updated', 'actions',)
        sequence = fields
        attrs = {'class': 'table table-striped table-hover'}

# App Creative


class bzCreativeDesignTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_creative_design')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    product_count = tables.TemplateColumn("{{ record.num_products }}")
    code = tables.LinkColumn(
        viewname='business:app_creative_design_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzCreativeDesign
        fields = ('code', 'name', 'product_count', 'date_added',
                  'date_updated', 'actions', )
        sequence = fields
        attrs = {'class': 'table table-striped table-hover'}
        empty_text = "No Designs Found."


class bzCreativeLayoutTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_creative_layout')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    product_count = tables.TemplateColumn("{{ record.num_products }}")
    code = tables.LinkColumn(
        viewname='business:app_creative_layout_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzCreativeLayout
        fields = ('code', 'name', 'product_count',
                  'date_added', 'date_updated', 'actions', )
        sequence = fields
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
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_list_color')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    code = tables.LinkColumn(
        viewname='business:app_list_color_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzBrand
        fields = ('code', 'label', 'label_clean',
                  'date_added', 'date_updated', 'actions', )
        sequence = fields
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogFileSpecTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_list_filespec')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    code = tables.LinkColumn(
        viewname='business:app_list_filespec_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzBrand
        fields = ('name', 'note', 'width', 'height', 'width_in', 'height_in',
                  'ratio', 'colorsystem',
                  'date_added', 'date_updated', 'actions', )
        sequence = fields
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
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_list_cprod')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    local = {'td': {'class': 'text-center'}}
    pid = tables.LinkColumn(
        viewname='business:app_list_cprod_update', args=[A('pk')],
        attrs={**commonBusinessTable.PRIMARY_BUTTON_ATTRS, **local}
    )

    class Meta:
        model = pfCatalogProduct
        fields = ('pid', 'brand', 'model', 'type', 'is_active',
                  'actions', )
        exclude = ('date_added', 'date_updated',)
        sequence = fields
        attrs = {'class': 'table table-striped table-hover'}


class pfCatalogSizeTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_list_color')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    code = tables.LinkColumn(
        viewname='business:app_list_size_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzBrand
        fields = ('code', 'label', 'label_clean', 'sort_group', 'sort_order',
                  'date_added', 'date_updated', 'actions', )
        sequence = fields
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
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_list_category')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    code = tables.LinkColumn(
        viewname='business:app_list_category_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzBrand
        fields = ('name', 'wid', 'is_active', 'display', 'count',
                  'date_added', 'date_updated', 'actions', )
        sequence = fields
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
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_list_shipping')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    code = tables.LinkColumn(
        viewname='business:app_list_shipping_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzBrand
        fields = ('name', 'count', 'wid',
                  'date_added', 'date_updated', 'actions', )
        sequence = fields
        attrs = {'class': 'table table-striped table-hover'}


class wooTagTable(commonBusinessTable):
    ACTION_TEMPLATE = commonBusinessTable.ACTION_TEMPLATE.replace(
        '[M]', 'app_list_tag')
    actions = tables.TemplateColumn(ACTION_TEMPLATE, verbose_name="")
    code = tables.LinkColumn(
        viewname='business:app_list_tag_update', args=[A('pk')],
        attrs=commonBusinessTable.PRIMARY_BUTTON_ATTRS)

    class Meta:
        model = bzBrand
        fields = ('name', 'wid', 'is_active', 'store', 'count',
                  'date_added', 'date_updated', 'actions', )
        sequence = fields
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
