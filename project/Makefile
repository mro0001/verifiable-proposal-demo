# The build file. One rule per research product, each naming its one source file.
# Written by the workflow's project setup, then edited so the project builds on any machine.
# WORKFLOW is the folder of the workflow (the one holding ospipe/). The default is a clone of
# the public workflow beside this repository. Set it otherwise, as in
# make proposal WORKFLOW=/path/to/workflow.

WORKFLOW ?= $(firstword $(wildcard ../../verifiable-social-science-workflow ../verifiable-social-science-workflow))
OSPIPE ?= PYTHONPATH='$(WORKFLOW)/ospipe' python3 -m ospipe
MANIFEST ?= numbers.yml
PURPOSE ?= draft
PRODUCT ?=

manifest:
	$(OSPIPE) emit-manifest --manifest $(MANIFEST)

emit:
	$(OSPIPE) emit --map Makefile --product $(PRODUCT)

.PHONY: proposal
proposal: proposal.md $(MANIFEST)
	$(OSPIPE) build --manuscript proposal.md --manifest $(MANIFEST) --tables-dir . --bib refs.bib --csl styles/informs.csl --to docx --reference-doc styles/reference.docx --builds-dir builds/proposal --verification-dir verification/proposal --purpose "$(PURPOSE)"

.PHONY: appendix
appendix: appendix.md $(MANIFEST)
	$(OSPIPE) build --manuscript appendix.md --manifest $(MANIFEST) --tables-dir . --bib refs.bib --csl styles/informs.csl --to docx --reference-doc styles/reference.docx --builds-dir builds/appendix --verification-dir verification/appendix --purpose "$(PURPOSE)"

# The data pipeline of pipeline.yaml, run in order. It computes the appendix's numbers
# from the archived artifact and the October 8 run folders (about 30 minutes, mostly tests).
.PHONY: data
data:
	PYTHONDONTWRITEBYTECODE=1 python3 s1_artifact_numbers.py
	PYTHONDONTWRITEBYTECODE=1 python3 s2_live_runs.py
