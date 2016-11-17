from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django_extensions.db import fields as extension_fields
import uuid
# from catalog import models as c


class GoogleCategory(MPTTModel):
    id = models.IntegerField(_('Google ID'), primary_key=True)
    code = models.CharField(_("Code"), max_length=16, default="", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255, default="", blank=True, null=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)
    long_name = models.CharField(_("Full Name"), max_length=300,
                                 default="", blank=True, help_text="")

    def __str__(self):
        if self.code and self.name:
            return "{} / {}".format(self.code, self.name)
        if self.name:
            return "{}".format(self.name)
        return _("Unnamed Google Category")

    class Meta:
        verbose_name = _("Google Category")
        verbose_name_plural = _("Google Categories")
        ordering = ['long_name', ]

    class MPTTMeta:
        order_insertion_by = ['name']
