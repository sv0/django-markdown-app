""" Support Django admin. """

from django.contrib import admin

from django_markdown.widgets import AdminMarkdownWidget
from django_markdown.models import MarkdownField


class MarkdownModelAdmin(admin.ModelAdmin):

    """ Support markdown as ModelAdmin. """

    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

    class Media:
        # Fix for jQuery issues in 2.2+
        # @see https://docs.djangoproject.com/en/2.2/releases/2.2/#merging-of-form-media-assets  # noqa
        js = [
            'admin/js/jquery.init.js',
            'django_markdown/jquery.init.js',
        ]


class MarkdownInlineAdmin(admin.StackedInline):

    """ Support markdown as StackedInline. """

    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

    class Media:
        js = [
            'admin/js/jquery.init.js',
            'django_markdown/jquery.init.js',
        ]
