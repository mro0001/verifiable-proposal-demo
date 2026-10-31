# We ran the workflow on its own proposal

AI sessions helped write this research proposal and its technical appendix. The [workflow](https://github.com/mro0001/verifiable-social-science-workflow) found each AI contribution, checked it, and wrote a report for the author. No model gives a verdict in any report. The author approves or holds each item. None is decided yet, so both documents are marked unverified.

![The proposal's layer figure filled in with what the workflow found. Prose: 273 edits, 257 by an AI, 186 with no recorded reason. References: 38 citations, 35 first named by an AI, 7 with no quote found in the source. Data and analysis code: 152 numbers from 2 scripts an AI wrote, all reproduce from the raw data. Build: 16 numbered builds, no AI wrote to a build.](project/figures/readme/results.png)

| Stream | What the check found | Reports |
|---|---|---|
| Prose | 257 of 273 edits were made by an AI. Each is shown with the reason the AI gave, and 186 have none on record ([why](docs/reading_reports.md#prose)). | [proposal](project/verification/proposal/prose/report.md) · [appendix](project/verification/appendix/prose/report.md) |
| References | 35 of 38 citations were first named by an AI. For 7 of them, no quote was found in the source. | [proposal](project/verification/proposal/citations/report.md) · [appendix](project/verification/appendix/citations/report.md) |
| Data and analysis code | AI sessions wrote both analysis scripts. All 152 numbers in the appendix reproduce from the raw data. | [final numbers](project/verification/appendix/data/report.md) · [analysis steps](project/verification/appendix/data_analysis/report.md) |
| Build | Each document has one source, and no AI wrote to a build folder. The report's 81 flags come from one check that also matches labels such as "Stage 1" ([why](docs/reading_reports.md#build)). | [proposal](project/verification/proposal/build/report.md) · [appendix](project/verification/appendix/build/report.md) |

## Try it

```
git clone https://github.com/mro0001/verifiable-social-science-workflow
git clone https://github.com/mro0001/verifiable-proposal-demo
cd verifiable-proposal-demo/project
make proposal
```

This rebuilds the proposal from `project/proposal.md` as the next numbered build, `project/builds/proposal/v007.docx`. With pandoc 3.9.0.2 it is byte for byte the same as v006. It needs Python 3.9 or later with PyYAML and python-docx, and pandoc. `make data` recomputes all 152 numbers from the raw archives, in about 30 minutes.

## Read more

- [How to read the reports](docs/reading_reports.md): one entry explained field by field, and what each report found
- [The record behind the reports](docs/record.md): the 325 AI sessions, what the record cannot show, and the searchable session index ([`sessions.csv`](project/sessions/sessions.csv))
- [The project folder](project/README.md): what each file is
- [Rebuild and rerun](docs/rebuild.md): the build commands, and why most reports can be read here but not rerun
