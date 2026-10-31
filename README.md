# Verifiable proposal demo

This repository holds a research proposal and its technical appendix, each built from one plain text file by a manuscript workflow, and the verification reports the author reads to check what AI sessions contributed to them. A report lays out what the record of the AI sessions shows and what programs checked. No model gives a verdict in any report. The author approves or holds each item, no item is decided yet, and so every build is marked unverified for every stream.

The text is the author's. It changes only where the pipeline needs it. Author-year citations became keys that print the same way, the appendix's numbers about the prototype became placeholders filled from a numbers file, and the six works the text cites but the author's reference list leaves out were added to `refs.bib`.

A reader can rebuild both documents, read every report, and search the session index. Rerunning the reports that read the record of the AI sessions needs that record, which stays private, so those reports can only be read here (see Rerunning the reports).

## Terms

A few words recur in what follows.

- **The workflow** is the system that builds the documents and runs the reports, the research artifact the appendix describes. **The pipeline** is its build part.
- **A stream** is one kind of verification, prose, citations (shown as the references report), data (shown as the final-numbers report), or build. The build marks each document verified or not for each stream.
- **The record** is the audit layer's store of the AI sessions, their transcripts and tool calls. **The audit home** is the folder that holds it.
- **A handoff** is a script that copies a report's inputs from the project into a new folder. **`vg.py`** is the program that runs a report's procedure, step by step, and writes the report.
- **ForgeCode** and **Claude Code** are the two AI coding programs whose sessions the record holds.
- **A phase** is collection, cleaning, or analysis, as each step of `pipeline.yaml` declares.

## What is here

| Path | What it holds |
|---|---|
| `proposal.md`, `appendix.md` | The two source texts |
| `refs.bib`, `styles/` | The 30 references, the INFORMS citation style, and the Word style file |
| `figures/` | The figures of each document |
| `numbers.yml` | Every number the appendix cites by placeholder, 152 keys, each tied to the output it comes from |
| `pipeline.yaml`, `params.yaml`, `acquisition.yaml` | The two analysis steps with their phase, every analytic choice set once, and the two raw archives with their checksums |
| `s1_artifact_numbers.py`, `s2_live_runs.py` | The two analysis scripts, each with its steps marked |
| `params_io.py`, `results_io.py` | The helpers both scripts share |
| `artifact_public_e22136c.tar`, `artifact_public_f48459a.tar`, `live_runs_2026-10-08.tar` | The raw data, archives of the public research artifact at commit e22136c, the copy the appendix describes, and at the earlier commit f48459a, whose procedures the seven live runs of October 8 used, and those runs packed from it |
| `*.csv` | The analysis outputs |
| `builds/<product>/` | Every numbered build, with its ledger `BUILDS.md` |
| `verification/<product>/<report>/` | Each report, `report.md`, and its results file, `results.json` |
| `verification/<product>/<stream>.json` | The copy of each stream's results file that the build reads |
| `verification/<product>/prose_pin/`, `verification/references_inputs/` | The pin of the author's last draft for each prose report, and the metadata cache the references reports read |
| `settings/provider.example.yaml` | The model settings of the live runs, with the service's address replaced |
| `sessions/` | The public index of the AI sessions behind the reports |
| `tools/` | The conversion scripts, and `check_text.py`, which compares a build's plain text with the original Word file, which is not in this repository |

The reports name the final build's text `draft.md` or `final_text.md`. These are `builds/proposal/v006.md` and `builds/appendix/v010.md`.

## The record behind the reports

The reports read the record of the AI sessions that worked on the proposal, kept in the demo's audit home, which stays out of this repository since it holds whole transcripts. The record holds these sessions, 325 in all.

- The 12 Claude Code sessions from September 10 to October 28 that touched the proposal's folders, with their 267 subagent conversations.
- The 31 ForgeCode conversations from September 30 to October 2, run in the proposal's test folder, 27 of them begun by an agent, so their prompts count as an AI's words.
- The 8 sessions that built this demo, and 7 later ones that tried its README, fixed the workflow's Word adapter, and updated the appendix, its numbers, and its figures for the copy e22136c. The session that coordinated them, and that reran these reports, is the author's own conversation with the AI and is not in the record.

Some files are named as AI output, since AI agents wrote them outside the sessions' own tool calls or before the record begins.

- The research reports in `workflow_for_manuscripts/research/`, written by research agents in July.
- The working files in the proposal's two working folders, less the author's own three files there, a draft written from scratch, a file of the author's own words, and the author's revisions in Word.
- As sources an AI fetched rather than wrote, the paper texts and search results kept with the opening's citation checks. They count as AI output but never as the AI's own words, so they give no reason.

The record has limits, which each report's evidence lets the author weigh.

- It shows who first named a work within the captured sessions and files, not what the author knew before.
- It cannot see what a shell command read, so a shell command's output counts as AI output. A work first seen in a printout of the author's own manuscript therefore shows as from an AI, with the printed words to judge from.
- A file an AI read is dated by when it was read, not when it was written.
- It reads an AI's stated reason only from the words it shows, not from its thinking. The agent that updated the appendix wrote the reason for 54 of its 122 edits only in its thinking, so the prose report shows those changes as having no recorded reason.
- Changes the coordinating session made are not in it. It renamed the archive in `params.yaml` and the scripts' docstrings and added the step marks, so the final-numbers report shows the scripts as differing from the AI's recorded text.

## The reports

### References

For each citation in the final build, the report gives its sentence and who first named the cited work in the record, with the session's public id, the time, how the record named it, and the words. For each citation from an AI it then says whether the work was found, gives the AI's recorded reason, and gives a quote, taken from the record when the record quotes the source and otherwise located in the source by a model, and a program checks every exact quote against the source text.

| Count | Proposal v006 | Appendix v010 |
|---|---|---|
| Citations in the final build | 35 | 3 |
| From an AI | 32 | 3 |
| The author's | 3 | 0 |
| Works not found | 0 | 0 |
| Works not looked up, since they have no DOI | 4 | 1 |
| AI citations with no quote found in their source | 7 | 0 |
| Quotes in the record not found in their source | 10 | 0 |
| AI citations with no recorded reason | 0 | 0 |

The four works with no DOI are healy2020, kapoor2026, oxford2026, and wiley2025. Of the seven AI citations with no quote found, the model found no passage bearing on the sentence for three (boiko2023, doshi2024, and lee2024, which share one sentence), gave a paraphrase for two, and gave a passage for two that the program could not find word for word. The model's findings vary between runs, and in an earlier run it located a passage for boiko2023, so each answer it gave is saved in the run folder. A quote in the record that is not in its source is most often other words the AI put in double quotes, and each is shown beside the citation for the author to read. Reports in `verification/proposal/citations/` and `verification/appendix/citations/`.

### Prose

Each prose report compares the text right after conversion from Word (commit 769b8f0) with the current source text, placeholders and all, and takes from the record which changes an AI made and the reason it stated. Its opening says "the final build's text", but it reads the source. A program flags an AI change with no recorded reason as blocking and one that alters a number, a citation, a quotation, a negation, or a claim's strength as a warning. No model judges any change.

In the proposal, all 72 changes are AI changes by the record. Fifty-six have no recorded reason, 55 of them the deletes of the typed reference list, which the build now prints from `refs.bib`, and 60 are flagged as content changes. In the appendix, 185 of 201 changes are AI changes, 130 have no recorded reason, mostly for the reason given above under the record's limits, and 98 are flagged as content changes. In both, one more blocking item says the record's first entry is an AI's write of the whole converted file, so the record cannot tell which later changes are the AI's beyond the ones it names. The appendix's 16 changes the record does not name are therefore listed as the author's on that understanding, though no person edited this text. They are pieces of the AI's larger edits that the record cannot split, most of them deletions in the replaced example report. Reports in `verification/proposal/prose/` and `verification/appendix/prose/`.

### Final numbers

The final-numbers report lists each of the 152 numbers in `numbers.yml` with the output and the script that produce it. By the record of the AI's file edits, AI sessions wrote both scripts, so all 152 come from AI work. The report shows the AI's 22 changes to the scripts, 10 of them with no recorded reason, which a program flags as blocking, and lists the 37 parameters the AI set for the author to check, 9 of them set with no recorded reason, also blocking. Of its other 7 warnings, 5 say the scripts no longer hold the AI's recorded text, since later edits replaced it, and 2 say a script's Inputs section disagrees with `pipeline.yaml`. Its reproducibility section reran the pipeline from the raw archives in an empty folder. Both steps reproduce their outputs, and all 152 numbers agree with the rerun. Report in `verification/appendix/data/`.

### Data collection, cleaning, and analysis

Each phase report gives an outline of the phase's steps in one or two words, then each step's exact code with its file and lines, then the sentences of the appendix that a model found describing the phase, each with where the scripts carry it out or "missing". A program checks that each quote is in the appendix and that each place is lines of a script the pipeline declares. Each description is an item for the author, to approve as a fair account of what the scripts do or to hold.

Both analysis steps declare the phase analysis, since the raw archives were collected outside the pipeline and nothing is cleaned. So the analysis report outlines 14 steps, 8 in `s1_artifact_numbers.py` and 6 in `s2_live_runs.py`, and lists 47 descriptions, 19 of them carried out at a confirmed place and 28 missing from the scripts, such as the sentence that a placeholder with no value stops the build. The collection and cleaning reports have no step and, in this run, no sentence. In an earlier run on the previous appendix the model gave 60 sentences as describing cleaning, most of them analysis sentences. Reports in `verification/appendix/data_collection/`, `data_cleaning/`, and `data_analysis/`.

### Build

The build procedure was not changed, and its report uses the workflow's own terms. Both build runs check the same packed copy of the whole project, so the two reports are the same. They give 81 blocking findings, 10 on the proposal and 71 on the appendix, all from the check for typed results, which flags any number in the text that equals a value in `numbers.yml`, so small numbers in labels such as Stage 1 or Table 2 are false alarms. Its Item column shows the matched value, not a line number. They also give 60 warnings, 59 on bare numbers and 1 that the author's build preferences are not written down. The ledger matches every build file on disk, each document has one source, and no AI session wrote to a build folder. The rebuild check did not run on any build. Reports in `verification/proposal/build/` and `verification/appendix/build/`.

## Rebuilding

You need Python 3.9 with PyYAML and python-docx, pandoc (3.9.0.2 made these builds), and the workflow. The reports here were made with the workflow at the candidate public copy, commit e22136c. Name its folder with `WORKFLOW=`.

```
make proposal WORKFLOW=/path/to/workflow
make appendix WORKFLOW=/path/to/workflow
```

Without `WORKFLOW=`, the `Makefile` looks for the workflow in the author's own folder layout and stops with "No module named ospipe". Each build fills every placeholder from `numbers.yml`, stops if one has no value, writes the next numbered build in `builds/<product>/`, and adds a ledger row that names each stream's current results and whether it is verified. To compute the numbers again from the raw archives, run `make data` (about 30 minutes, mostly the artifact's test suites) and then `make manifest`.

## Rerunning the reports

The references, prose, and build reports, and the final-numbers report's account of the AI's edits, read the record, and the record is not in this repository. Neither are the cited works' texts, most of which are not openly licensed. These reports can be read here but not rerun from here. A report run with an empty record says nothing about it. The prose report then lists every change as the author's, and the build report counts no AI write, so a reader who starts an empty audit home gets clean-looking reports that are wrong. With the record in place, the commands below rerun each report. The phase reports and the final-numbers report's rerun of the pipeline need no record.

Run them from the workflow's folder. `DEMO` is this folder, at the path the record was captured with, and `COPY` is a copy of it, made with `git archive`, into which the records go. Each `vg.py run` writes its report to `RUN/files/report.md` and its items to `RUN/results.json`. Name each run as the published ones are named, such as `appendix_prose`, since the folder's name becomes the run's id.

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

## The session index

`sessions/` lists 181 of the record's sessions, those that touched this folder or the proposal's earlier folders (its working folder, the special issue folder, and its test folder), and any session an item of the final reports names. They are 12 Claude Code sessions with 129 of their subagent conversations, the 31 ForgeCode conversations, and 9 of the 15 sessions that built and updated the demo. Those 9 name as their parent the coordinating session, which has no row since it is not in the record. Nineteen sessions led to an AI contribution in the final reports, 292 in all, the 72 changes in the proposal's prose report, the 185 in the appendix's, and the 35 citations. The final-numbers report's items name no session, so its 22 script changes are not counted there. A citation first named in a file with no session, such as one of July's research reports, is linked to the first session that named it.

Each session has a public id, S followed by 12 hex characters of a hash of the harness's own id, which cannot be turned back into it, and the reports name sessions only by it. For each session the index gives its start and length, the harness and the models, its tool calls counted by verb, the files it read, edited, and wrote, named inside this folder or inside an earlier folder, and the checksum and size of its transcript. Transcripts are not included. A model wrote a title, gist, summary, and keywords for 3 of the demo-building sessions, marked as not reviewed by the author, with the author's name written as [withheld]. The proposal's sessions have none.

To search the index, open `sessions/sessions.csv`, which GitHub shows as a table with a search box, or open `sessions/index.html` in a browser, which has a search box and a box to keep only the sessions with a contribution. Each session also has its own page, `sessions/<public id>.md`. A transcript shared later can be checked against its row's checksum, as `sessions/README.md` explains. That README says a session touched the project when it ran in this folder or touched a file in it, and here the earlier folders count as this folder.

## Models and services

- `qwen/qwen3.8-27b` located passages in the references reports and found the descriptions in the phase reports, through a university-hosted model service, at temperature 0 with an output limit of 65,536 tokens (`settings/provider.example.yaml`). No model judged anything.
- Crossref and DataCite supplied the record of each DOI on October 31. The 23 records are kept in `verification/references_inputs/metadata_cache.json`, which the references runs read, so a rerun with the record gives the same lookups offline.
- A search tool found open copies of the cited works. The texts are kept out of this repository, since most are not openly licensed, and `sources_manifest.yaml` says where each came from.
- pandoc made every build, with the INFORMS citation style.

## Before this is shared

- The history gets a fresh start, since every commit carries the author's email address.
- Whether the journal allows posting the submitted proposal and appendix before a decision needs checking.
