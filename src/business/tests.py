import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_bzbrand(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "vendor" not in defaults:
        defaults["vendor"] = create_pfstore()
    return bzBrand.objects.create(**defaults)


def create_bzcreativecollection(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "bzbrand" not in defaults:
        defaults["bzbrand"] = create_bzbrand()
    return bzCreativeCollection.objects.create(**defaults)


def create_bzcreativedesign(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "bzcreativecollection" not in defaults:
        defaults["bzcreativecollection"] = create_bzcreativecollection()
    return bzCreativeDesign.objects.create(**defaults)


def create_bzcreativelayout(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "bzcreativecollection" not in defaults:
        defaults["bzcreativecollection"] = create_bzcreativecollection()
    return bzCreativeLayout.objects.create(**defaults)


def create_bzcreativerendering(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults.update(**kwargs)
    if "bzcreativedesign" not in defaults:
        defaults["bzcreativedesign"] = create_bzcreativedesign()
    if "bzcreativelayout" not in defaults:
        defaults["bzcreativelayout"] = create_bzcreativelayout()
    return bzCreativeRendering.objects.create(**defaults)


def create_bzproduct(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["name"] = "name"
    defaults["status"] = "status"
    defaults.update(**kwargs)
    if "bzDesign" not in defaults:
        defaults["bzDesign"] = create_bzcreativedesign()
    return bzProduct.objects.create(**defaults)


def create_bzproductvariant(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["is_active"] = "is_active"
    defaults.update(**kwargs)
    if "bzproduct" not in defaults:
        defaults["bzproduct"] = create_bzproduct()
    if "pfcatalogvariant" not in defaults:
        defaults["pfcatalogvariant"] = create_pfcatalogvariant()
    return bzProductVariant.objects.create(**defaults)


def create_wooattribute(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["wid"] = "wid"
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["type"] = "type"
    defaults["has_archives"] = "has_archives"
    defaults.update(**kwargs)
    if "store" not in defaults:
        defaults["store"] = create_woostore()
    return wooAttribute.objects.create(**defaults)


def create_woocategory(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["wid"] = "wid"
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["parent"] = "parent"
    defaults["description"] = "description"
    defaults["display"] = "display"
    defaults["count"] = "count"
    defaults["image_id"] = "image_id"
    defaults["image_date_created"] = "image_date_created"
    defaults.update(**kwargs)
    if "store" not in defaults:
        defaults["store"] = create_woostore()
    return wooCategory.objects.create(**defaults)


def create_wooimage(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["wid"] = "wid"
    defaults["date_created"] = "date_created"
    defaults["alt"] = "alt"
    defaults["position"] = "position"
    defaults.update(**kwargs)
    return wooImage.objects.create(**defaults)


def create_wooproduct(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["wid"] = "wid"
    defaults["slug"] = "slug"
    defaults["permalink"] = "permalink"
    defaults["date_created"] = "date_created"
    defaults["dimension_length"] = "dimension_length"
    defaults["dimension_width"] = "dimension_width"
    defaults["dimension_height"] = "dimension_height"
    defaults["weight"] = "weight"
    defaults["reviews_allowed"] = "reviews_allowed"
    defaults.update(**kwargs)
    if "woostore" not in defaults:
        defaults["woostore"] = create_woostore()
    if "shipping_class" not in defaults:
        defaults["shipping_class"] = create_wooshippingclass()
    if "tags" not in defaults:
        defaults["tags"] = create_wootag()
    if "images" not in defaults:
        defaults["images"] = create_wooimage()
    return wooProduct.objects.create(**defaults)


def create_wooshippingclass(**kwargs):
    defaults = {}
    defaults["wid"] = "wid"
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["description"] = "description"
    defaults["count"] = "count"
    defaults.update(**kwargs)
    return wooShippingClass.objects.create(**defaults)


def create_woostore(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["base_url"] = "base_url"
    defaults["consumer_secret"] = "consumer_secret"
    defaults["timezone"] = "timezone"
    defaults["verify_ssl"] = "verify_ssl"
    defaults.update(**kwargs)
    return wooStore.objects.create(**defaults)


def create_wootag(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["wid"] = "wid"
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["description"] = "description"
    defaults["count"] = "count"
    defaults.update(**kwargs)
    if "store" not in defaults:
        defaults["store"] = create_woostore()
    return wooTag.objects.create(**defaults)


def create_wooterm(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["wid"] = "wid"
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["menu_order"] = "menu_order"
    defaults["count"] = "count"
    defaults["wr_tooltip"] = "wr_tooltip"
    defaults["wr_label"] = "wr_label"
    defaults.update(**kwargs)
    if "productattribute" not in defaults:
        defaults["productattribute"] = create_wooattribute()
    return wooTerm.objects.create(**defaults)


def create_woovariant(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["wid"] = "wid"
    defaults["date_created"] = "date_created"
    defaults["permalink"] = "permalink"
    defaults["sku"] = "sku"
    defaults["price"] = "price"
    defaults["dimension_length"] = "dimension_length"
    defaults["dimension_width"] = "dimension_width"
    defaults["dimension_height"] = "dimension_height"
    defaults["weight"] = "weight"
    defaults.update(**kwargs)
    if "shipping_class" not in defaults:
        defaults["shipping_class"] = create_wooshippingclass()
    if "images" not in defaults:
        defaults["images"] = create_wooimage()
    return wooVariant.objects.create(**defaults)


def create_wpmedia(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["alt_text"] = "alt_text"
    defaults["width"] = "width"
    defaults["height"] = "height"
    defaults["file"] = "file"
    defaults["author"] = "author"
    defaults["mime_type"] = "mime_type"
    defaults["comment_status"] = "comment_status"
    defaults["wid"] = "wid"
    defaults["source_url"] = "source_url"
    defaults["template"] = "template"
    defaults["ping_status"] = "ping_status"
    defaults["caption"] = "caption"
    defaults["link"] = "link"
    defaults["slug"] = "slug"
    defaults["modified"] = "modified"
    defaults["guid"] = "guid"
    defaults["description"] = "description"
    defaults["modified_gmt"] = "modified_gmt"
    defaults["title"] = "title"
    defaults["date_gmt"] = "date_gmt"
    defaults["type"] = "type"
    defaults.update(**kwargs)
    if "woostore" not in defaults:
        defaults["woostore"] = create_woostore()
    return wpMedia.objects.create(**defaults)


def create_wpmediasize(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["name"] = "name"
    defaults["file"] = "file"
    defaults["mime_type"] = "mime_type"
    defaults["width"] = "width"
    defaults["height"] = "height"
    defaults["source_url"] = "source_url"
    defaults.update(**kwargs)
    if "wpmedia" not in defaults:
        defaults["wpmedia"] = create_wpmedia()
    return wpMediaSize.objects.create(**defaults)


def create_pfcountry(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return pfCountry.objects.create(**defaults)


def create_pfstate(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "pfcountry" not in defaults:
        defaults["pfcountry"] = create_pfcountry()
    return pfState.objects.create(**defaults)


def create_pfsyncproduct(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["pid"] = "pid"
    defaults["external_id"] = "external_id"
    defaults["variants"] = "variants"
    defaults["synced"] = "synced"
    defaults.update(**kwargs)
    if "pfstore" not in defaults:
        defaults["pfstore"] = create_pfstore()
    return pfSyncProduct.objects.create(**defaults)


def create_pfsyncvariant(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["pid"] = "pid"
    defaults["external_id"] = "external_id"
    defaults["synced"] = "synced"
    defaults.update(**kwargs)
    if "pfsyncproduct" not in defaults:
        defaults["pfsyncproduct"] = create_pfsyncproduct()
    if "files" not in defaults:
        defaults["files"] = create_pfprintfile()
    return pfSyncVariant.objects.create(**defaults)


def create_pfsyncitemoption(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["pid"] = "pid"
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "pfsyncvariant" not in defaults:
        defaults["pfsyncvariant"] = create_pfsyncvariant()
    return pfSyncItemOption.objects.create(**defaults)


def create_pfcatalogcolor(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["label"] = "label"
    defaults["label_clean"] = "label_clean"
    defaults["hex_code"] = "hex_code"
    defaults.update(**kwargs)
    return pfCatalogColor.objects.create(**defaults)


def create_pfcatalogsize(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["label"] = "label"
    defaults["label_clean"] = "label_clean"
    defaults["sort_group"] = "sort_group"
    defaults["sort_order"] = "sort_order"
    defaults.update(**kwargs)
    return pfCatalogSize.objects.create(**defaults)


def create_pfcatalogfilespec(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["name"] = "name"
    defaults["note"] = "note"
    defaults["width"] = "width"
    defaults["height"] = "height"
    defaults["width_in"] = "width_in"
    defaults["height_in"] = "height_in"
    defaults["ratio"] = "ratio"
    defaults["colorsystem"] = "colorsystem"
    defaults.update(**kwargs)
    return pfCatalogFileSpec.objects.create(**defaults)


def create_pfcatalogfiletype(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["pid"] = "pid"
    defaults["title"] = "title"
    defaults["additional_price"] = "additional_price"
    defaults.update(**kwargs)
    if "pfcatalogvariant" not in defaults:
        defaults["pfcatalogvariant"] = create_pfcatalogvariant()
    return pfCatalogFileType.objects.create(**defaults)


def create_pfcatalogoptiontype(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["pid"] = "pid"
    defaults["title"] = "title"
    defaults["type"] = "type"
    defaults["additional_price"] = "additional_price"
    defaults.update(**kwargs)
    if "pfcatalogvariant" not in defaults:
        defaults["pfcatalogvariant"] = create_pfcatalogvariant()
    return pfCatalogOptionType.objects.create(**defaults)


def create_pfcatalogproduct(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["pid"] = "pid"
    defaults["type"] = "type"
    defaults["brand"] = "brand"
    defaults["model"] = "model"
    defaults["image"] = "image"
    defaults["variant_count"] = "variant_count"
    defaults.update(**kwargs)
    return pfCatalogProduct.objects.create(**defaults)


def create_pfcatalogvariant(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["is_active"] = "is_active"
    defaults["pid"] = "pid"
    defaults["name"] = "name"
    defaults["image"] = "image"
    defaults["price"] = "price"
    defaults["in_stock"] = "in_stock"
    defaults["weight"] = "weight"
    defaults.update(**kwargs)
    if "pfsize" not in defaults:
        defaults["pfsize"] = create_pfcatalogsize()
    return pfCatalogVariant.objects.create(**defaults)


def create_pfstore(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["code"] = "code"
    defaults["name"] = "name"
    defaults["website"] = "website"
    defaults["created"] = "created"
    defaults["consumer_key"] = "consumer_key"
    defaults["consumer_secret"] = "consumer_secret"
    defaults.update(**kwargs)
    return pfStore.objects.create(**defaults)


def create_pfprintfile(**kwargs):
    defaults = {}
    defaults["date_updated"] = "date_updated"
    defaults["pid"] = "pid"
    defaults["type"] = "type"
    defaults["hash"] = "hash"
    defaults["url"] = "url"
    defaults["filename"] = "filename"
    defaults["mime_type"] = "mime_type"
    defaults["size"] = "size"
    defaults["width"] = "width"
    defaults["height"] = "height"
    defaults["dpi"] = "dpi"
    defaults["status"] = "status"
    defaults["created"] = "created"
    defaults["thumbnail_url"] = "thumbnail_url"
    defaults["visible"] = "visible"
    defaults.update(**kwargs)
    if "pfstore" not in defaults:
        defaults["pfstore"] = create_pfstore()
    return pfPrintFile.objects.create(**defaults)


class bzBrandViewTest(unittest.TestCase):
    '''
    Tests for bzBrand
    '''

    def setUp(self):
        self.client = Client()

    def test_list_bzbrand(self):
        url = reverse('business_bzbrand_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bzbrand(self):
        url = reverse('business_bzbrand_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "vendor": create_pfstore().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bzbrand(self):
        bzbrand = create_bzbrand()
        url = reverse('business_bzbrand_detail', args=[bzbrand.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bzbrand(self):
        bzbrand = create_bzbrand()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "vendor": create_pfstore().pk,
        }
        url = reverse('business_bzbrand_update', args=[bzbrand.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class bzCreativeCollectionViewTest(unittest.TestCase):
    '''
    Tests for bzCreativeCollection
    '''

    def setUp(self):
        self.client = Client()

    def test_list_bzcreativecollection(self):
        url = reverse('business_bzcreativecollection_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bzcreativecollection(self):
        url = reverse('business_bzcreativecollection_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "bzbrand": create_bzbrand().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bzcreativecollection(self):
        bzcreativecollection = create_bzcreativecollection()
        url = reverse('business_bzcreativecollection_detail', args=[bzcreativecollection.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bzcreativecollection(self):
        bzcreativecollection = create_bzcreativecollection()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "bzbrand": create_bzbrand().pk,
        }
        url = reverse('business_bzcreativecollection_update', args=[bzcreativecollection.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class bzCreativeDesignViewTest(unittest.TestCase):
    '''
    Tests for bzCreativeDesign
    '''

    def setUp(self):
        self.client = Client()

    def test_list_bzcreativedesign(self):
        url = reverse('business_bzcreativedesign_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bzcreativedesign(self):
        url = reverse('business_bzcreativedesign_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "bzcreativecollection": create_bzcreativecollection().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bzcreativedesign(self):
        bzcreativedesign = create_bzcreativedesign()
        url = reverse('business_bzcreativedesign_detail', args=[bzcreativedesign.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bzcreativedesign(self):
        bzcreativedesign = create_bzcreativedesign()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "bzcreativecollection": create_bzcreativecollection().pk,
        }
        url = reverse('business_bzcreativedesign_update', args=[bzcreativedesign.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class bzCreativeLayoutViewTest(unittest.TestCase):
    '''
    Tests for bzCreativeLayout
    '''

    def setUp(self):
        self.client = Client()

    def test_list_bzcreativelayout(self):
        url = reverse('business_bzcreativelayout_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bzcreativelayout(self):
        url = reverse('business_bzcreativelayout_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "bzcreativecollection": create_bzcreativecollection().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bzcreativelayout(self):
        bzcreativelayout = create_bzcreativelayout()
        url = reverse('business_bzcreativelayout_detail', args=[bzcreativelayout.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bzcreativelayout(self):
        bzcreativelayout = create_bzcreativelayout()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "bzcreativecollection": create_bzcreativecollection().pk,
        }
        url = reverse('business_bzcreativelayout_update', args=[bzcreativelayout.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class bzCreativeRenderingViewTest(unittest.TestCase):
    '''
    Tests for bzCreativeRendering
    '''

    def setUp(self):
        self.client = Client()

    def test_list_bzcreativerendering(self):
        url = reverse('business_bzcreativerendering_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bzcreativerendering(self):
        url = reverse('business_bzcreativerendering_create')
        data = {
            "date_updated": "date_updated",
            "bzcreativedesign": create_bzcreativedesign().pk,
            "bzcreativelayout": create_bzcreativelayout().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bzcreativerendering(self):
        bzcreativerendering = create_bzcreativerendering()
        url = reverse('business_bzcreativerendering_detail', args=[bzcreativerendering.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bzcreativerendering(self):
        bzcreativerendering = create_bzcreativerendering()
        data = {
            "date_updated": "date_updated",
            "bzcreativedesign": create_bzcreativedesign().pk,
            "bzcreativelayout": create_bzcreativelayout().pk,
        }
        url = reverse('business_bzcreativerendering_update', args=[bzcreativerendering.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class bzProductViewTest(unittest.TestCase):
    '''
    Tests for bzProduct
    '''

    def setUp(self):
        self.client = Client()

    def test_list_bzproduct(self):
        url = reverse('business_bzproduct_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bzproduct(self):
        url = reverse('business_bzproduct_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "status": "status",
            "bzDesign": create_bzcreativedesign().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bzproduct(self):
        bzproduct = create_bzproduct()
        url = reverse('business_bzproduct_detail', args=[bzproduct.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bzproduct(self):
        bzproduct = create_bzproduct()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "status": "status",
            "bzDesign": create_bzcreativedesign().pk,
        }
        url = reverse('business_bzproduct_update', args=[bzproduct.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class bzProductVariantViewTest(unittest.TestCase):
    '''
    Tests for bzProductVariant
    '''

    def setUp(self):
        self.client = Client()

    def test_list_bzproductvariant(self):
        url = reverse('business_bzproductvariant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bzproductvariant(self):
        url = reverse('business_bzproductvariant_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "is_active": "is_active",
            "bzproduct": create_bzproduct().pk,
            "pfcatalogvariant": create_pfcatalogvariant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bzproductvariant(self):
        bzproductvariant = create_bzproductvariant()
        url = reverse('business_bzproductvariant_detail', args=[bzproductvariant.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bzproductvariant(self):
        bzproductvariant = create_bzproductvariant()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "is_active": "is_active",
            "bzproduct": create_bzproduct().pk,
            "pfcatalogvariant": create_pfcatalogvariant().pk,
        }
        url = reverse('business_bzproductvariant_update', args=[bzproductvariant.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooAttributeViewTest(unittest.TestCase):
    '''
    Tests for wooAttribute
    '''

    def setUp(self):
        self.client = Client()

    def test_list_wooattribute(self):
        url = reverse('business_wooattribute_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wooattribute(self):
        url = reverse('business_wooattribute_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "type": "type",
            "has_archives": "has_archives",
            "store": create_woostore().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wooattribute(self):
        wooattribute = create_wooattribute()
        url = reverse('business_wooattribute_detail', args=[wooattribute.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wooattribute(self):
        wooattribute = create_wooattribute()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "type": "type",
            "has_archives": "has_archives",
            "store": create_woostore().pk,
        }
        url = reverse('business_wooattribute_update', args=[wooattribute.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooCategoryViewTest(unittest.TestCase):
    '''
    Tests for wooCategory
    '''

    def setUp(self):
        self.client = Client()

    def test_list_woocategory(self):
        url = reverse('business_woocategory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_woocategory(self):
        url = reverse('business_woocategory_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "parent": "parent",
            "description": "description",
            "display": "display",
            "count": "count",
            "image_id": "image_id",
            "image_date_created": "image_date_created",
            "store": create_woostore().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_woocategory(self):
        woocategory = create_woocategory()
        url = reverse('business_woocategory_detail', args=[woocategory.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_woocategory(self):
        woocategory = create_woocategory()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "parent": "parent",
            "description": "description",
            "display": "display",
            "count": "count",
            "image_id": "image_id",
            "image_date_created": "image_date_created",
            "store": create_woostore().pk,
        }
        url = reverse('business_woocategory_update', args=[woocategory.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooImageViewTest(unittest.TestCase):
    '''
    Tests for wooImage
    '''

    def setUp(self):
        self.client = Client()

    def test_list_wooimage(self):
        url = reverse('business_wooimage_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wooimage(self):
        url = reverse('business_wooimage_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "date_created": "date_created",
            "alt": "alt",
            "position": "position",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wooimage(self):
        wooimage = create_wooimage()
        url = reverse('business_wooimage_detail', args=[wooimage.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wooimage(self):
        wooimage = create_wooimage()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "date_created": "date_created",
            "alt": "alt",
            "position": "position",
        }
        url = reverse('business_wooimage_update', args=[wooimage.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooProductViewTest(unittest.TestCase):
    '''
    Tests for wooProduct
    '''

    def setUp(self):
        self.client = Client()

    def test_list_wooproduct(self):
        url = reverse('business_wooproduct_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wooproduct(self):
        url = reverse('business_wooproduct_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "slug": "slug",
            "permalink": "permalink",
            "date_created": "date_created",
            "dimension_length": "dimension_length",
            "dimension_width": "dimension_width",
            "dimension_height": "dimension_height",
            "weight": "weight",
            "reviews_allowed": "reviews_allowed",
            "woostore": create_woostore().pk,
            "shipping_class": create_wooshippingclass().pk,
            "tags": create_wootag().pk,
            "images": create_wooimage().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wooproduct(self):
        wooproduct = create_wooproduct()
        url = reverse('business_wooproduct_detail', args=[wooproduct.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wooproduct(self):
        wooproduct = create_wooproduct()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "slug": "slug",
            "permalink": "permalink",
            "date_created": "date_created",
            "dimension_length": "dimension_length",
            "dimension_width": "dimension_width",
            "dimension_height": "dimension_height",
            "weight": "weight",
            "reviews_allowed": "reviews_allowed",
            "woostore": create_woostore().pk,
            "shipping_class": create_wooshippingclass().pk,
            "tags": create_wootag().pk,
            "images": create_wooimage().pk,
        }
        url = reverse('business_wooproduct_update', args=[wooproduct.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooShippingClassViewTest(unittest.TestCase):
    '''
    Tests for wooShippingClass
    '''

    def setUp(self):
        self.client = Client()

    def test_list_wooshippingclass(self):
        url = reverse('business_wooshippingclass_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wooshippingclass(self):
        url = reverse('business_wooshippingclass_create')
        data = {
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "description": "description",
            "count": "count",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wooshippingclass(self):
        wooshippingclass = create_wooshippingclass()
        url = reverse('business_wooshippingclass_detail', args=[wooshippingclass.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wooshippingclass(self):
        wooshippingclass = create_wooshippingclass()
        data = {
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "description": "description",
            "count": "count",
        }
        url = reverse('business_wooshippingclass_update', args=[wooshippingclass.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooStoreViewTest(unittest.TestCase):
    '''
    Tests for wooStore
    '''

    def setUp(self):
        self.client = Client()

    def test_list_woostore(self):
        url = reverse('business_woostore_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_woostore(self):
        url = reverse('business_woostore_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "base_url": "base_url",
            "consumer_secret": "consumer_secret",
            "timezone": "timezone",
            "verify_ssl": "verify_ssl",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_woostore(self):
        woostore = create_woostore()
        url = reverse('business_woostore_detail', args=[woostore.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_woostore(self):
        woostore = create_woostore()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "base_url": "base_url",
            "consumer_secret": "consumer_secret",
            "timezone": "timezone",
            "verify_ssl": "verify_ssl",
        }
        url = reverse('business_woostore_update', args=[woostore.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooTagViewTest(unittest.TestCase):
    '''
    Tests for wooTag
    '''

    def setUp(self):
        self.client = Client()

    def test_list_wootag(self):
        url = reverse('business_wootag_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wootag(self):
        url = reverse('business_wootag_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "description": "description",
            "count": "count",
            "store": create_woostore().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wootag(self):
        wootag = create_wootag()
        url = reverse('business_wootag_detail', args=[wootag.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wootag(self):
        wootag = create_wootag()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "description": "description",
            "count": "count",
            "store": create_woostore().pk,
        }
        url = reverse('business_wootag_update', args=[wootag.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooTermViewTest(unittest.TestCase):
    '''
    Tests for wooTerm
    '''

    def setUp(self):
        self.client = Client()

    def test_list_wooterm(self):
        url = reverse('business_wooterm_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wooterm(self):
        url = reverse('business_wooterm_create')
        data = {
            "date_updated": "date_updated",
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "menu_order": "menu_order",
            "count": "count",
            "wr_tooltip": "wr_tooltip",
            "wr_label": "wr_label",
            "productattribute": create_wooattribute().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wooterm(self):
        wooterm = create_wooterm()
        url = reverse('business_wooterm_detail', args=[wooterm.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wooterm(self):
        wooterm = create_wooterm()
        data = {
            "date_updated": "date_updated",
            "wid": "wid",
            "name": "name",
            "slug": "slug",
            "menu_order": "menu_order",
            "count": "count",
            "wr_tooltip": "wr_tooltip",
            "wr_label": "wr_label",
            "productattribute": create_wooattribute().pk,
        }
        url = reverse('business_wooterm_update', args=[wooterm.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wooVariantViewTest(unittest.TestCase):
    '''
    Tests for wooVariant
    '''

    def setUp(self):
        self.client = Client()

    def test_list_woovariant(self):
        url = reverse('business_woovariant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_woovariant(self):
        url = reverse('business_woovariant_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "date_created": "date_created",
            "permalink": "permalink",
            "sku": "sku",
            "price": "price",
            "dimension_length": "dimension_length",
            "dimension_width": "dimension_width",
            "dimension_height": "dimension_height",
            "weight": "weight",
            "shipping_class": create_wooshippingclass().pk,
            "images": create_wooimage().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_woovariant(self):
        woovariant = create_woovariant()
        url = reverse('business_woovariant_detail', args=[woovariant.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_woovariant(self):
        woovariant = create_woovariant()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "wid": "wid",
            "date_created": "date_created",
            "permalink": "permalink",
            "sku": "sku",
            "price": "price",
            "dimension_length": "dimension_length",
            "dimension_width": "dimension_width",
            "dimension_height": "dimension_height",
            "weight": "weight",
            "shipping_class": create_wooshippingclass().pk,
            "images": create_wooimage().pk,
        }
        url = reverse('business_woovariant_update', args=[woovariant.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wpMediaViewTest(unittest.TestCase):
    '''
    Tests for wpMedia
    '''

    def setUp(self):
        self.client = Client()

    def test_list_wpmedia(self):
        url = reverse('business_wpmedia_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wpmedia(self):
        url = reverse('business_wpmedia_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "alt_text": "alt_text",
            "width": "width",
            "height": "height",
            "file": "file",
            "author": "author",
            "mime_type": "mime_type",
            "comment_status": "comment_status",
            "wid": "wid",
            "source_url": "source_url",
            "template": "template",
            "ping_status": "ping_status",
            "caption": "caption",
            "link": "link",
            "slug": "slug",
            "modified": "modified",
            "guid": "guid",
            "description": "description",
            "modified_gmt": "modified_gmt",
            "title": "title",
            "date_gmt": "date_gmt",
            "type": "type",
            "woostore": create_woostore().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wpmedia(self):
        wpmedia = create_wpmedia()
        url = reverse('business_wpmedia_detail', args=[wpmedia.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wpmedia(self):
        wpmedia = create_wpmedia()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "alt_text": "alt_text",
            "width": "width",
            "height": "height",
            "file": "file",
            "author": "author",
            "mime_type": "mime_type",
            "comment_status": "comment_status",
            "wid": "wid",
            "source_url": "source_url",
            "template": "template",
            "ping_status": "ping_status",
            "caption": "caption",
            "link": "link",
            "slug": "slug",
            "modified": "modified",
            "guid": "guid",
            "description": "description",
            "modified_gmt": "modified_gmt",
            "title": "title",
            "date_gmt": "date_gmt",
            "type": "type",
            "woostore": create_woostore().pk,
        }
        url = reverse('business_wpmedia_update', args=[wpmedia.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class wpMediaSizeViewTest(unittest.TestCase):
    '''
    Tests for wpMediaSize
    '''

    def setUp(self):
        self.client = Client()

    def test_list_wpmediasize(self):
        url = reverse('business_wpmediasize_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wpmediasize(self):
        url = reverse('business_wpmediasize_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "name": "name",
            "file": "file",
            "mime_type": "mime_type",
            "width": "width",
            "height": "height",
            "source_url": "source_url",
            "wpmedia": create_wpmedia().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wpmediasize(self):
        wpmediasize = create_wpmediasize()
        url = reverse('business_wpmediasize_detail', args=[wpmediasize.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wpmediasize(self):
        wpmediasize = create_wpmediasize()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "name": "name",
            "file": "file",
            "mime_type": "mime_type",
            "width": "width",
            "height": "height",
            "source_url": "source_url",
            "wpmedia": create_wpmedia().pk,
        }
        url = reverse('business_wpmediasize_update', args=[wpmediasize.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfCountryViewTest(unittest.TestCase):
    '''
    Tests for pfCountry
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfcountry(self):
        url = reverse('business_pfcountry_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfcountry(self):
        url = reverse('business_pfcountry_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfcountry(self):
        pfcountry = create_pfcountry()
        url = reverse('business_pfcountry_detail', args=[pfcountry.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfcountry(self):
        pfcountry = create_pfcountry()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
        }
        url = reverse('business_pfcountry_update', args=[pfcountry.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfStateViewTest(unittest.TestCase):
    '''
    Tests for pfState
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfstate(self):
        url = reverse('business_pfstate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfstate(self):
        url = reverse('business_pfstate_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "pfcountry": create_pfcountry().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfstate(self):
        pfstate = create_pfstate()
        url = reverse('business_pfstate_detail', args=[pfstate.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfstate(self):
        pfstate = create_pfstate()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "pfcountry": create_pfcountry().pk,
        }
        url = reverse('business_pfstate_update', args=[pfstate.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfSyncProductViewTest(unittest.TestCase):
    '''
    Tests for pfSyncProduct
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfsyncproduct(self):
        url = reverse('business_pfsyncproduct_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfsyncproduct(self):
        url = reverse('business_pfsyncproduct_create')
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "external_id": "external_id",
            "variants": "variants",
            "synced": "synced",
            "pfstore": create_pfstore().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfsyncproduct(self):
        pfsyncproduct = create_pfsyncproduct()
        url = reverse('business_pfsyncproduct_detail', args=[pfsyncproduct.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfsyncproduct(self):
        pfsyncproduct = create_pfsyncproduct()
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "external_id": "external_id",
            "variants": "variants",
            "synced": "synced",
            "pfstore": create_pfstore().pk,
        }
        url = reverse('business_pfsyncproduct_update', args=[pfsyncproduct.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfSyncVariantViewTest(unittest.TestCase):
    '''
    Tests for pfSyncVariant
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfsyncvariant(self):
        url = reverse('business_pfsyncvariant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfsyncvariant(self):
        url = reverse('business_pfsyncvariant_create')
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "external_id": "external_id",
            "synced": "synced",
            "pfsyncproduct": create_pfsyncproduct().pk,
            "files": create_pfprintfile().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfsyncvariant(self):
        pfsyncvariant = create_pfsyncvariant()
        url = reverse('business_pfsyncvariant_detail', args=[pfsyncvariant.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfsyncvariant(self):
        pfsyncvariant = create_pfsyncvariant()
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "external_id": "external_id",
            "synced": "synced",
            "pfsyncproduct": create_pfsyncproduct().pk,
            "files": create_pfprintfile().pk,
        }
        url = reverse('business_pfsyncvariant_update', args=[pfsyncvariant.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfSyncItemOptionViewTest(unittest.TestCase):
    '''
    Tests for pfSyncItemOption
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfsyncitemoption(self):
        url = reverse('business_pfsyncitemoption_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfsyncitemoption(self):
        url = reverse('business_pfsyncitemoption_create')
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "value": "value",
            "pfsyncvariant": create_pfsyncvariant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfsyncitemoption(self):
        pfsyncitemoption = create_pfsyncitemoption()
        url = reverse('business_pfsyncitemoption_detail', args=[pfsyncitemoption.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfsyncitemoption(self):
        pfsyncitemoption = create_pfsyncitemoption()
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "value": "value",
            "pfsyncvariant": create_pfsyncvariant().pk,
        }
        url = reverse('business_pfsyncitemoption_update', args=[pfsyncitemoption.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfCatalogColorViewTest(unittest.TestCase):
    '''
    Tests for pfCatalogColor
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfcatalogcolor(self):
        url = reverse('business_pfcatalogcolor_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfcatalogcolor(self):
        url = reverse('business_pfcatalogcolor_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "label": "label",
            "label_clean": "label_clean",
            "hex_code": "hex_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfcatalogcolor(self):
        pfcatalogcolor = create_pfcatalogcolor()
        url = reverse('business_pfcatalogcolor_detail', args=[pfcatalogcolor.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfcatalogcolor(self):
        pfcatalogcolor = create_pfcatalogcolor()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "label": "label",
            "label_clean": "label_clean",
            "hex_code": "hex_code",
        }
        url = reverse('business_pfcatalogcolor_update', args=[pfcatalogcolor.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfCatalogSizeViewTest(unittest.TestCase):
    '''
    Tests for pfCatalogSize
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfcatalogsize(self):
        url = reverse('business_pfcatalogsize_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfcatalogsize(self):
        url = reverse('business_pfcatalogsize_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "label": "label",
            "label_clean": "label_clean",
            "sort_group": "sort_group",
            "sort_order": "sort_order",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfcatalogsize(self):
        pfcatalogsize = create_pfcatalogsize()
        url = reverse('business_pfcatalogsize_detail', args=[pfcatalogsize.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfcatalogsize(self):
        pfcatalogsize = create_pfcatalogsize()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "label": "label",
            "label_clean": "label_clean",
            "sort_group": "sort_group",
            "sort_order": "sort_order",
        }
        url = reverse('business_pfcatalogsize_update', args=[pfcatalogsize.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfCatalogFileSpecViewTest(unittest.TestCase):
    '''
    Tests for pfCatalogFileSpec
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfcatalogfilespec(self):
        url = reverse('business_pfcatalogfilespec_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfcatalogfilespec(self):
        url = reverse('business_pfcatalogfilespec_create')
        data = {
            "date_updated": "date_updated",
            "name": "name",
            "note": "note",
            "width": "width",
            "height": "height",
            "width_in": "width_in",
            "height_in": "height_in",
            "ratio": "ratio",
            "colorsystem": "colorsystem",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfcatalogfilespec(self):
        pfcatalogfilespec = create_pfcatalogfilespec()
        url = reverse('business_pfcatalogfilespec_detail', args=[pfcatalogfilespec.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfcatalogfilespec(self):
        pfcatalogfilespec = create_pfcatalogfilespec()
        data = {
            "date_updated": "date_updated",
            "name": "name",
            "note": "note",
            "width": "width",
            "height": "height",
            "width_in": "width_in",
            "height_in": "height_in",
            "ratio": "ratio",
            "colorsystem": "colorsystem",
        }
        url = reverse('business_pfcatalogfilespec_update', args=[pfcatalogfilespec.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfCatalogFileTypeViewTest(unittest.TestCase):
    '''
    Tests for pfCatalogFileType
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfcatalogfiletype(self):
        url = reverse('business_pfcatalogfiletype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfcatalogfiletype(self):
        url = reverse('business_pfcatalogfiletype_create')
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "title": "title",
            "additional_price": "additional_price",
            "pfcatalogvariant": create_pfcatalogvariant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfcatalogfiletype(self):
        pfcatalogfiletype = create_pfcatalogfiletype()
        url = reverse('business_pfcatalogfiletype_detail', args=[pfcatalogfiletype.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfcatalogfiletype(self):
        pfcatalogfiletype = create_pfcatalogfiletype()
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "title": "title",
            "additional_price": "additional_price",
            "pfcatalogvariant": create_pfcatalogvariant().pk,
        }
        url = reverse('business_pfcatalogfiletype_update', args=[pfcatalogfiletype.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfCatalogOptionTypeViewTest(unittest.TestCase):
    '''
    Tests for pfCatalogOptionType
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfcatalogoptiontype(self):
        url = reverse('business_pfcatalogoptiontype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfcatalogoptiontype(self):
        url = reverse('business_pfcatalogoptiontype_create')
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "title": "title",
            "type": "type",
            "additional_price": "additional_price",
            "pfcatalogvariant": create_pfcatalogvariant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfcatalogoptiontype(self):
        pfcatalogoptiontype = create_pfcatalogoptiontype()
        url = reverse('business_pfcatalogoptiontype_detail', args=[pfcatalogoptiontype.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfcatalogoptiontype(self):
        pfcatalogoptiontype = create_pfcatalogoptiontype()
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "title": "title",
            "type": "type",
            "additional_price": "additional_price",
            "pfcatalogvariant": create_pfcatalogvariant().pk,
        }
        url = reverse('business_pfcatalogoptiontype_update', args=[pfcatalogoptiontype.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfCatalogProductViewTest(unittest.TestCase):
    '''
    Tests for pfCatalogProduct
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfcatalogproduct(self):
        url = reverse('business_pfcatalogproduct_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfcatalogproduct(self):
        url = reverse('business_pfcatalogproduct_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "pid": "pid",
            "type": "type",
            "brand": "brand",
            "model": "model",
            "image": "image",
            "variant_count": "variant_count",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfcatalogproduct(self):
        pfcatalogproduct = create_pfcatalogproduct()
        url = reverse('business_pfcatalogproduct_detail', args=[pfcatalogproduct.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfcatalogproduct(self):
        pfcatalogproduct = create_pfcatalogproduct()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "pid": "pid",
            "type": "type",
            "brand": "brand",
            "model": "model",
            "image": "image",
            "variant_count": "variant_count",
        }
        url = reverse('business_pfcatalogproduct_update', args=[pfcatalogproduct.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfCatalogVariantViewTest(unittest.TestCase):
    '''
    Tests for pfCatalogVariant
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfcatalogvariant(self):
        url = reverse('business_pfcatalogvariant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfcatalogvariant(self):
        url = reverse('business_pfcatalogvariant_create')
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "pid": "pid",
            "name": "name",
            "image": "image",
            "price": "price",
            "in_stock": "in_stock",
            "weight": "weight",
            "pfsize": create_pfcatalogsize().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfcatalogvariant(self):
        pfcatalogvariant = create_pfcatalogvariant()
        url = reverse('business_pfcatalogvariant_detail', args=[pfcatalogvariant.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfcatalogvariant(self):
        pfcatalogvariant = create_pfcatalogvariant()
        data = {
            "date_updated": "date_updated",
            "is_active": "is_active",
            "pid": "pid",
            "name": "name",
            "image": "image",
            "price": "price",
            "in_stock": "in_stock",
            "weight": "weight",
            "pfsize": create_pfcatalogsize().pk,
        }
        url = reverse('business_pfcatalogvariant_update', args=[pfcatalogvariant.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfStoreViewTest(unittest.TestCase):
    '''
    Tests for pfStore
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfstore(self):
        url = reverse('business_pfstore_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfstore(self):
        url = reverse('business_pfstore_create')
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "website": "website",
            "created": "created",
            "consumer_key": "consumer_key",
            "consumer_secret": "consumer_secret",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfstore(self):
        pfstore = create_pfstore()
        url = reverse('business_pfstore_detail', args=[pfstore.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfstore(self):
        pfstore = create_pfstore()
        data = {
            "date_updated": "date_updated",
            "code": "code",
            "name": "name",
            "website": "website",
            "created": "created",
            "consumer_key": "consumer_key",
            "consumer_secret": "consumer_secret",
        }
        url = reverse('business_pfstore_update', args=[pfstore.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pfPrintFileViewTest(unittest.TestCase):
    '''
    Tests for pfPrintFile
    '''

    def setUp(self):
        self.client = Client()

    def test_list_pfprintfile(self):
        url = reverse('business_pfprintfile_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pfprintfile(self):
        url = reverse('business_pfprintfile_create')
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "type": "type",
            "hash": "hash",
            "url": "url",
            "filename": "filename",
            "mime_type": "mime_type",
            "size": "size",
            "width": "width",
            "height": "height",
            "dpi": "dpi",
            "status": "status",
            "created": "created",
            "thumbnail_url": "thumbnail_url",
            "visible": "visible",
            "pfstore": create_pfstore().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pfprintfile(self):
        pfprintfile = create_pfprintfile()
        url = reverse('business_pfprintfile_detail', args=[pfprintfile.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pfprintfile(self):
        pfprintfile = create_pfprintfile()
        data = {
            "date_updated": "date_updated",
            "pid": "pid",
            "type": "type",
            "hash": "hash",
            "url": "url",
            "filename": "filename",
            "mime_type": "mime_type",
            "size": "size",
            "width": "width",
            "height": "height",
            "dpi": "dpi",
            "status": "status",
            "created": "created",
            "thumbnail_url": "thumbnail_url",
            "visible": "visible",
            "pfstore": create_pfstore().pk,
        }
        url = reverse('business_pfprintfile_update', args=[pfprintfile.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
