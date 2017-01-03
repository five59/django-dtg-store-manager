from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Product, ProductImage, ProductCategory, ImageType, ProductInfo, ContentType, InfoContent, Variant, Attribute, AttributeValue, VariantOption, VariantTemplate, TemplateSpace, LayerType, SpaceLayer
from .forms import ProductForm, ProductImageForm, ProductCategoryForm, ImageTypeForm, ProductInfoForm, ContentTypeForm, InfoContentForm, VariantForm, AttributeForm, AttributeValueForm, VariantOptionForm, VariantTemplateForm, TemplateSpaceForm, LayerTypeForm, SpaceLayerForm


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


class ProductImageListView(ListView):
    model = ProductImage


class ProductImageCreateView(CreateView):
    model = ProductImage
    form_class = ProductImageForm


class ProductImageDetailView(DetailView):
    model = ProductImage


class ProductImageUpdateView(UpdateView):
    model = ProductImage
    form_class = ProductImageForm


class ProductCategoryListView(ListView):
    model = ProductCategory


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm


class ProductCategoryDetailView(DetailView):
    model = ProductCategory


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm


class ImageTypeListView(ListView):
    model = ImageType


class ImageTypeCreateView(CreateView):
    model = ImageType
    form_class = ImageTypeForm


class ImageTypeDetailView(DetailView):
    model = ImageType


class ImageTypeUpdateView(UpdateView):
    model = ImageType
    form_class = ImageTypeForm


class ProductInfoListView(ListView):
    model = ProductInfo


class ProductInfoCreateView(CreateView):
    model = ProductInfo
    form_class = ProductInfoForm


class ProductInfoDetailView(DetailView):
    model = ProductInfo


class ProductInfoUpdateView(UpdateView):
    model = ProductInfo
    form_class = ProductInfoForm


class ContentTypeListView(ListView):
    model = ContentType


class ContentTypeCreateView(CreateView):
    model = ContentType
    form_class = ContentTypeForm


class ContentTypeDetailView(DetailView):
    model = ContentType


class ContentTypeUpdateView(UpdateView):
    model = ContentType
    form_class = ContentTypeForm


class InfoContentListView(ListView):
    model = InfoContent


class InfoContentCreateView(CreateView):
    model = InfoContent
    form_class = InfoContentForm


class InfoContentDetailView(DetailView):
    model = InfoContent


class InfoContentUpdateView(UpdateView):
    model = InfoContent
    form_class = InfoContentForm


class VariantListView(ListView):
    model = Variant


class VariantCreateView(CreateView):
    model = Variant
    form_class = VariantForm


class VariantDetailView(DetailView):
    model = Variant


class VariantUpdateView(UpdateView):
    model = Variant
    form_class = VariantForm


class AttributeListView(ListView):
    model = Attribute


class AttributeCreateView(CreateView):
    model = Attribute
    form_class = AttributeForm


class AttributeDetailView(DetailView):
    model = Attribute


class AttributeUpdateView(UpdateView):
    model = Attribute
    form_class = AttributeForm


class AttributeValueListView(ListView):
    model = AttributeValue


class AttributeValueCreateView(CreateView):
    model = AttributeValue
    form_class = AttributeValueForm


class AttributeValueDetailView(DetailView):
    model = AttributeValue


class AttributeValueUpdateView(UpdateView):
    model = AttributeValue
    form_class = AttributeValueForm


class VariantOptionListView(ListView):
    model = VariantOption


class VariantOptionCreateView(CreateView):
    model = VariantOption
    form_class = VariantOptionForm


class VariantOptionDetailView(DetailView):
    model = VariantOption


class VariantOptionUpdateView(UpdateView):
    model = VariantOption
    form_class = VariantOptionForm


class VariantTemplateListView(ListView):
    model = VariantTemplate


class VariantTemplateCreateView(CreateView):
    model = VariantTemplate
    form_class = VariantTemplateForm


class VariantTemplateDetailView(DetailView):
    model = VariantTemplate


class VariantTemplateUpdateView(UpdateView):
    model = VariantTemplate
    form_class = VariantTemplateForm


class TemplateSpaceListView(ListView):
    model = TemplateSpace


class TemplateSpaceCreateView(CreateView):
    model = TemplateSpace
    form_class = TemplateSpaceForm


class TemplateSpaceDetailView(DetailView):
    model = TemplateSpace


class TemplateSpaceUpdateView(UpdateView):
    model = TemplateSpace
    form_class = TemplateSpaceForm


class LayerTypeListView(ListView):
    model = LayerType


class LayerTypeCreateView(CreateView):
    model = LayerType
    form_class = LayerTypeForm


class LayerTypeDetailView(DetailView):
    model = LayerType


class LayerTypeUpdateView(UpdateView):
    model = LayerType
    form_class = LayerTypeForm


class SpaceLayerListView(ListView):
    model = SpaceLayer


class SpaceLayerCreateView(CreateView):
    model = SpaceLayer
    form_class = SpaceLayerForm


class SpaceLayerDetailView(DetailView):
    model = SpaceLayer


class SpaceLayerUpdateView(UpdateView):
    model = SpaceLayer
    form_class = SpaceLayerForm

