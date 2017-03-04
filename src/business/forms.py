from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()


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

    class Meta:
        model = bzCreativeRendering
        fields = ['bzcreativedesign', 'bzcreativelayout']


class bzProductForm(forms.ModelForm):

    class Meta:
        model = bzProduct
        fields = ['code', 'name', 'status', 'bzDesign']


class bzProductVariantForm(forms.ModelForm):

    class Meta:
        model = bzProductVariant
        fields = ['code', 'is_active', 'bzproduct', 'pfcatalogvariant']


class wooAttributeForm(forms.ModelForm):

    class Meta:
        model = wooAttribute
        fields = ['is_active', 'wid',
                  'name', 'slug', 'type', 'has_archives', 'store']


class wooCategoryForm(forms.ModelForm):

    class Meta:
        model = wooCategory
        fields = ['is_active', 'wid', 'name', 'slug', 'parent',
                  'description', 'display', 'count', 'image_id', 'image_date_created', 'store']


class wooImageForm(forms.ModelForm):

    class Meta:
        model = wooImage
        fields = ['is_active', 'wid', 'date_created', 'alt', 'position']


class wooProductForm(forms.ModelForm):

    class Meta:
        model = wooProduct
        fields = ['is_active', 'wid', 'slug', 'permalink', 'date_created', 'dimension_length',
                  'dimension_width', 'dimension_height', 'weight', 'reviews_allowed', 'woostore', 'shipping_class', 'tags', 'images']


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
        fields = ['code', 'base_url', 'consumer_secret', 'timezone', 'verify_ssl']


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
        fields = ['is_active', 'wid', 'date_created', 'permalink', 'sku', 'price',
                  'dimension_length', 'dimension_width', 'dimension_height', 'weight', 'shipping_class', 'images']


class wpMediaForm(forms.ModelForm):

    class Meta:
        model = wpMedia
        fields = ['is_active', 'alt_text', 'width', 'height', 'file', 'author', 'mime_type', 'comment_status', 'wid', 'source_url',
                  'template', 'ping_status', 'caption', 'link', 'slug', 'modified', 'guid', 'description', 'modified_gmt', 'title', 'date_gmt', 'type', 'woostore']


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
        fields = ['pid', 'title', 'type', 'additional_price', 'pfcatalogvariant']


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
        self.helper.layout = Layout(
            Fieldset(
                '',
                'code',
                'name',
                'website',
                'consumer_key',
                'consumer_secret',
            ),
            FormActions(
                Submit('update', 'Save', css_class="btn-success"),
            )
        )

    class Meta:
        model = pfStore
        fields = ['code', 'name', 'website',
                  'consumer_key', 'consumer_secret']


class pfPrintFileForm(forms.ModelForm):

    class Meta:
        model = pfPrintFile
        fields = ['pid', 'type', 'hash', 'url', 'filename', 'mime_type', 'size',
                  'width', 'height', 'dpi', 'status', 'created', 'thumbnail_url', 'visible', 'pfstore']
