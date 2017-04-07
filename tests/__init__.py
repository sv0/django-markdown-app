import os

from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')


from django.conf import settings
from django.apps import apps

apps.populate(settings.INSTALLED_APPS)
call_command('migrate', interactive=False)

from django_markdown.tests import *  # noqa
