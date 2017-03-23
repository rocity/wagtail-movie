from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class CatalogPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    # Content Panels adds the fields to the admin
    # interface where the admin can place input data
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
