Django-Markdown v. 0.8.5
########################

.. _description:

**Django markdown** is django application that allows use markdown wysiwyg in flatpages, admin forms and other forms.
Documentaton available at pypi_ or github_.

It's a fork of https://github.com/klen/django_markdown

The reason of forking is the original project is not maintained anymore and the owner(klen_) is not interested in the merging of the pull requests.


.. _badges:

.. image:: https://travis-ci.org/sv0/django-markdown-app.svg?branch=master
    :target: https://travis-ci.org/sv0/django-markdown-app
    :alt: Build Status

.. image:: https://coveralls.io/repos/github/sv0/django-markdown-app/badge.svg?branch=master
    :target: https://coveralls.io/github/sv0/django-markdown-app?branch=master
    :alt: Coverals

.. image:: http://img.shields.io/pypi/v/django-markdown-app.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-markdown-app
    :alt: Version

.. image:: http://img.shields.io/pypi/dm/django-markdown-app.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-markdown-app
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/django-markdown-app.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-markdown-app
    :alt: License

.. image:: http://img.shields.io/gratipay/klen.svg?style=flat-square
    :target: https://www.gratipay.com/klen/
    :alt: Donate

.. contents::

.. _requirements:

Requirements
============

- python >= 2.7
- django >= 1.6
- markdown


.. _installation:

Installation
============

**Django markdown** should be installed using pip: ::

    pip install django-markdown-app


Setup
=====

.. note:: 'django_markdown' require 'django.contrib.staticfiles' in INSTALLED_APPS

- Add 'django_markdown' to INSTALLED_APPS ::

    INSTALLED_APPS += ( 'django_markdown', )


- Add django_markdown urls to base urls ::

    url('^markdown/', include( 'django_markdown.urls')),


Use django_markdown
===================

#) Models: ::
    
    from django_markdown.models import MarkdownField
    class MyModel(models.Model):
        content = MarkdownField()

#) Custom forms: ::

    from django_markdown.fields import MarkdownFormField
    from django_markdown.widgets import MarkdownWidget
    class MyCustomForm(forms.Form):
        content = forms.CharField(widget=MarkdownWidget())
        content2 = MarkdownFormField()

#) Custom admins: ::

    from django_markdown.admin import MarkdownModelAdmin
    admin.site.register(MyModel, MarkdownModelAdmin)

#) Admin Overrides: (If you don't want to subclass package ModelAdmin's) ::

    from django.contrib import admin

    class YourModelAdmin(admin.ModelAdmin):
        formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

#) Flatpages: ::

    # in your project main urls
    from django_markdown import flatpages
    ...
    # Django admin
    admin.autodiscover()
    flatpages.register()
    urlpatterns += [ url(r'^admin/', include(admin.site.urls)), ]

#) Template tags: ::

    <textarea name="test" id="new"></textarea>
    {% markdown_editor "#new" %}
    {% markdown_media %}


Settings
========

**MARKDOWN_EDITOR_SETTINGS** - holds the extra parameters set to be passed to ``textarea.markItUp()``

**MARKDOWN_EDITOR_SKIN** - skin option, default value is ``markitup``

Example: `settings.py` ::

    MARKDOWN_EDITOR_SKIN = 'simple'

**MARKDOWN_EXTENSIONS** - optional list of extensions passed to Markdown, discussed at https://pythonhosted.org/Markdown/extensions/index.html#officially-supported-extensions

Example: `settings.py` ::

    MARKDOWN_EXTENSIONS = ['extra']

**MARKDOWN_EXTENSION_CONFIGS** - Configure extensions, discussed at https://pythonhosted.org/Markdown/reference.html#extension_configs

**MARKDOWN_PREVIEW_TEMPLATE** - Template for preview a markdown. By default `django_markdown/preview.css`

**MARKDOWN_STYLE** - path to preview styles. By default `django_markdown/preview.css`

**MARKDOWN_SET_PATH** - path to folder with sets. By default `django_markdown/sets`

**MARKDOWN_SET_NAME** - name for current set. By default `markdown`.

**MARKDOWN_PROTECT_PREVIEW** - protect preview url for staff only


Examples
========

Execute `make run` in sources directory. Open http://127.0.0.1:8000 in your
browser. For admin access use 'root:root' credentials.


Changes
=======

Make sure you`ve read the following document if you are upgrading from previous versions:

http://packages.python.org/django-markdown-app/changes.html


Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/sv0/django-markdown-app/issues


Contributing
============

Development of django-markdown happens at github: https://github.com/sv0/django-markdown-app


Contributors
============

* klen_ (Kirill Klenov)

* yavorskiy_ (Sergii Iavorskyi)


License
=======

Licensed under a `GNU lesser general public license`_.


Copyright
=========

Copyright (c) 2011 Kirill Klenov (horneds@gmail.com)

Markitup_:
    (c) 2008 Jay Salvat
    http://markitup.jaysalvat.com/ 
    

.. _GNU lesser general public license: http://www.gnu.org/copyleft/lesser.html
.. _pypi: http://packages.python.org/django-markdown/
.. _Markitup: http://markitup.jaysalvat.com/ 
.. _github: https://github.com/klen/django_markdown
.. _klen: https://github.com/klen
.. _yavorskiy: https://github.com/yavorskiy
