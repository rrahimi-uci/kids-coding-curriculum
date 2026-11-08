# Parent information deck -- build with `make` from this folder.
#   make          deck + speaker notes + handout  -> build/
#   make deck     slides only (build/parent-deck.pdf)
#   make notes    presenter edition with speaker notes (build/parent-deck-notes.pdf)
#   make handout  one-page handout (build/parent-handout.pdf)
#   make png      render every slide to build/png/ for visual checks
#   make clean
# Needs LuaLaTeX, biber and the packages listed in README.md.

export TEXINPUTS := $(CURDIR)//:$(CURDIR)/../shared/latex//:$(TEXINPUTS)
LUALATEX := lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build/aux
SOURCES := main.tex beamerthemekidscode.sty content/shared.tex references.bib ../shared/latex/kidscode-colors.sty

.PHONY: all deck notes handout png clean
all: deck notes handout
deck: build/parent-deck.pdf
notes: build/parent-deck-notes.pdf
handout: build/parent-handout.pdf

# One rule per document: lualatex -> biber -> lualatex x2 (references + TikZ positions).
define build_doc
	@mkdir -p build/aux
	$(LUALATEX) -jobname=$(2) $(1) > build/aux/$(2).run.log || (tail -40 build/aux/$(2).log; exit 1)
	biber --quiet --input-directory build/aux --output-directory build/aux $(2)
	$(LUALATEX) -jobname=$(2) $(1) > build/aux/$(2).run.log || (tail -40 build/aux/$(2).log; exit 1)
	$(LUALATEX) -jobname=$(2) $(1) > build/aux/$(2).run.log || (tail -40 build/aux/$(2).log; exit 1)
	cp build/aux/$(2).pdf $@
endef

build/parent-deck.pdf: $(SOURCES)
	$(call build_doc,main.tex,parent-deck)
build/parent-deck-notes.pdf: notes.tex $(SOURCES)
	$(call build_doc,notes.tex,parent-deck-notes)
build/parent-handout.pdf: handout.tex content/shared.tex references.bib ../shared/latex/kidscode.cls ../shared/latex/kidscode-colors.sty
	$(call build_doc,handout.tex,parent-handout)

png: all
	@mkdir -p build/png
	pdftoppm -r 60 -png build/parent-deck.pdf build/png/slide
	pdftoppm -r 60 -png build/parent-handout.pdf build/png/handout

clean:
	rm -rf build
