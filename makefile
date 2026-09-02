SRCS:=stdlibs

release: lint test clean
	flit publish

regenerate:
	uv run --locked -m stdlibs.fetch_releases
	uv run --locked -m stdlibs.fetch

format:
	uv run --locked ufmt format $(SRCS)

lint:
	uv run --locked mypy --non-interactive --install-types $(SRCS)
	uv run --locked flake8 $(SRCS)
	uv run --locked ufmt check $(SRCS)

test:
	uv run --locked coverage run -m $(SRCS).tests
	uv run --locked coverage report

html: .venv README.md docs/*.rst docs/conf.py
	uv run --locked sphinx-build -b html docs html

clean:
	rm -rf build dist html README MANIFEST *.egg-info .mypy_cache

distclean: clean
	rm -rf .venv
