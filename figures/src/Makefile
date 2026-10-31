# The nine diagrams of the proposal and the technical appendix, built from their TeX sources.
# The commands are those of the two figure folders of the original proposal (pdflatex, then
# pdftoppm at 300 dpi), with the proposal's figures written to ../proposal and the appendix's
# to ../appendix. Figure 3 of the proposal is a screenshot and has no source here.
# Needs pdflatex (TeX Live) and pdftoppm (Poppler).
DPI ?= 300
PROPOSAL := fig2_flow fig3_components
APPENDIX := fig_system fig_connections fig_pipeline fig_audit fig_runtime fig_lifecycle fig_procedures

all: $(addprefix ../proposal/,$(addsuffix .png,$(PROPOSAL))) $(addprefix ../appendix/,$(addsuffix .png,$(APPENDIX)))

fig2_flow.pdf fig3_components.pdf: %.pdf: %.tex figstyle.tex
	pdflatex -interaction=nonstopmode -halt-on-error $< > $*.log.txt 2>&1 || (grep -A4 '^!' $*.log.txt; exit 1)

$(addsuffix .pdf,$(APPENDIX)): %.pdf: %.tex appendixstyle.tex figstyle.tex
	pdflatex -interaction=nonstopmode -halt-on-error $< > $*.log.txt 2>&1 || (grep -A4 '^!' $*.log.txt; exit 1)

../proposal/%.png: %.pdf
	pdftoppm -png -r $(DPI) -singlefile $< ../proposal/$*

../appendix/%.png: %.pdf
	pdftoppm -png -r $(DPI) -singlefile $< ../appendix/$*

clean:
	rm -f *.aux *.log *.log.txt *.pdf

.PHONY: all clean
