SRCS:=stdlibs
EXTRAS:=dev,docs

ifeq ($(OS),Windows_NT)
    ACTIVATE:=.venv/Scripts/activate
else
    ACTIVATE:=.venv/bin/activate
endif

UV:=$(shell uv --version)
ifdef UV
	VENV:=uv venv
	PIP:=uv pip
else
	VENV:=python -m venv
	PIP:=python -m pip
endif

.venv:
	$(VENV) .venv

venv: .venv
	source $(ACTIVATE) && make install
	echo 'run `source $(ACTIVATE)` to use virtualenv'

install:
	$(PIP) install -Ue .[$(EXTRAS)]

release: lint test clean
	flit publish

regenerate:
	python -m stdlibs.fetch_releases
	python -m stdlibs.fetch

format:
	python -m ufmt format $(SRCS)

lint:
	python -m mypy --non-interactive --install-types $(SRCS)
	python -m flake8 $(SRCS)
	python -m ufmt check $(SRCS)

test:
	python -m coverage run -m $(SRCS).tests
	python -m coverage report

html: .venv README.md docs/*.rst docs/conf.py
	source .venv/bin/activate && sphinx-build -b html docs html

clean:
	rm -rf build dist html README MANIFEST *.egg-info .mypy_cache

distclean: clean
	rm -rf .venv
