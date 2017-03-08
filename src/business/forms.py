from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import *
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from django.contrib.auth import get_user_model
from .models import *

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

# Forms


class bzBrandForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(bzBrandForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'code',
                'name',
            ),
            Fieldset(
                'Relationships',
                'vendor',
                'outlet',
            ),
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = bzBrand
        fields = ['code', 'name', 'vendor', 'outlet', ]


class bzCreativeCollectionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(bzCreativeCollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'code',
                'name',
                'bzbrand',
            ),
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = bzCreativeCollection
        fields = "__all__"


class bzCreativeDesignForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(bzCreativeDesignForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'code',
                'name',
                'bzcreativecollection',
            ),
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = bzCreativeDesign
        fields = ['code', 'name', 'bzcreativecollection']


class bzCreativeLayoutForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(bzCreativeLayoutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'code',
                'name',
                'bzcreativecollection',
            ),
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = bzCreativeLayout
        fields = ['code', 'name', 'bzcreativecollection']


class bzCreativeRenderingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(bzCreativeRenderingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'bzcreativedesign',
                'bzcreativelayout',
            ),
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = bzCreativeRendering
        fields = ['bzcreativedesign', 'bzcreativelayout']


class bzProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(bzProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
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
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = bzProduct
        fields = ['code', 'name', 'status', 'bzDesign']


class bzProductVariantForm(forms.ModelForm):
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


class wooAttributeForm(forms.ModelForm):

    class Meta:
        model = wooAttribute
        fields = ['is_active', 'wid',
                  'name', 'slug', 'type', 'has_archives', 'store']


class wooCategoryForm(forms.ModelForm):

    class Meta:
        model = wooCategory
        fields = ['is_active', 'wid', 'name', 'slug', 'parent',
                  'description', 'display', 'count', 'image_id',
                  'image_date_created', 'store']


class wooImageForm(forms.ModelForm):

    class Meta:
        model = wooImage
        fields = ['is_active', 'wid', 'date_created', 'alt', 'position']


class wooProductForm(forms.ModelForm):

    class Meta:
        model = wooProduct
        fields = ['is_active', 'wid', 'slug', 'permalink', 'date_created',
                  'dimension_length', 'dimension_width', 'dimension_height',
                  'weight', 'reviews_allowed', 'woostore', 'shipping_class',
                  'tags', 'images']


class wooShippingClassForm(forms.ModelForm):

    class Meta:
        model = wooShippingClass
        fields = ['wid', 'name', 'slug', 'description', 'count']


class wooStoreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(wooStoreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'code',
                'timezone',
            ),
            Fieldset(
                'Details',
                'verify_ssl',
                'base_url',
                'consumer_secret',
            ),
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = wooStore
        fields = ['code', 'base_url', 'consumer_secret', 'timezone',
                  'verify_ssl']


class wooTagForm(forms.ModelForm):

    class Meta:
        model = wooTag
        fields = ['is_active', 'wid',
                  'name', 'slug', 'description', 'count', 'store']


class wooTermForm(forms.ModelForm):

    class Meta:
        model = wooTerm
        fields = ['wid', 'name', 'slug', 'menu_order',
                  'count', 'wr_tooltip', 'wr_label', 'productattribute']


class wooVariantForm(forms.ModelForm):

    class Meta:
        model = wooVariant
        fields = ['is_active', 'wid', 'date_created', 'permalink', 'sku',
                  'price', 'dimension_length', 'dimension_width',
                  'dimension_height', 'weight', 'shipping_class', 'images']


class wpMediaForm(forms.ModelForm):

    class Meta:
        model = wpMedia
        fields = ['is_active', 'alt_text', 'width', 'height', 'file', 'author',
                  'mime_type', 'comment_status', 'wid', 'source_url',
                  'template', 'ping_status', 'caption', 'link', 'slug',
                  'modified', 'guid', 'description', 'modified_gmt', 'title',
                  'date_gmt', 'type', 'woostore']


class wpMediaSizeForm(forms.ModelForm):

    class Meta:
        model = wpMediaSize
        fields = ['is_active', 'name', 'file',
                  'mime_type', 'width', 'height', 'source_url', 'wpmedia']


class pfCountryForm(forms.ModelForm):

    class Meta:
        model = pfCountry
        fields = ['code', 'name']


class pfStateForm(forms.ModelForm):

    class Meta:
        model = pfState
        fields = ['code', 'name', 'pfcountry']


class pfSyncProductForm(forms.ModelForm):

    class Meta:
        model = pfSyncProduct
        fields = ['pid', 'external_id', 'variants', 'synced', 'pfstore']


class pfSyncVariantForm(forms.ModelForm):

    class Meta:
        model = pfSyncVariant
        fields = ['pid', 'external_id', 'synced', 'pfsyncproduct', 'files']


class pfSyncItemOptionForm(forms.ModelForm):

    class Meta:
        model = pfSyncItemOption
        fields = ['pid', 'value', 'pfsyncvariant']


class pfCatalogColorForm(forms.ModelForm):

    class Meta:
        model = pfCatalogColor
        fields = ['code', 'label', 'label_clean', 'hex_code']


class pfCatalogSizeForm(forms.ModelForm):

    class Meta:
        model = pfCatalogSize
        fields = ['code', 'label', 'label_clean', 'sort_group', 'sort_order']


class pfCatalogFileSpecForm(forms.ModelForm):

    class Meta:
        model = pfCatalogFileSpec
        fields = ['name', 'note', 'width', 'height',
                  'width_in', 'height_in', 'ratio', 'colorsystem']


class pfCatalogFileTypeForm(forms.ModelForm):

    class Meta:
        model = pfCatalogFileType
        fields = ['pid', 'title', 'additional_price', 'pfcatalogvariant']


class pfCatalogOptionTypeForm(forms.ModelForm):

    class Meta:
        model = pfCatalogOptionType
        fields = ['pid', 'title', 'type',
                  'additional_price', 'pfcatalogvariant']


class pfCatalogProductForm(forms.ModelForm):

    class Meta:
        model = pfCatalogProduct
        fields = ['is_active', 'pid', 'type',
                  'brand', 'model', 'image', 'variant_count']


class pfCatalogVariantForm(forms.ModelForm):

    class Meta:
        model = pfCatalogVariant
        fields = ['is_active', 'pid', 'name',
                  'image', 'price', 'in_stock', 'weight', 'pfsize']


class pfStoreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(pfStoreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        layout_header = Layout(
            Div(
                Div(
                    HTML("""<h3>
                         {% if mode == 'create' %}Create New {{ object_name }}{% endif %}
                         {% if mode == 'update' %}{{ object.name }}{% endif %}
                         </h3>"""),
                    css_class="col-md-8"),
                Div(
                    Div("",
                        HTML(
                            """<a href="{{ action_list }}" role="button" class="btn btn-default"><span class="glyphicon glyphicon-menu-left" aria-hidden="true"></span> Back</a>"""),
                        Submit('update', 'Save', css_class="btn-success"),
                        css_class="btn-group pull-right", role="group"),
                    css_class="col-md-4"),
                css_class="row"),
        )

        self.helper.layout = Layout(
            layout_header,
            TabHolder(
                Tab('Basic Info',
                    Div(
                        Div(
                            Fieldset('', 'code', 'key'),
                            css_class="col-md-5"),
                        Div(
                            HTML(
                                """<h4>{{ object.name }}</h4>
                                {% if object.website %}<a href="{{ object.website }}" target="_blank">{{ object.website }}</a>{% endif %}"""),
                            css_class="col-md-7"),
                        css_class="row"),
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
                        css_class="row")),
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
                            css_class="col-md-4"
                        ),
                        css_class="row"),
                    ),
            )
        )

    class Meta:
        model = pfStore
        fields = ['code', 'key', 'packingslip_email',
                  'packingslip_phone', 'packingslip_message', ]


class pfPrintFileForm(forms.ModelForm):

    class Meta:
        model = pfPrintFile
        fields = ['pid', 'type', 'hash', 'url', 'filename', 'mime_type',
                  'size', 'width', 'height', 'dpi', 'status', 'created',
                  'thumbnail_url', 'visible', 'pfstore']
