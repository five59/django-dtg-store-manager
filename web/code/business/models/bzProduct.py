from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid
from decimal import *
from .bzProductVariant import bzProductVariant
from .bzCreativeCollection import bzCreativeCollection
from .bzCreativeLayout import bzCreativeLayout
from .bzCreativeDesign import bzCreativeDesign
from vendor_printful.models.pfCatalogProduct import pfCatalogProduct
from vendor_printful.models.pfCatalogVariant import pfCatalogVariant
from outlet_woocommerce.models.wooProduct import wooProduct
# from outlet_woocommerce.models.wooProductVariant import wooProductVariant


class bzProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    code = models.CharField(_("Code"), max_length=64, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    bzDesign = models.ForeignKey("business.bzCreativeDesign", verbose_name=_(
        "Creative Design"), blank=True, null=True)
    bzLayout = models.ForeignKey("business.bzCreativeLayout", verbose_name=_(
        "Creative Layout"), blank=True, null=True)
    pfProduct = models.ForeignKey('vendor_printful.pfCatalogProduct',
                                  verbose_name=_("Printful Product"), blank=True, null=True)
    wcProduct = models.ForeignKey('outlet_woocommerce.wooProduct',
                                  verbose_name=_("Woo Product"), blank=True, null=True)

    pfSizes = models.ManyToManyField("vendor_printful.pfCatalogSize",
                                     verbose_name=_("Sizes"), blank=True)
    pfColors = models.ManyToManyField(
        "vendor_printful.pfCatalogColor", verbose_name=_("Colors"), blank=True)

    def get_woostore(self):
        if self.wcProduct:
            rv = self.wcProduct.woostore
        else:
            rv = None
        return rv
    get_woostore.short_description = _("Woo Store")

    def _update_sku(self):
        sku = []
        # First Group: Creative & Store
        if self.bzDesign.bzcreativecollection:
            sku.append(self.bzDesign.bzcreativecollection.code)
        else:
            sku.append("XXX")
        if self.bzDesign:
            sku.append(self.bzDesign.code)
        else:
            sku.append("XX")
        # -- Store (WooCommerce)
        if self.get_woostore():
            sku.append(self.get_woostore().code)
        else:
            sku.append("XX")
        sku.append("-")

        # Second Group: Product Construction
        if self.pfProduct:
            if self.pfProduct.pid:
                sku.append("{num:04d}".format(num=int(self.pfProduct.pid)))
            else:
                sku.append("0000")
        else:
            sku.append("0000")

        if self.wcProduct:
            if self.wcProduct.wid:
                sku.append("{num:05d}".format(num=int(self.wcProduct.wid)))
            else:
                sku.append("00000")
        else:
            sku.append("XXXXX")

        rv = "".join(sku)
        self.code = rv

    def _update_wooProduct(self):
        # TODO. Either create or update the WooProduct.
        raise NotImplementedError("Not Implemented (Yet)")

    def get_pfvariants(self):
        try:
            rv = pfCatalogVariant.objects.filter(
                pfsize__in=self.pfSizes.all(),
                pfcolor__in=self.pfColors.all(),
                pfcatalogproduct=self.pfProduct,
            )
        except:
            rv = pfCatalogVariant.objects.none()
        return rv
    get_pfvariants.short_description = _("Variants")

    def num_pfvariants(self):
        try:
            rv = self.get_pfvariants().count()
        except:
            rv = 0
        return rv
    num_pfvariants.short_description = _("Variants")

    def _update_bzProductVariants(self):
        bzProductVariant.objects.filter(bzproduct=self).update(is_active=False)
        for pfv in self.get_pfvariants():
            bzVariantObj, created = bzProductVariant.objects.update_or_create(
                bzproduct=self,
                pfcatalogvariant=pfv,
                defaults={
                    "is_active": True,
                },
            )
            print("-- {} {}.".format(
                "Created" if created else "Updated",
                bzVariantObj.code,
            ))

    # def _update_wooProductVariants(self):
    #     wooProductVariant.objects.filter(wooproduct=self.wooproduct).update(is_active=False)
    #     for pfv in self.get_woovariants():
    #         bzVariantObj, created = bzProductVariant.objects.update_or_create(
    #             bzproduct=self,
    #             pfcatalogvariant=pfv,
    #             defaults={
    #                 "is_active": True,
    #             },
    #         )
    #         print("-- {} {}.".format(
    #             "Created" if created else "Updated",
    #             bzVariantObj.code,
    #         ))

    def _update_wooProduct(self):
        if self.wcProduct:
            self.wcProduct.name = self.name
            self.wcProduct.type = wooProduct.TYPE_VARIABLE
            self.wcProduct.catalog_visibility = wooProduct.VISIBILITY_VISIBLE
            self.wcProduct.sku = self.code
            self.wcProduct.regular_price = Decimal("0.00")  # TODO
            self.wcProduct.save()

        else:
            self.wcProduct = wooProduct.objects.create(
                name=self.name,
                type=wooProduct.TYPE_VARIABLE,
                catalog_visibility=wooProduct.VISIBILITY_VISIBLE,
                sku=self.code,
                regular_price=Decimal("0.00"),  # TODO
            )

    def create_by_creativecollection(collection_code=None, layout_code=None, pfProduct_id=None, name_template="{}"):
        bzCollectionObj = bzCreativeCollection.objects.get(code=collection_code)
        bzLayoutObj = bzCreativeLayout.objects.get(
            code=layout_code, bzcreativecollection=bzCollectionObj)
        pfProductObj = pfCatalogProduct.objects.get(pid=pfProduct_id)
        print(bzCollectionObj, bzLayoutObj, pfProductObj)

        for d in bzCreativeDesign.objects.filter(bzcreativecollection=bzCollectionObj):
            p = bzProduct.objects.create(
                name=name_template.format(d.name),
                bzDesign=d,
                bzLayout=bzLayoutObj,
                pfProduct=pfProductObj,
            )
            p.save()  # Need to save it so that the links get created.
            for c in p.pfProduct.get_colors():
                p.pfColors.add(c)
            for s in p.pfProduct.get_sizes():
                p.pfSizes.add(s)
            p.save()

    def save(self, *args, **kwargs):
        self._update_sku()
        self._update_wooProduct()
        self._update_bzProductVariants()
        super(bzProduct, self).save(*args, **kwargs)

    def __str__(self):
        if self.code and self.name:
            return "[{}] {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Product")

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["name", "code", ]
