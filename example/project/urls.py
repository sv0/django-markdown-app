from django.conf.urls import include, url
from django.contrib import admin

from django_markdown import flatpages

admin.autodiscover()

flatpages.register()

urlpatterns = [
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'', include('project.md.urls')),
]
