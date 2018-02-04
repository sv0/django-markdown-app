from django.urls import include, path
from django.contrib import admin

from django_markdown import flatpages

admin.autodiscover()

flatpages.register()

urlpatterns = [
    path('markdown/', include('django_markdown.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('project.md.urls')),
]
