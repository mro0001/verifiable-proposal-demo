# Rebuild and rerun

The paths on this page are inside `project/`, and `make` runs there.

## The source texts

The text is the author's. It changes only where the pipeline needs it. Author-year citations became keys that print the same way, the appendix's numbers about the prototype became placeholders filled from a numbers file, and the six works the text cites but the author's reference list leaves out were added to `refs.bib`.

## What is here

[`project/README.md`](../project/README.md) says what each file in the project folder is.

## Rebuilding

You need Python 3.9 with PyYAML and python-docx, pandoc (3.9.0.2 made these builds), and the workflow. The reports here were made with the workflow at the candidate public copy, commit e22136c. Name its folder with `WORKFLOW=`.

```
make proposal WORKFLOW=/path/to/workflow
make appendix WORKFLOW=/path/to/workflow
```

Without `WORKFLOW=`, the `Makefile` looks for the workflow beside this repository, at `../../verifiable-social-science-workflow` from `project/`, where `git clone` puts it, and stops with "No module named ospipe" if it is not there. Each build fills every placeholder from `numbers.yml`, stops if one has no value, writes the next numbered build in `builds/<product>/`, and adds a ledger row that names each stream's current results and whether it is verified. To compute the numbers again from the raw archives, run `make data` (about 30 minutes, mostly the artifact's test suites) and then `make manifest`.

## Rerunning the reports

The references, prose, and build reports, and the final-numbers report's account of the AI's edits, read the record, and the record is not in this repository. Neither are the cited works' texts, most of which are not openly licensed. These reports can be read here but not rerun from here. A report run with an empty record says nothing about it. The prose report then lists every change as the author's, and the build report counts no AI write, so a reader who starts an empty audit home gets clean-looking reports that are wrong. With the record in place, the commands below rerun each report. The phase reports and the final-numbers report's rerun of the pipeline need no record.

Run them from the workflow's folder. `DEMO` is the project folder, at the path the record was captured with, and `COPY` is a copy of it, made with `git archive`, into which the records go. Each `vg.py run` writes its report to `RUN/files/report.md` and its items to `RUN/results.json`. Name each run as the published ones are named, such as `appendix_prose`, since the folder's name becomes the run's id.

```
# References (citations), for the proposal or, with appendix in place of proposal, the appendix
python3 -m audit_layer write-out citation-provenance --project DEMO --references DEMO/refs.bib --out PROV.yaml --artifacts PATH ... --fetched PATH ...
python3 -m connections adapt citations --out REFS --export DEMO/refs.bib
cp DEMO/verification/references_inputs/metadata_cache.json REFS/
cp SOURCES/source_*.txt REFS/
python3 handoffs/project_to_references.py --project COPY --references REFS --provenance PROV.yaml --to INPUTS --builds-dir builds/proposal --source proposal.md
(cd verification_procedures && python3 vg.py run graphs/citations.yaml --run RUN --inputs INPUTS --judge live)

# Prose
git -C DEMO show 769b8f0:proposal.md > COPY/author_draft.md
python3 -m audit_layer write-out rationales --project DEMO --source proposal.md --out RATIONALES.yaml
python3 handoffs/audit_to_project.py --record rationales --from RATIONALES.yaml --project COPY
python3 handoffs/project_to_prose.py --project COPY --prose DEMO/verification/proposal/prose_pin --to INPUTS --source proposal.md
(cd verification_procedures && VG_OFFLINE=1 python3 vg.py run graphs/prose.yaml --run RUN --inputs INPUTS)

# Final numbers (data), and the three phase reports
python3 -m audit_layer write-out file-edits --project DEMO --out EDITS.yaml
python3 handoffs/project_to_data.py --project COPY --to INPUTS --file-edits EDITS.yaml
(cd verification_procedures && VG_OFFLINE=1 python3 vg.py run graphs/data.yaml --run RUN --inputs INPUTS)
python3 handoffs/project_to_data_phases.py --project COPY --to PHASES --builds-dir builds/appendix
(cd verification_procedures && python3 vg.py run graphs/data_analysis.yaml --run RUN --inputs PHASES --judge live)

# Build
python3 -m audit_layer write-out session-writes --project DEMO --out WRITES.jsonl
python3 handoffs/audit_to_project.py --record session_writes --from WRITES.jsonl --project COPY
python3 handoffs/project_to_build.py --project COPY --to INPUTS --source proposal.md
(cd verification_procedures && VG_OFFLINE=1 python3 vg.py run graphs/build.yaml --run RUN --inputs INPUTS)

# The results file where the build reads it, and the author's decision on an item
python3 handoffs/results_to_pipeline.py --run RUN --stream prose --project DEMO --product proposal
(cd verification_procedures && python3 vg.py decide --run RUN --item ITEM --approve --by "NAME")
```

The rerun with `make data` and the data report's own rerun need no record. Without the record of file edits, the final-numbers report says no record was given and every number waits for the author. A live model, used by the references and phase reports, reads the provider setting in `CONNECTIONS_HOME` (as in `settings/provider.example.yaml`) and the key in `WORKFLOW_MODEL_KEY`. Point every workflow home (`AUDIT_HOME`, `CONNECTIONS_HOME`, `FEATURES_HOME`, `OBSERVABILITY_HOME`) at folders of their own.

[Back to the README](../README.md)
