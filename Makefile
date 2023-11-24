MODULE=django_markdown
VIRTUALENV=$(shell echo "$${VDIR:-'.venv'}")

all: $(VIRTUALENV)

.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

.PHONY: clean
# target: clean - Clean repo
clean:
	@rm -rf build dist docs/_build django_markdown_app.egg-info
	find $(CURDIR) -name "*.pyc" -delete
	find $(CURDIR) -name "*.orig" -delete
	find $(CURDIR) -name "__pycache__" | xargs rm -rf
	find $(CURDIR) -name "django_markdown_app-?.?.?.dist-info" | xargs rm -rf

# ==============
#  Bump version
# ==============

.PHONY: release
VERSION?=minor
# target: release - Bump version
release:
	@pip3 install bumpversion
	@bumpversion $(VERSION)
	@git checkout master
	@git merge develop
	@git checkout develop
	@git push --all
	@git push --tags

.PHONY: minor
minor: release

.PHONY: patch
patch:
	make release VERSION=patch

.PHONY: major
major:
	make release VERSION=major


# ===============
#  Build package
# ===============

.PHONY: register
# target: register - Register module on PyPi
register:
	@python3 setup.py register

.PHONY: upload
# target: upload - Upload module on PyPi
upload: clean docs
	@pip3 install twine wheel
	@python3 setup.py sdist bdist_wheel
	@twine upload dist/*

.PHONY: docs
# target: docs - Compile and upload docs
docs:
	@pip3 install sphinx sphinx-pypi-upload
	@python3 setup.py build_sphinx --source-dir=docs/ --build-dir=docs/_build --all-files


# =============
#  Development
# =============


$(VIRTUALENV): requirements.txt
	[ -d $(VIRTUALENV) ] || python3 -m venv $(VIRTUALENV)
	@$(VIRTUALENV)/bin/pip3 install -r requirements.txt
	touch $(VIRTUALENV)

$(VIRTUALENV)/bin/py.test: requirements-tests.txt $(VIRTUALENV)
	@$(VIRTUALENV)/bin/pip3 install -r requirements-tests.txt
	touch $(VIRTUALENV)/bin/py.test

.PHONY: test
# target: test - Runs tests
test: clean $(VIRTUALENV)/bin/py.test
	@$(VIRTUALENV)/bin/py.test

$(CURDIR)/example/db.sqlite3: $(VIRTUALENV)
	$(VIRTUALENV)/bin/python3 example/manage.py migrate --noinput

.PHONY: run
run: $(CURDIR)/example/db.sqlite3
	$(VIRTUALENV)/bin/python3 example/manage.py runserver

.PHONY: shell
shell: $(CURDIR)/example/db.sqlite3
	$(VIRTUALENV)/bin/python3 example/manage.py shell
