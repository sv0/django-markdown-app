from django.apps import AppConfig


class MdConfig(AppConfig):
    name = 'project.md'

    def ready(self):
        ...
