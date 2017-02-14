from django.utils import dateparse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from django.utils import dateparse
import pytz


def date_wp_to_iso8601(val):
    raise NotImplementedError()


def date_iso8601_to_wp(val):
    rv = dateparse.parse_datetime(val).replace(tzinfo=pytz.UTC)
    return rv
