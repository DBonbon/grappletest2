from django.db import models
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import CharBlock,RichTextBlock
from grapple.models import (
    GraphQLRichText,
    GraphQLString,
    GraphQLStreamfield,
)


class HomePage(Page):
    date = models.CharField(max_length=50)
    summary = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("summary"),
    ]

    # Note these fields below:
    graphql_fields = [
        GraphQLString("date"),
        GraphQLRichText("summary"),
    ]
