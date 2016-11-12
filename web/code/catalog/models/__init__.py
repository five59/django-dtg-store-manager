from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields
import uuid

from .Manufacturer import Manufacturer
from .Category import Category
from .GoogleCategory import GoogleCategory
from .Color import Color
from .Size import Size
from .Brand import Brand
from .Item import Item
from .ItemVariant import ItemVariant
