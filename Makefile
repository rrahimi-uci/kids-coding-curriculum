# Kids Coding curriculum - common tasks. Run `make help`.
PY ?= .venv/bin/python
LEVEL ?=
LEVEL_ARG := $(if $(LEVEL),--level $(LEVEL),)

.PHONY: help setup test smoke pdf pdf-standard pdf-dyslexia check clean

help:
	@echo "make setup         create .venv (Python 3.10, like Thonny) with pytest"
	@echo "make test          run every automated check (fast, no windows)"
	@echo "make smoke         open every turtle program in a real window briefly (Mac)"
	@echo "make pdf           build all PDFs, standard + dyslexia-friendly (LEVEL=1|2|3)"
	@echo "make pdf-standard  build only the standard edition"
	@echo "make check         test + pdf (what CI runs)"
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

clean:
	rm -rf build
