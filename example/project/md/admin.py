from django.contrib import admin

from .models import ContentObject
from django_markdown.admin import MarkdownModelAdmin


@admin.register(ContentObject)
class ContentObjectAdmin(MarkdownModelAdmin):
    pass
