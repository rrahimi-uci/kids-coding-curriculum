# Kids Coding curriculum - common tasks. Run `make help`.
PY ?= .venv/bin/python
LEVEL ?=
LEVEL_ARG := $(if $(LEVEL),--level $(LEVEL),)

SITE_PY ?= .venv-site/bin/python

.PHONY: help setup test smoke pdf pdf-standard pdf-dyslexia check clean student-bundle site-setup site-data site site-check site-serve

help:
	@echo "make setup         create .venv (Python 3.10, like Thonny) with pytest"
	@echo "make test          run every automated check (fast, no windows)"
	@echo "make smoke         open every turtle program in a real window briefly (Mac)"
	@echo "make pdf           build all PDFs, standard + dyslexia-friendly (LEVEL=1|2|3|j1|j2)"
	@echo "make pdf-standard  build only the standard edition"
	@echo "make check         test + pdf (what CI runs)"
	@echo "make student-bundle  solution-free copy for a child's Mac, with self-checks (LEVEL=1|2|3|j1|j2)"
	@echo "make site-setup    one-time: create .venv-site and install the site/ npm packages"
	@echo "make site          build the website (site/dist), then run the private-content and content checks"
	@echo "make site-check    HTML, link, accessibility and Lighthouse checks on site/dist"
	@echo "make site-serve    preview site/dist at http://localhost:4321/"
	@echo "make clean         remove build/"

setup:
	uv venv --python 3.10 --managed-python .venv || python3 -m venv .venv
	uv pip install --python .venv -r requirements-dev.txt || .venv/bin/pip install -r requirements-dev.txt

test:
	$(PY) -m pytest -q

smoke:
	$(PY) -m pytest -q --gui testing/test_smoke_gui.py

pdf:
	python3 tools/build.py $(LEVEL_ARG)

pdf-standard:
	python3 tools/build.py --variant standard $(LEVEL_ARG)

pdf-dyslexia:
	python3 tools/build.py --variant dyslexia $(LEVEL_ARG)

check: test pdf

student-bundle:
	python3 tools/student_bundle.py $(LEVEL_ARG)

site-setup:
	uv venv --python 3.12 .venv-site || python3 -m venv .venv-site
	uv pip install --python .venv-site -r requirements-site.txt || .venv-site/bin/pip install -r requirements-site.txt
	cd site && npm ci --no-audit --no-fund

site-data:
	$(SITE_PY) -m tools.site.build

site: site-data
	cd site && npm run build
	$(SITE_PY) -m tools.site.check_private site/dist
	$(SITE_PY) -m tools.site.check_content site/dist

site-check:
	cd site && npx html-validate "dist/**/*.html" --config .htmlvalidate.json
	cd site && node qa/links.mjs dist
	cd site && node qa/a11y.mjs dist
	cd site && CHROME_PATH="$${CHROME_PATH:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}" node qa/lighthouse.mjs dist

site-serve:
	cd site && npx http-server dist -p 4321 -c-1

clean:
	rm -rf build
