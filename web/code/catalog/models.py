from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid

# Printer/Producer/Shipper
class Producer(models.Model):
    """( Producer description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    code = models.CharField(_("ID Code"), max_length=2, default="", blank=True)
    def __str__(self):
        return u"Producer"
    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"

class Manufacturer(models.Model):
    """( Manufacturer description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    code = models.CharField(_("ID Code"), max_length=2, default="", blank=True)
    def __str__(self):
        return u"Manufacturer"
    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

class Part(models.Model):
    """( Part description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    code = models.CharField(_("ID Code"), max_length=2, default="", blank=True)
    def __str__(self):
        return u"Part"
    class Meta:
        verbose_name = "Part"
        verbose_name_plural = "Part"

class Attribute(models.Model):
    """( Attribute description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    code = models.CharField(_("ID Code"), max_length=2, default="", blank=True)
    is_variant_key = models.BooleanField(_("Variant?"), default=True, help_text='')
    def __str__(self):
        return u"Attribute"
    class Meta:
        verbose_name = "Attribute"
        verbose_name_plural = "Attributes"

class AttributeValue(models.Model):
    """( AttributeValue description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "AttributeValue"
        verbose_name_plural = "AttributeValues"

class Creative(models.Model):
    """( Creative description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    def __str__(self):
        return u"Creative"
    class Meta:
        verbose_name = "Creative"
        verbose_name_plural = "Creatives"

class Collection(models.Model):
    """( Collection description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    code = models.CharField(_("ID Code"), max_length=2, default="", blank=True)
    def __str__(self):
        return u"Collection"
    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

class Product(models.Model):
    """( Product description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    code = models.CharField(_("ID Code"), max_length=2, default="", blank=True)
    def __str__(self):
        return u"Product"
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Outlet(models.Model):
    """( Outlet description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    code = models.CharField(_("ID Code"), max_length=2, default="", blank=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True)
    public_url = models.URLField(_("Web"), null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Outlet"
        verbose_name_plural = "Outlets"
