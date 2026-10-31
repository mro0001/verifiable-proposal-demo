# The record behind the reports

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

## The session index

`sessions/` lists 181 of the record's sessions, those that touched this folder or the proposal's earlier folders (its working folder, the special issue folder, and its test folder), and any session an item of the final reports names. They are 12 Claude Code sessions with 129 of their subagent conversations, the 31 ForgeCode conversations, and 9 of the 15 sessions that built and updated the demo. Those 9 name as their parent the coordinating session, which has no row since it is not in the record. Nineteen sessions led to an AI contribution in the final reports, 292 in all, the 72 changes in the proposal's prose report, the 185 in the appendix's, and the 35 citations. The final-numbers report's items name no session, so its 22 script changes are not counted there. A citation first named in a file with no session, such as one of July's research reports, is linked to the first session that named it.

Each session has a public id, S followed by 12 hex characters of a hash of the harness's own id, which cannot be turned back into it, and the reports name sessions only by it. For each session the index gives its start and length, the harness and the models, its tool calls counted by verb, the files it read, edited, and wrote, named inside this folder or inside an earlier folder, and the checksum and size of its transcript. Transcripts are not included. A model wrote a title, gist, summary, and keywords for 3 of the demo-building sessions, marked as not reviewed by the author, with the author's name written as [withheld]. The proposal's sessions have none.

To search the index, open `sessions/sessions.csv`, which GitHub shows as a table with a search box, or open `sessions/index.html` in a browser, which has a search box and a box to keep only the sessions with a contribution. Each session also has its own page, `sessions/<public id>.md`. A transcript shared later can be checked against its row's checksum, as `sessions/README.md` explains. That README says a session touched the project when it ran in this folder or touched a file in it, and here the earlier folders count as this folder.

## Models and services

- `qwen/qwen3.8-27b` located passages in the references reports and found the descriptions in the phase reports, through a university-hosted model service, at temperature 0 with an output limit of 65,536 tokens (`settings/provider.example.yaml`). No model judged anything.
- Crossref and DataCite supplied the record of each DOI on October 31. The 23 records are kept in `verification/references_inputs/metadata_cache.json`, which the references runs read, so a rerun with the record gives the same lookups offline.
- A search tool found open copies of the cited works. The texts are kept out of this repository, since most are not openly licensed, and `sources_manifest.yaml` says where each came from.
- pandoc made every build, with the INFORMS citation style.

[Back to the README](../README.md)
