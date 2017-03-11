from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import *
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from django.contrib.auth import get_user_model
from .models import *
from crispy_unforms.layout import *

User = get_user_model()

# Helper methods


def generateTable(data):
    rv = []
    rv.append('<table class="table table-striped">')
    for label, value in data.items():
        # FIXME There is definitely a better way to format this string.
        rv.append(
            '<tr><th>{}</th><td>[[object.{}]]</td></tr>'.format(
                label, value).replace('[', '{').replace(']', '}'))
    rv.append('</table>')
    return "".join(rv)


def generateColorSwatch(hex):
    if hex:
        rv = []
        url = "http://placehold.it/350x300/{{object." + hex + "}}?text=%20"
        rv.append("<div class='thumbnail'><img src='{}' />".format(url))
        rv.append('<div class="caption">{{ object }}</div></div>')
    return "".join(rv)


class businessCommonForm(forms.ModelForm):
    form_layout = None

    businessCommonLayoutHeader = Layout(
        Div(
            Div(
                HTML("""<h3>
                     {% if mode == 'create' %}Create New {{ object_name }}{% endif %}
                     {% if mode == 'update' %}
                        {% if object.name %}{{ object.name }}{% else %}Edit {{ object_name }}{% endif %}
                     {% endif %}
                     </h3>"""),
                css_class="col-md-8"
            ),
            Div(
                Div("",
                    HTML(
                        """<a href="{{ action_list }}" role="button" class="btn btn-default"><span class="glyphicon glyphicon-menu-left" aria-hidden="true"></span> Back</a>"""),
                    HTML("""<button class='btn btn-primary' type="submit" name="update" class="submit submitButton" id="submit-id-search">Save <span class='glyphicon glyphicon-menu-right'></button>"""),
                    # Submit(<button type="submit">this button submits the form</button>
                    #     'update', "<span class='glyphicon glyphicon-menu-right'> Save", css_class="btn-primary"),
                    css_class="btn-group pull-right", role="group"),
                css_class="col-md-4"
            ),
            css_class="row"
        )
    )

    def __init__(self, *args, **kwargs):
        super(businessCommonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            self.businessCommonLayoutHeader,
            Div(self.form_layout),
        )

# App: Store


class bzBrandForm(businessCommonForm):
    form_layout = Layout(
        Div(
            Div(
                Fieldset('Basics', 'code', 'name'),
                css_class="col-md-3"),
            Div(
                Fieldset('Relationships', 'vendor', 'outlet'),
                css_class="col-md-5"),
            Div(
                HTML("""<h4>Brands</h4>
                         <p>Brands connect a Printful store to a WordPress site. Everything you do within this app is linked to a specific brand.</p>"""),
                css_class="col-md-4"),
            css_class="row"))

    class Meta:
        model = bzBrand
        fields = ['code', 'name', 'vendor', 'outlet', ]


class pfStoreForm(businessCommonForm):
    form_layout = Layout(
        TabHolder(
            Tab('Basic Info',
                Div(
                    Div(
                        Fieldset('', 'code', 'key'),
                        css_class="col-md-5"),
                    Div(
                        HTML(
                            """<h4>{{ object.name }}</h4>
                                    {% if object.website %}<a href="{{ object.website }}" target="_blank">{{ object.website }}</a>{% endif %}"""
                        ),
                        css_class="col-md-7"),
                    css_class="row")
                ),
            Tab('Addresses',
                Div(
                    Div(HTML("""
                                    <div class="panel panel-default">
                                        <div class="panel-heading"
                                            <h3 class="panel-title">Billing Address</h3>
                                        </div>
                                        <div class="panel-body">{% if object.billing_address %}{{ object.billing_address.asHTML|safe }}{% else %}None on file.{% endif %}</div>
                                    </div>"""), css_class="col-md-4"),
                    Div(HTML("""
                                    <div class="panel panel-default">
                                        <div class="panel-heading"
                                            <h3 class="panel-title">Return Address</h3>
                                        </div>
                                        <div class="panel-body">{% if object.return_address %}{{ object.return_address.asHTML|safe }}{% else %}Return address will be Printful's own.{% endif %}</div>
                                    </div>"""), css_class="col-md-4"),
                    Div(
                        HTML("""<h4>Address Management</h4>
                                     <p>To manage this information, sign in to your Printful Dashboard.</p>"""),
                        css_class="col-md-4"),
                    css_class="row")
                ),
            Tab('Credit Card Info',
                Div(
                    Div(
                        HTML(generateTable({
                            'Payment Type': 'payment_type',
                            'Card Number (Masked)': 'payment_number_mask',
                            'Card Expires': 'payment_expires',
                        })),
                        css_class="col-md-8"),
                    Div(
                        HTML("""<h4>Payment Details</h4>
                                     <p>To manage this information, sign in to your Printful Dashboard.</p>"""),
                        css_class="col-md-4"),
                    css_class="row"),
                ),
            Tab('Packing Slip',
                Div(
                    Div(
                        Fieldset('', 'packingslip_email', 'packingslip_phone',
                                 'packingslip_message'),
                        css_class="col-md-8"),
                    Div(
                        HTML("""<h4>Packing Slip Details</h4>
                                         <p>This information gets printed on your customers' packing slips.</p>"""),
                        css_class="col-md-4"),
                    css_class="row"),
                ),
        )
    )

    class Meta:
        model = pfStore
        fields = ['code', 'key', 'packingslip_email',
                  'packingslip_phone', 'packingslip_message', ]


class wooStoreForm(businessCommonForm):
    form_layout = Layout(
        Div(
            Fieldset('', 'code', 'timezone', 'verify_ssl'),
            css_class="col-md-3"),
        Div(
            Fieldset('', 'base_url', 'consumer_key',
                     'consumer_secret',),
            css_class="col-md-5"),
        Div(
            HTML("""<h4>WordPress Site</h4>
                         <p>This sets up the connection to your WordPress site. It will broker all of the interactions with your WooCommerce store.</p>"""),
            css_class="col-md-4")
    )

    class Meta:
        model = wooStore
        fields = ['code', 'base_url', 'consumer_key', 'consumer_secret', 'timezone',
                  'verify_ssl']


# App: Creative

class bzCreativeCollectionForm(businessCommonForm):
    form_layout = Layout(
        Div(
            Fieldset('', 'code', 'name', 'bzbrand',),
            css_class="col-md-4")
    )

    class Meta:
        model = bzCreativeCollection
        fields = ['code', 'name', 'bzbrand', ]


class bzCreativeDesignForm(businessCommonForm):
    form_layout = Layout(
        Div(
            Fieldset('', 'code', 'name', 'bzcreativecollection',),
            css_class="col-md-4"),
    )

    class Meta:
        model = bzCreativeDesign
        fields = ['code', 'name', 'bzcreativecollection']


class bzCreativeLayoutForm(businessCommonForm):
    form_layout = Layout(
        Div(
            Fieldset('', 'code', 'name', 'bzcreativecollection',),
            css_class="col-md-4"),
    )

    class Meta:
        model = bzCreativeLayout
        fields = ['code', 'name', 'bzcreativecollection']


class bzCreativeRenderingForm(businessCommonForm):
    form_layout = Layout(
        Fieldset(
            '',
            'bzcreativedesign',
            'bzcreativelayout',
        ),
    )

    class Meta:
        model = bzCreativeRendering
        fields = ['bzcreativedesign', 'bzcreativelayout']


class bzProductForm(businessCommonForm):
    form_layout = Layout(
        Fieldset(
            '',
            'code',
            'name',
            'status',
            'bzDesign',
            'pfProduct',
            'wooProduct',
            'pfSyncProduct',
        ),
    )

    class Meta:
        model = bzProduct
        fields = ['code', 'name', 'status', 'bzDesign']


class bzProductVariantForm(businessCommonForm):
    def __init__(self, *args, **kwargs):
        super(bzProductVariantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'code',
                'is_active',
                'bzproduct',
                'pfcatalogvariant',
                'pfcolor',
                'pfsize',
            ),
            PrependedText('price', '$', placeholder="0.00"),
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = bzProductVariant
        fields = ['code', 'is_active', 'bzproduct', 'pfcatalogvariant',
                  'pfcolor', 'pfsize', 'price', ]


class wooAttributeForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = wooAttribute
        fields = ['is_active', 'wid',
                  'name', 'slug', 'type', 'has_archives', 'store']


class wooCategoryForm(businessCommonForm):
    form_layout = Layout(
        Div(
            Fieldset("", 'name', 'store', 'display',
                     'slug', 'parent', 'image_id',),
            css_class="col-md-4"
        ),
        Div(
            Fieldset("", 'description', 'is_active', ),
            HTML("<table class='table table-striped'>"),
            HTML("<tr><th>Product Count</th><td>{{ object.count }}<td></tr>"),
            HTML("<tr><th>WordPress ID</th><td>{{ object.wid }}<td></tr>"),
            HTML(
                "<tr><th>Image Creation Date</th><td>{{ object.image_date_created }}<td></tr>"),
            HTML("</table>"),
            css_class="col-md-4"
        ),
        Div(
            HTML("""<h4>Product Category</h4>
                             <p></p>"""),
            css_class="col-md-4"),

    )

    class Meta:
        model = wooCategory
        fields = ['is_active', 'wid', 'name', 'slug', 'parent',
                  'description', 'display', 'count', 'image_id',
                  'image_date_created', 'store']
        exclude = ['count', 'wid', 'image_date_created', ]


class wooImageForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = wooImage
        fields = ['is_active', 'wid', 'date_created', 'alt', 'position']


class wooProductForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = wooProduct
        fields = ['is_active', 'wid', 'slug', 'permalink', 'date_created',
                  'dimension_length', 'dimension_width', 'dimension_height',
                  'weight', 'reviews_allowed', 'woostore', 'shipping_class',
                  'tags', 'images']


class wooShippingClassForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = wooShippingClass
        fields = ['wid', 'name', 'slug', 'description', 'count']


class wooTagForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = wooTag
        fields = ['is_active', 'wid',
                  'name', 'slug', 'description', 'count', 'store']


class wooTermForm(businessCommonForm):

    form_layout = Layout()

    class Meta:
        model = wooTerm
        fields = ['wid', 'name', 'slug', 'menu_order',
                  'count', 'wr_tooltip', 'wr_label', 'productattribute']


class wooVariantForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = wooVariant
        fields = ['is_active', 'wid', 'date_created', 'permalink', 'sku',
                  'price', 'dimension_length', 'dimension_width',
                  'dimension_height', 'weight', 'shipping_class', 'images']


class wpMediaForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = wpMedia
        fields = ['is_active', 'alt_text', 'width', 'height', 'file', 'author',
                  'mime_type', 'comment_status', 'wid', 'source_url',
                  'template', 'ping_status', 'caption', 'link', 'slug',
                  'modified', 'guid', 'description', 'modified_gmt', 'title',
                  'date_gmt', 'type', 'woostore']


class wpMediaSizeForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = wpMediaSize
        fields = ['is_active', 'name', 'file',
                  'mime_type', 'width', 'height', 'source_url', 'wpmedia']


class pfCountryForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfCountry
        fields = ['code', 'name']


class pfStateForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfState
        fields = ['code', 'name', 'pfcountry']


class pfSyncProductForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfSyncProduct
        fields = ['pid', 'external_id', 'variants', 'synced', 'pfstore']


class pfSyncVariantForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfSyncVariant
        fields = ['pid', 'external_id', 'synced', 'pfsyncproduct', 'files']


class pfSyncItemOptionForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfSyncItemOption
        fields = ['pid', 'value', 'pfsyncvariant']


class pfCatalogColorForm(businessCommonForm):
    form_layout = Layout(
        Div(
            HTML(generateColorSwatch('get_hex_code_clean')),
            css_class="col-md-3",
        ),
        Div(
            Fieldset('', 'code', 'label_clean', 'hex_code'),
            css_class="col-md-3"),
        Div(
            HTML("""<h4>Catalog Colours</h4>
                     <p>Lorem.</p>"""),
            css_class="col-md-4"),
    )

    class Meta:
        model = pfCatalogColor
        fields = ['code', 'label_clean', 'hex_code']


class pfCatalogSizeForm(businessCommonForm):
    form_layout = Layout(
        Div(
            Fieldset("", 'code', 'name', 'label_clean'),
            css_class="col-md-4"
        ),
        Div(
            Fieldset("", 'sort_group', 'sort_order'),
            css_class="col-md-4"
        ),
        Div(
            HTML("""<h4>Catalog Sizes</h4>
                     <p>Lorem.</p>"""),
            css_class="col-md-4"),
    )

    class Meta:
        model = pfCatalogSize
        fields = ['code', 'name', 'label_clean', 'sort_group', 'sort_order']


class pfCatalogFileSpecForm(businessCommonForm):

    class Meta:
        model = pfCatalogFileSpec
        fields = ['name', 'note', 'width', 'height',
                  'width_in', 'height_in', 'ratio', 'colorsystem']


class pfCatalogFileTypeForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfCatalogFileType
        fields = ['pid', 'title', 'additional_price', 'pfcatalogvariant']


class pfCatalogOptionTypeForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfCatalogOptionType
        fields = ['pid', 'title', 'type',
                  'additional_price', 'pfcatalogvariant']


class pfCatalogProductForm(businessCommonForm):
    form_layout = Layout(
        Div(
            Div(
                Thumbnail('image', 'model', caption=True),
                css_class="col-md-3"
            ),
            Div(
                HTML("<table class='table table-striped'>"),
                HTML("<tr><th>Brand</th><td>{{ object.brand }}<td></tr>"),
                HTML("<tr><th>Type</th><td>{{ object.ptype }}<td></tr>"),
                HTML(
                    "<tr><th>Variants</th><td>{{ object.variant_count }}<td></tr>"),
                HTML("<tr><th>Printful ID</th><td>{{ object.pid }}<td></tr>"),
                HTML(
                    "<tr><th>Active?</th><td>{{ object.is_active }}<td></tr>"),
                HTML("</table>"),
                # TODO Add colors and sizes display here.
                css_class="col-md-5"),
            Div(
                HTML("""<h4>Catalog Products</h4>
                         <p></p>"""),
                css_class="col-md-4"),
            css_class="row"
        )
    )

    class Meta:
        model = pfCatalogProduct
        exclude = [
            'is_active', 'pid', 'ptype',
            'brand', 'model', 'image', 'variant_count']


class pfCatalogVariantForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfCatalogVariant
        fields = ['is_active', 'pid', 'name',
                  'image', 'price', 'in_stock', 'weight', 'pfsize']


class pfPrintFileForm(businessCommonForm):
    form_layout = Layout()

    class Meta:
        model = pfPrintFile
        fields = ['pid', 'type', 'hash', 'url', 'filename', 'mime_type',
                  'size', 'width', 'height', 'dpi', 'status', 'created',
                  'thumbnail_url', 'visible', 'pfstore']
