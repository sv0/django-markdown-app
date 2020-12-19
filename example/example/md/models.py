from django.db import models
from django_markdown.models import MarkdownField


class ContentObject(models.Model):
    """ Class description. """

    content = MarkdownField()
    description = MarkdownField()
