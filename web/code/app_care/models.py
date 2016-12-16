from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
from catalog.models.Size import Size
from creative import models as cr
from catalog import models as ca


class CareComponent(models.Model):
    CATEGORY_WASH = 1
    CATEGORY_BLEACH = 2
    CATEGORY_DRY = 3
    CATEGORY_WRING = 4
    CATEGORY_IRON = 5
    CATEGORY_DRYCLEAN = 6
    CATEGORY_CHOICES = (
        (CATEGORY_WASH, "Wash"),
        (CATEGORY_BLEACH, "Bleach"),
        (CATEGORY_DRY, "Dry"),
        (CATEGORY_WRING, "Wring"),
        (CATEGORY_IRON, "Iron"),
        (CATEGORY_DRYCLEAN, "Dry Clean"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="")
    category = models.IntegerField(_("Category"), choices=CATEGORY_CHOICES,  default=0)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)

    icon_height = models.IntegerField(_("Icon Height"), default=0)
    icon_width = models.IntegerField(_("Icon Width"), default=0)
    icon = models.ImageField(upload_to="", height_field="icon_height",
                             width_field="icon_width", null=True, blank=True)

    description = models.TextField(_("Description"), default="", blank=True, null=True)

    def has_icon(self):
        if self.icon:
            return True
        return False
    has_icon.short_description = _("Has Icon?")
    has_icon.boolean = True

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Care Component")

    class Meta:
        verbose_name = _("Care Component")
        verbose_name_plural = _("Care Components")
        ordering = ["category", "name", ]


class CareInstructions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    item = models.ForeignKey(ca.Item, blank=True, null=True)

    icon_wash = models.ForeignKey(CareComponent, related_name='rel_wash', verbose_name=_("Washing Instructions"),
                                  limit_choices_to={'category': CareComponent.CATEGORY_WASH}, blank=True, null=True)
    icon_bleach = models.ForeignKey(CareComponent, related_name='rel_bleach', verbose_name=_("Bleach Instructions"),
                                    limit_choices_to={'category': CareComponent.CATEGORY_BLEACH}, blank=True, null=True)
    icon_dry = models.ForeignKey(CareComponent, related_name='rel_dry', verbose_name=_("Drying Instructions"),
                                 limit_choices_to={'category': CareComponent.CATEGORY_DRY}, blank=True, null=True)
    icon_wring = models.ForeignKey(CareComponent, related_name='rel_wring', verbose_name=_("Wringing Instructions"),
                                   limit_choices_to={'category': CareComponent.CATEGORY_WRING}, blank=True, null=True)
    icon_iron = models.ForeignKey(CareComponent, related_name='rel_iron', verbose_name=_("Ironing Instructions"),
                                  limit_choices_to={'category': CareComponent.CATEGORY_IRON}, blank=True, null=True)
    icon_dryclean = models.ForeignKey(CareComponent, related_name='rel_dryclean', verbose_name=_("Dry Cleaning Instructions"),
                                      limit_choices_to={'category': CareComponent.CATEGORY_DRYCLEAN}, blank=True, null=True)

    def get_list(self):
        rv = (self.icon_wash, self.icon_bleach, self.icon_dry,
              self.icon_wring, self.icon_iron, self.icon_dryclean)
        rv = [x for x in rv if x is not None]
        return rv

    def get_item_code(self):
        return self.item.get_item_code()
    get_item_code.short_description = "Item Code"

    def __str__(self):
        if self.item:
            return '{} {}'.format(self.item.name, _("Instructions"))
        return _("Unnamed Care Instructions")

    class Meta:
        verbose_name = _("Care Instructions")
        verbose_name_plural = _("Care Instructions")
        ordering = ["item", ]


class CareLabel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    # name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    saleschannel = models.ForeignKey(cr.SalesChannel, blank=True, null=True)
    instructions = models.ForeignKey(CareInstructions, blank=True, null=True)
    size = models.ForeignKey(ca.Size, blank=True, null=True)

    artwork = models.ImageField(_("Artwork"), blank=True, null=True)

    def generate_label(self):
        return True

    def __str__(self):
        if self.instructions.item:
            return "{} / {} / {}".format(self.saleschannel, self.instructions.item, self.size)
        return _("Unnamed Care Label")

    class Meta:
        verbose_name = _("Care Label")
        verbose_name_plural = _("Care Label")
        ordering = ['saleschannel', 'instructions', 'size', ]
