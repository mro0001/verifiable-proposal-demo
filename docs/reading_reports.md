# How to read the reports

Each report lists items for the author to approve or hold. It lays out what the record of the AI sessions shows and what programs checked. No model gives a verdict in any report.

## Where they are

| Stream | Proposal | Appendix |
|---|---|---|
| Prose | [report](../verification/proposal/prose/report.md) | [report](../verification/appendix/prose/report.md) |
| References | [report](../verification/proposal/citations/report.md) | [report](../verification/appendix/citations/report.md) |
| Data and analysis code | | [final numbers](../verification/appendix/data/report.md), [collection](../verification/appendix/data_collection/report.md), [cleaning](../verification/appendix/data_cleaning/report.md), [analysis](../verification/appendix/data_analysis/report.md) |
| Build | [report](../verification/proposal/build/report.md) | [report](../verification/appendix/build/report.md) |

Each report folder also holds `results.json`, the items with their decisions, which the build reads.

## One entry, field by field

Entry r18 of the [proposal's references report](../verification/proposal/citations/report.md#r18-walters2023), shortened:

| Field | In r18 | What it tells you |
|---|---|---|
| Sentence | "Plausibility failures appear in hallucinated citations [@walters2023], ..." | Where the final build cites the work |
| Origin | First named by an AI on July 31, in `research/06_provenance_verification/report.md`, a file an AI wrote | Who first named the work in the record, and where |
| Session | `Sf2b3ddaba981` | The session's public id, a row in [`sessions/sessions.csv`](../sessions/sessions.csv) |
| Found | found, DOI 10.1038/s41598-023-41032-5 | Whether the work exists, looked up by its DOI |
| Reason | "The first careful audit of LLM-generated bibliographies ..." | Why the AI cited it, in its own recorded words |
| Quote | "55% of the GPT-3.5 citations but just 18% of the GPT-4 citations are fabricated" | A passage of the source, taken from the record or, when the record has none, located by a model |
| Quote check | found in `source_walters2023.txt` | Whether a program found the quote word for word in the source text |
| Trail | records 04 to 10 | The step records of the run behind each field |

The author reads the entry and approves or holds it. The other reports follow the same pattern: each item, the evidence from the record, what a program checked, and a decision left to the author.

## Terms

A few words recur in what follows.

- **The workflow** is the system that builds the documents and runs the reports, the research artifact the appendix describes. **The pipeline** is its build part.
- **A stream** is one kind of verification, prose, citations (shown as the references report), data (shown as the final-numbers report), or build. The build marks each document verified or not for each stream.
- **The record** is the audit layer's store of the AI sessions, their transcripts and tool calls. **The audit home** is the folder that holds it.
- **A handoff** is a script that copies a report's inputs from the project into a new folder. **`vg.py`** is the program that runs a report's procedure, step by step, and writes the report.
- **ForgeCode** and **Claude Code** are the two AI coding programs whose sessions the record holds.
- **A phase** is collection, cleaning, or analysis, as each step of `pipeline.yaml` declares.

## What each report found

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

[Back to the README](../README.md)
