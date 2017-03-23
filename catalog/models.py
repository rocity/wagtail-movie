from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class CatalogPage(Page):
    """
    Catalog Page
    A page to display all movies
    """
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    # Content Panels adds the fields to the admin
    # interface where the admin can place input data
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]


class MoviePage(Page):
    """
    Movie Page
    A page of a movie's details
    """
    description = RichTextField(blank=True)

    def main_image(self):
        movie_item = self.movie_images.first()
        if movie_item:
            return movie_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        InlinePanel('movie_images', label='Movie Images')
    ]


class MoviePageMovieImage(Orderable):
    """
    Movie Image Orderable
    Images for a movie
    """
    page = ParentalKey(MoviePage, related_name='movie_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]
