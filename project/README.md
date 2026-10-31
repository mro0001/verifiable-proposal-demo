# The project folder

The proposal and its appendix as a project laid out by the workflow. Every path in the reports is a path inside this folder. Run `make` here.

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

[Back to the README](../README.md)
