import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Product, ProductImage, ProductCategory, ImageType, ProductInfo, ContentType, InfoContent, Variant, VariantOption, VariantTemplate, TemplateSpace, LayerType, SpaceLayer
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


def create_product(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["id"] = "id"
    defaults["uid"] = "uid"
    defaults["name"] = "name"
    defaults["is_featured"] = "is_featured"
    defaults["is_coming_soon"] = "is_coming_soon"
    defaults["has_available_product_variants"] = "has_available_product_variants"
    defaults["has_product_templates"] = "has_product_templates"
    defaults["description"] = "description"
    defaults["max_zoom"] = "max_zoom"
    defaults["priceinfo_price"] = "priceinfo_price"
    defaults["priceinfo_currencycode"] = "priceinfo_currencycode"
    defaults["priceinfo_currencydigits"] = "priceinfo_currencydigits"
    defaults["priceinfo_currencyformat"] = "priceinfo_currencyformat"
    defaults["priceinfo_formattedprice"] = "priceinfo_formattedprice"
    defaults["retailprice_price"] = "retailprice_price"
    defaults["retailprice_currencycode"] = "retailprice_currencycode"
    defaults["retailprice_currencydigits"] = "retailprice_currencydigits"
    defaults["retailprice_currencyformat"] = "retailprice_currencyformat"
    defaults["retailprice_formattedprice"] = "retailprice_formattedprice"
    defaults.update(**kwargs)
    if "categories" not in defaults:
        defaults["categories"] = create_productcategory()
    return Product.objects.create(**defaults)


def create_productimage(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["id"] = "id"
    defaults["index"] = "index"
    defaults["url"] = "url"
    defaults.update(**kwargs)
    if "product" not in defaults:
        defaults["product"] = create_product()
    if "image_type" not in defaults:
        defaults["image_type"] = create_imagetype()
    return ProductImage.objects.create(**defaults)


def create_productcategory(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["id"] = "id"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return ProductCategory.objects.create(**defaults)


def create_imagetype(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return ImageType.objects.create(**defaults)


def create_productinfo(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["key"] = "key"
    defaults["index"] = "index"
    defaults.update(**kwargs)
    if "product" not in defaults:
        defaults["product"] = create_product()
    if "content_type" not in defaults:
        defaults["content_type"] = create_contenttype()
    return ProductInfo.objects.create(**defaults)


def create_contenttype(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_infocontent(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["text"] = "text"
    defaults.update(**kwargs)
    if "productinfo" not in defaults:
        defaults["productinfo"] = create_productinfo()
    return InfoContent.objects.create(**defaults)


def create_variant(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["sku"] = "sku"
    defaults["has_templates"] = "has_templates"
    defaults["max_images"] = "max_images"
    defaults["priceinfo_price"] = "priceinfo_price"
    defaults["priceinfo_currencycode"] = "priceinfo_currencycode"
    defaults["priceinfo_currencydigits"] = "priceinfo_currencydigits"
    defaults["priceinfo_currencyformat"] = "priceinfo_currencyformat"
    defaults["priceinfo_formattedprice"] = "priceinfo_formattedprice"
    defaults.update(**kwargs)
    if "product" not in defaults:
        defaults["product"] = create_product()
    return Variant.objects.create(**defaults)


def create_variantoption(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["option_id"] = "option_id"
    defaults["name"] = "name"
    defaults["sort_value"] = "sort_value"
    defaults["value"] = "value"
    defaults["value_id"] = "value_id"
    defaults["image_type"] = "image_type"
    defaults["image_url"] = "image_url"
    defaults.update(**kwargs)
    if "variant" not in defaults:
        defaults["variant"] = create_variant()
    return VariantOption.objects.create(**defaults)


def create_VariantTemplate(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["name"] = "name"
    defaults["is_default"] = "is_default"
    defaults["image_url"] = "image_url"
    defaults.update(**kwargs)
    if "variant" not in defaults:
        defaults["variant"] = create_variant()
    return VariantTemplate.objects.create(**defaults)


def create_templatespace(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["id"] = "id"
    defaults["index"] = "index"
    defaults.update(**kwargs)
    if "VariantTemplate" not in defaults:
        defaults["VariantTemplate"] = create_VariantTemplate()
    return TemplateSpace.objects.create(**defaults)


def create_layertype(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return LayerType.objects.create(**defaults)


def create_spacelayer(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["include_in_print"] = "include_in_print"
    defaults["x1"] = "x1"
    defaults["x2"] = "x2"
    defaults["y1"] = "y1"
    defaults["y2"] = "y2"
    defaults["zIndex"] = "zIndex"
    defaults.update(**kwargs)
    if "templatespace" not in defaults:
        defaults["templatespace"] = create_templatespace()
    if "layer_type" not in defaults:
        defaults["layer_type"] = create_layertype()
    return SpaceLayer.objects.create(**defaults)


class ProductViewTest(unittest.TestCase):
    '''
    Tests for Product
    '''
    def setUp(self):
        self.client = Client()

    def test_list_product(self):
        url = reverse('api_gooten_product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        url = reverse('api_gooten_product_create')
        data = {
            "slug": "slug",
            "id": "id",
            "uid": "uid",
            "name": "name",
            "is_featured": "is_featured",
            "is_coming_soon": "is_coming_soon",
            "has_available_product_variants": "has_available_product_variants",
            "has_product_templates": "has_product_templates",
            "description": "description",
            "max_zoom": "max_zoom",
            "priceinfo_price": "priceinfo_price",
            "priceinfo_currencycode": "priceinfo_currencycode",
            "priceinfo_currencydigits": "priceinfo_currencydigits",
            "priceinfo_currencyformat": "priceinfo_currencyformat",
            "priceinfo_formattedprice": "priceinfo_formattedprice",
            "retailprice_price": "retailprice_price",
            "retailprice_currencycode": "retailprice_currencycode",
            "retailprice_currencydigits": "retailprice_currencydigits",
            "retailprice_currencyformat": "retailprice_currencyformat",
            "retailprice_formattedprice": "retailprice_formattedprice",
            "categories": create_productcategory().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_product(self):
        product = create_product()
        url = reverse('api_gooten_product_detail', args=[product.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product = create_product()
        data = {
            "slug": "slug",
            "id": "id",
            "uid": "uid",
            "name": "name",
            "is_featured": "is_featured",
            "is_coming_soon": "is_coming_soon",
            "has_available_product_variants": "has_available_product_variants",
            "has_product_templates": "has_product_templates",
            "description": "description",
            "max_zoom": "max_zoom",
            "priceinfo_price": "priceinfo_price",
            "priceinfo_currencycode": "priceinfo_currencycode",
            "priceinfo_currencydigits": "priceinfo_currencydigits",
            "priceinfo_currencyformat": "priceinfo_currencyformat",
            "priceinfo_formattedprice": "priceinfo_formattedprice",
            "retailprice_price": "retailprice_price",
            "retailprice_currencycode": "retailprice_currencycode",
            "retailprice_currencydigits": "retailprice_currencydigits",
            "retailprice_currencyformat": "retailprice_currencyformat",
            "retailprice_formattedprice": "retailprice_formattedprice",
            "categories": create_productcategory().id,
        }
        url = reverse('api_gooten_product_update', args=[product.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProductImageViewTest(unittest.TestCase):
    '''
    Tests for ProductImage
    '''
    def setUp(self):
        self.client = Client()

    def test_list_productimage(self):
        url = reverse('api_gooten_productimage_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_productimage(self):
        url = reverse('api_gooten_productimage_create')
        data = {
            "slug": "slug",
            "id": "id",
            "index": "index",
            "url": "url",
            "product": create_product().id,
            "image_type": create_imagetype().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_productimage(self):
        productimage = create_productimage()
        url = reverse('api_gooten_productimage_detail', args=[productimage.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_productimage(self):
        productimage = create_productimage()
        data = {
            "slug": "slug",
            "id": "id",
            "index": "index",
            "url": "url",
            "product": create_product().id,
            "image_type": create_imagetype().id,
        }
        url = reverse('api_gooten_productimage_update', args=[productimage.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProductCategoryViewTest(unittest.TestCase):
    '''
    Tests for ProductCategory
    '''
    def setUp(self):
        self.client = Client()

    def test_list_productcategory(self):
        url = reverse('api_gooten_productcategory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_productcategory(self):
        url = reverse('api_gooten_productcategory_create')
        data = {
            "slug": "slug",
            "id": "id",
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_productcategory(self):
        productcategory = create_productcategory()
        url = reverse('api_gooten_productcategory_detail', args=[productcategory.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_productcategory(self):
        productcategory = create_productcategory()
        data = {
            "slug": "slug",
            "id": "id",
            "name": "name",
        }
        url = reverse('api_gooten_productcategory_update', args=[productcategory.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ImageTypeViewTest(unittest.TestCase):
    '''
    Tests for ImageType
    '''
    def setUp(self):
        self.client = Client()

    def test_list_imagetype(self):
        url = reverse('api_gooten_imagetype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_imagetype(self):
        url = reverse('api_gooten_imagetype_create')
        data = {
            "slug": "slug",
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_imagetype(self):
        imagetype = create_imagetype()
        url = reverse('api_gooten_imagetype_detail', args=[imagetype.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_imagetype(self):
        imagetype = create_imagetype()
        data = {
            "slug": "slug",
            "name": "name",
        }
        url = reverse('api_gooten_imagetype_update', args=[imagetype.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProductInfoViewTest(unittest.TestCase):
    '''
    Tests for ProductInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_productinfo(self):
        url = reverse('api_gooten_productinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_productinfo(self):
        url = reverse('api_gooten_productinfo_create')
        data = {
            "slug": "slug",
            "key": "key",
            "index": "index",
            "product": create_product().id,
            "content_type": create_contenttype().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_productinfo(self):
        productinfo = create_productinfo()
        url = reverse('api_gooten_productinfo_detail', args=[productinfo.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_productinfo(self):
        productinfo = create_productinfo()
        data = {
            "slug": "slug",
            "key": "key",
            "index": "index",
            "product": create_product().id,
            "content_type": create_contenttype().id,
        }
        url = reverse('api_gooten_productinfo_update', args=[productinfo.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ContentTypeViewTest(unittest.TestCase):
    '''
    Tests for ContentType
    '''
    def setUp(self):
        self.client = Client()

    def test_list_contenttype(self):
        url = reverse('api_gooten_contenttype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_contenttype(self):
        url = reverse('api_gooten_contenttype_create')
        data = {
            "slug": "slug",
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_contenttype(self):
        contenttype = create_contenttype()
        url = reverse('api_gooten_contenttype_detail', args=[contenttype.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_contenttype(self):
        contenttype = create_contenttype()
        data = {
            "slug": "slug",
            "name": "name",
        }
        url = reverse('api_gooten_contenttype_update', args=[contenttype.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InfoContentViewTest(unittest.TestCase):
    '''
    Tests for InfoContent
    '''
    def setUp(self):
        self.client = Client()

    def test_list_infocontent(self):
        url = reverse('api_gooten_infocontent_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_infocontent(self):
        url = reverse('api_gooten_infocontent_create')
        data = {
            "slug": "slug",
            "text": "text",
            "productinfo": create_productinfo().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_infocontent(self):
        infocontent = create_infocontent()
        url = reverse('api_gooten_infocontent_detail', args=[infocontent.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_infocontent(self):
        infocontent = create_infocontent()
        data = {
            "slug": "slug",
            "text": "text",
            "productinfo": create_productinfo().id,
        }
        url = reverse('api_gooten_infocontent_update', args=[infocontent.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class VariantViewTest(unittest.TestCase):
    '''
    Tests for Variant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_variant(self):
        url = reverse('api_gooten_variant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_variant(self):
        url = reverse('api_gooten_variant_create')
        data = {
            "slug": "slug",
            "sku": "sku",
            "has_templates": "has_templates",
            "max_images": "max_images",
            "priceinfo_price": "priceinfo_price",
            "priceinfo_currencycode": "priceinfo_currencycode",
            "priceinfo_currencydigits": "priceinfo_currencydigits",
            "priceinfo_currencyformat": "priceinfo_currencyformat",
            "priceinfo_formattedprice": "priceinfo_formattedprice",
            "product": create_product().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_variant(self):
        variant = create_variant()
        url = reverse('api_gooten_variant_detail', args=[variant.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_variant(self):
        variant = create_variant()
        data = {
            "slug": "slug",
            "sku": "sku",
            "has_templates": "has_templates",
            "max_images": "max_images",
            "priceinfo_price": "priceinfo_price",
            "priceinfo_currencycode": "priceinfo_currencycode",
            "priceinfo_currencydigits": "priceinfo_currencydigits",
            "priceinfo_currencyformat": "priceinfo_currencyformat",
            "priceinfo_formattedprice": "priceinfo_formattedprice",
            "product": create_product().id,
        }
        url = reverse('api_gooten_variant_update', args=[variant.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class VariantOptionViewTest(unittest.TestCase):
    '''
    Tests for VariantOption
    '''
    def setUp(self):
        self.client = Client()

    def test_list_variantoption(self):
        url = reverse('api_gooten_variantoption_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_variantoption(self):
        url = reverse('api_gooten_variantoption_create')
        data = {
            "slug": "slug",
            "option_id": "option_id",
            "name": "name",
            "sort_value": "sort_value",
            "value": "value",
            "value_id": "value_id",
            "image_type": "image_type",
            "image_url": "image_url",
            "variant": create_variant().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_variantoption(self):
        variantoption = create_variantoption()
        url = reverse('api_gooten_variantoption_detail', args=[variantoption.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_variantoption(self):
        variantoption = create_variantoption()
        data = {
            "slug": "slug",
            "option_id": "option_id",
            "name": "name",
            "sort_value": "sort_value",
            "value": "value",
            "value_id": "value_id",
            "image_type": "image_type",
            "image_url": "image_url",
            "variant": create_variant().id,
        }
        url = reverse('api_gooten_variantoption_update', args=[variantoption.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class VariantTemplateViewTest(unittest.TestCase):
    '''
    Tests for VariantTemplate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_VariantTemplate(self):
        url = reverse('api_gooten_VariantTemplate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_VariantTemplate(self):
        url = reverse('api_gooten_VariantTemplate_create')
        data = {
            "slug": "slug",
            "name": "name",
            "is_default": "is_default",
            "image_url": "image_url",
            "variant": create_variant().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_VariantTemplate(self):
        VariantTemplate = create_VariantTemplate()
        url = reverse('api_gooten_VariantTemplate_detail', args=[VariantTemplate.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_VariantTemplate(self):
        VariantTemplate = create_VariantTemplate()
        data = {
            "slug": "slug",
            "name": "name",
            "is_default": "is_default",
            "image_url": "image_url",
            "variant": create_variant().id,
        }
        url = reverse('api_gooten_VariantTemplate_update', args=[VariantTemplate.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TemplateSpaceViewTest(unittest.TestCase):
    '''
    Tests for TemplateSpace
    '''
    def setUp(self):
        self.client = Client()

    def test_list_templatespace(self):
        url = reverse('api_gooten_templatespace_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_templatespace(self):
        url = reverse('api_gooten_templatespace_create')
        data = {
            "slug": "slug",
            "id": "id",
            "index": "index",
            "VariantTemplate": create_VariantTemplate().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_templatespace(self):
        templatespace = create_templatespace()
        url = reverse('api_gooten_templatespace_detail', args=[templatespace.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_templatespace(self):
        templatespace = create_templatespace()
        data = {
            "slug": "slug",
            "id": "id",
            "index": "index",
            "VariantTemplate": create_VariantTemplate().id,
        }
        url = reverse('api_gooten_templatespace_update', args=[templatespace.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LayerTypeViewTest(unittest.TestCase):
    '''
    Tests for LayerType
    '''
    def setUp(self):
        self.client = Client()

    def test_list_layertype(self):
        url = reverse('api_gooten_layertype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_layertype(self):
        url = reverse('api_gooten_layertype_create')
        data = {
            "slug": "slug",
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_layertype(self):
        layertype = create_layertype()
        url = reverse('api_gooten_layertype_detail', args=[layertype.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_layertype(self):
        layertype = create_layertype()
        data = {
            "slug": "slug",
            "name": "name",
        }
        url = reverse('api_gooten_layertype_update', args=[layertype.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SpaceLayerViewTest(unittest.TestCase):
    '''
    Tests for SpaceLayer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_spacelayer(self):
        url = reverse('api_gooten_spacelayer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_spacelayer(self):
        url = reverse('api_gooten_spacelayer_create')
        data = {
            "slug": "slug",
            "include_in_print": "include_in_print",
            "x1": "x1",
            "x2": "x2",
            "y1": "y1",
            "y2": "y2",
            "zIndex": "zIndex",
            "templatespace": create_templatespace().id,
            "layer_type": create_layertype().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_spacelayer(self):
        spacelayer = create_spacelayer()
        url = reverse('api_gooten_spacelayer_detail', args=[spacelayer.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_spacelayer(self):
        spacelayer = create_spacelayer()
        data = {
            "slug": "slug",
            "include_in_print": "include_in_print",
            "x1": "x1",
            "x2": "x2",
            "y1": "y1",
            "y2": "y2",
            "zIndex": "zIndex",
            "templatespace": create_templatespace().id,
            "layer_type": create_layertype().id,
        }
        url = reverse('api_gooten_spacelayer_update', args=[spacelayer.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


