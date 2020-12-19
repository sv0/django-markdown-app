from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from .models import ContentObject


@admin.register(ContentObject)
class ContentObjectAdmin(MarkdownModelAdmin):
    pass
