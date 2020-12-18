""" Markdown utils. """
import json
import markdown as markdown_module

from django.template import loader
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from . import settings


def markdown(value, extensions=settings.MARKDOWN_EXTENSIONS,
             extension_configs=settings.MARKDOWN_EXTENSION_CONFIGS,
             safe=False):
    """ Render markdown over a given value, optionally using varios extensions.

    Default extensions could be defined which MARKDOWN_EXTENSIONS option.

    :returns: A rendered markdown

    """
    return mark_safe(markdown_module.markdown(
        force_text(value), extensions=extensions,
        extension_configs=extension_configs, safe_mode=safe))


def editor_js_initialization(selector, **extra_settings):
    """Return script tag of type 'application/json'
       with initialization code.
    """

    init_template = loader.get_template(
        settings.MARKDOWN_EDITOR_INIT_TEMPLATE)

    options = dict(
        previewParserPath=reverse('django_markdown_preview'),
        **settings.MARKDOWN_EDITOR_SETTINGS
    )
    options.update(extra_settings)
    ctx = dict(
        selector=selector,
        extra_settings=json.dumps(options)
    )
    return init_template.render(ctx)
