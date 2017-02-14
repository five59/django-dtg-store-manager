from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from timezone_field import TimeZoneField
import uuid
from django.utils import dateparse
from .wooStore import wooStore
from outlet_woocommerce.helper import *
from outlet_woocommerce.api import *
from .wpMediaSize import wpMediaSize


class wpMedia(models.Model):

    STATUSBOOL_OPEN = 'open'
    STATUSBOOL_CLOSED = 'closed'
    STATUSBOOL_CHOICES = (
        (STATUSBOOL_OPEN, _("Open")),
        (STATUSBOOL_CLOSED, _("Closed")),
    )

    MEDIATYPE_IMAGE = "image"
    MEDIATYPE_FILE = "file"
    MEDIATYPE_CHOICES = (
        (MEDIATYPE_IMAGE, _("Image")),
        (MEDIATYPE_FILE, )
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_("Is Active?"), default=True)

    alt_text = models.CharField(_("Alternate Text"), max_length=255,
                                default="", blank=True, null=True)
    media_type = models.CharField(_("Media Type"), max_length=255,
                                  default="", blank=True, null=True)
    width = models.IntegerField(_("Width"), default=0)
    height = models.IntegerField(_("Height"), default=0)
    file = models.CharField(_("File"), max_length=255, default="", blank=True, null=True)
    author = models.IntegerField(_("Author"), default=0)
    mime_type = models.CharField(_("MIME Type"), max_length=255, default="", blank=True, null=True)
    comment_status = models.CharField(_("Comment Status"), max_length=255,
                                      default=STATUSBOOL_OPEN, choices=STATUSBOOL_CHOICES)
    post = models.IntegerField(_("Post ID"), default=0)
    wid = models.CharField(_("ID"), max_length=16, default="", blank=True, null=True)
    source_url = models.URLField(_("Source URL"), blank=True, null=True)
    template = models.CharField(_("Template"), max_length=255, default="", blank=True, null=True)

    ping_status = models.CharField(_("Ping Status"), max_length=255,
                                   default=STATUSBOOL_OPEN, choices=STATUSBOOL_CHOICES)
    date = models.DateTimeField(_("Date"), blank=True, null=True)
    caption = models.CharField(_("Caption"), max_length=255, default="", blank=True, null=True)
    link = models.URLField(_("Link"), default="", blank=True, null=True)
    slug = models.CharField(_("Slug"), max_length=255, blank=True, null=True)
    modified = models.DateTimeField(_("Modified"), blank=True, null=True)
    guid = models.CharField(_("GUID"), max_length=255, default="", blank=True, null=True)
    description = models.TextField(_("Description"), default="", blank=True, null=True)
    modified_gmt = models.DateTimeField(_("Modified GMT"), blank=True, null=True)
    title = models.CharField(_("Title"), max_length=255, default="", blank=True, null=True)
    date_gmt = models.DateTimeField(_("Date GMT"), blank=True, null=True)
    type = models.CharField(_("Type"), max_length=64, default="", blank=True, null=True)

    # sizes = reverse relation
    woostore = models.ForeignKey("outlet_woocommerce.woostore", blank=True, null=True)

    def get_sizes(self):
        return wpMediaSize.objects.filter(wpmedia=self)
    get_sizes.short_description = _("Sizes")

    def num_sizes(self):
        return self.get_sizes().count()
    get_sizes.short_description = _("Sizes")

    def __str__(self):
        if self.title and self.file:
            return "{} / {}".format(self.title, self.file)
        if self.title:
            return "{}".format(self.title)
        return _("Unnamed wpMedia")

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")
        ordering = ["title", "guid", ]

    def _api_pull(data, store):
        # print(data)
        obj, created = wpMedia.objects.update_or_create(
            wid=data['id'],
            woostore=store,
            defaults={
                "is_active": True,
                "alt_text": data['alt_text'],
                "media_type": data['media_type'],
                "width": data['media_details']['width'],
                "height": data['media_details']['height'],
                "file": data['media_details']['file'],
                "author": data['author'],
                "mime_type": data['mime_type'],
                "comment_status": data['comment_status'],
                "post": data['post'] if data['post'] else 0,
                "wid": data['id'] if data['id'] else 0,
                "source_url": data["source_url"],
                "template": data["template"],
                "ping_status": data["ping_status"],
                "date": date_iso8601_to_wp(data["date"]),
                "caption": data["caption"]["rendered"],
                "link": data["link"],
                "slug": data["slug"],
                "modified": date_iso8601_to_wp(data["modified"]),
                "guid": data["guid"]["rendered"],
                "description": data["description"]["rendered"],
                "modified_gmt": date_iso8601_to_wp(data["modified_gmt"]),
                "title": data["title"]["rendered"],
                "date_gmt": date_iso8601_to_wp(data["date_gmt"]),
                "type": data["type"],
            }
        )
        print("- {} {}".format(
            "Created" if created else "Updated",
            obj.file,
        ))
        if 'sizes' in data['media_details']:
            wpMediaSize.objects.filter(wpmedia=obj).update(is_active=False)
            for name, size in data['media_details']['sizes'].items():
                sObj, sCreated = wpMediaSize.objects.update_or_create(
                    name=name,
                    wpmedia=obj,
                    defaults={
                        "is_active": True,
                        "file": size['file'],
                        "source_url": size['source_url'],
                        "mime_type": size['mime_type'],
                        "width": size['width'],
                        "height": size['height'],
                    }
                )
                print("-- {} {}".format(
                    "Created" if sCreated else "Updated",
                    sObj.name
                ))
        return obj

    def api_push(self):
        data = {
            # TODO
            "name": self.name,
        }
        if self.wid:
            self._api_update(data)
        else:
            self._api_create(data)

    def api_pull_all(store):
        path = "wp/v2/media"
        a = wcClient(store=store)
        data = a.get(path)
        wpMedia.objects.filter(woostore=store).update(is_active=False)
        print(a)
        while a.link_next:
            for d in data:
                mediaObj = wpMedia._api_pull(d, store)
            if a.link_next:
                res = a.get(a.link_next)
        else:
            for d in data:
                mediaObj = wpMedia._api_pull(d, store)

    def _api_create(self, data):
        path = "wp/v2/media"
        try:
            a = wcClient(store=self.woostore)
            data = a.post(path, data)
        except Exception as e:
            raise Exception(e)
        print("Created")
        self.wid = data['id']
        self.save()

    def _api_update(self, data):
        path = "wp/v2/media/{}" + str(self.wid)
        try:
            a = wcClient(store=self.woostore)
            data = a.post(path, data)
        except Exception as e:
            raise Exception(e)
        self.save()

    def _api_retrieve(self):
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_delete(self):
        raise NotImplementedError("Not Implemented (Yet)")

    def _api_batch(self):
        raise NotImplementedError("Not Implemented (Yet)")
