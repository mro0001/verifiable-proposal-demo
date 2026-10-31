# References report

The text read is the final build's text, `draft.md` (sha256:6cfef15424907eb740a62a668ab9aaf9cecadbe47765b67dce2e205bcd4fb076). Each citation in it is listed with who first named the cited work in the record of sessions and artifacts. For each citation from an AI, the report says whether the work could be found, and for each work found it gives the AI's recorded reason and a quote, which a program then looks for in the source text. Nothing here is a verdict. The scholar approves or holds each citation from an AI and each one the record never names.

| Count | Number |
|---|---|
| Citations in the final build | 3 |
| From an AI | 3 |
| The scholar's | 0 |
| Never named in the record | 0 |
| Works not found | 0 |
| Works not looked up | 1 |
| AI citations with no quote found in their source | 0 |
| Quotes in the record not found in their source | 0 |
| AI citations with no recorded reason | 0 |

## Citations

**From an AI (3)**

### r01: @healy2020

- **Sentence:** The reproducible pipeline assembles research products through a build script [@healy2020].
- **Origin:** First named by an AI at 2026-07-28T02:45:10.124Z in research/workflow_lit_socsci.md, in a file an AI wrote, where the record reads "Use the concept DOI and name the version you read. - **Healy, K. *The Plain Person's Guide to Plain Text Social Science*.** https://plain-text.co/, page dated 2019-10-04; PDF at https://kieranhealy.org/files/papers/plain-person-text.pdf (..."
- **Session:** Sf2b3ddaba981
- **Reference:** Healy, K. (2020). The Plain Person’s Guide to Plain-Text Social Science.
- **Found:** no DOI, not looked up
- **Notes:** @healy2020 has no DOI, so it was not looked up
- **Trail:** origin from citation_provenance.yaml (record 04_read_origin); lookup (records 05_fetch_metadata, 06_check_existence); times are each record's started_at

### r02: @lu2026

- **Sentence:** A procedural graph [@lu2026] is a record of how to carry out a task, kept in the system's knowledge base so that a person can read and edit it.
- **Origin:** First named by an AI at 2026-07-31T19:57:43.088Z in research/05_ai_research_workflow/report.md, in a file an AI wrote, where the record reads "**Agentic science: milestone or hazard?** Nature publication and a passed workshop review [Lu et al. 2026, ABSTRACT] versus 42% failed experiments and hallucinated numerics in independent evaluation [Beel et al. 2025, ABSTRACT], plus the prior-file..."
- **Session:** Sfdc8140a6627
- **Reference:** Lu, Y., Chen, Y., Wu, S., Arık, S. (2026). Procedural graphs: Self-evolving execution structures for LLM agents. doi:10.48550/arXiv.2609.09153
- **Found:** found in the metadata cache (DOI 10.48550/arxiv.2609.09153). The record reads Lu, Y., Chen, Y., Wu, S., Arık, S. (2026). Procedural Graphs: Self-Evolving Execution Structures for LLM Agents. arXiv. Type Preprint.
- **Reason:** "**Agentic science: milestone or hazard?** Nature publication and a passed workshop review [Lu et al. 2026, ABSTRACT] versus 42% failed experiments and hallucinated numerics in independent evaluation [Beel et al. 2025, ABSTRACT], plus the prior-file's Messeri & Crockett illusion-of-understanding counterweight. The debate is live and the manuscript sits exactly on its fault line." (said by the AI at 2026-07-31T19:57:43.088Z in research/05_ai_research_workflow/report.md)
- **Quote:** "The PG keeps a task domain’s procedural knowledge outside the model weights, where it can be inspected, retrieved at each step, and edited without retraining." (located by live:qwen/qwen3.8-27b, at p. 2)
- **Quote check:** found in source_lu2026.txt, which holds the full text
- **Trail:** origin from citation_provenance.yaml (record 04_read_origin); lookup (records 05_fetch_metadata, 06_check_existence); source text source_lu2026.txt sha256:0e208872cd54... (record 07_pin_sources); passage located by live:qwen/qwen3.8-27b (record 09_locate_passage); quote checked by a program (record 10_verify_quote); times are each record's started_at

### r03: @lu2026

- **Sentence:** Running the graph this way is our extension of @lu2026.
- **Origin:** First named by an AI at 2026-07-31T19:57:43.088Z in research/05_ai_research_workflow/report.md, in a file an AI wrote, where the record reads "**Agentic science: milestone or hazard?** Nature publication and a passed workshop review [Lu et al. 2026, ABSTRACT] versus 42% failed experiments and hallucinated numerics in independent evaluation [Beel et al. 2025, ABSTRACT], plus the prior-file..."
- **Session:** Sfdc8140a6627
- **Reference:** Lu, Y., Chen, Y., Wu, S., Arık, S. (2026). Procedural graphs: Self-evolving execution structures for LLM agents. doi:10.48550/arXiv.2609.09153
- **Found:** found in the metadata cache (DOI 10.48550/arxiv.2609.09153). The record reads Lu, Y., Chen, Y., Wu, S., Arık, S. (2026). Procedural Graphs: Self-Evolving Execution Structures for LLM Agents. arXiv. Type Preprint.
- **Reason:** "**Agentic science: milestone or hazard?** Nature publication and a passed workshop review [Lu et al. 2026, ABSTRACT] versus 42% failed experiments and hallucinated numerics in independent evaluation [Beel et al. 2025, ABSTRACT], plus the prior-file's Messeri & Crockett illusion-of-understanding counterweight. The debate is live and the manuscript sits exactly on its fault line." (said by the AI at 2026-07-31T19:57:43.088Z in research/05_ai_research_workflow/report.md)
- **Quote:** none located
- **Notes:** the passage step found no passage in the source text of @lu2026 that bears on the sentence
- **Trail:** origin from citation_provenance.yaml (record 04_read_origin); lookup (records 05_fetch_metadata, 06_check_existence); source text source_lu2026.txt sha256:0e208872cd54... (record 07_pin_sources); passage located by live:qwen/qwen3.8-27b (record 09_locate_passage); times are each record's started_at

**Never named in the record (0)**

None.

**The scholar's citations, not checked further (0)**

None.

## Notes

- check_existence / healy2020: @healy2020 has no DOI, so it was not looked up
- match_references / ans2026: @ans2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / astrom2008: @astrom2008 is in the reference list and not cited in the final build, so it is not checked
- match_references / boiko2023: @boiko2023 is in the reference list and not cited in the final build, so it is not checked
- match_references / dellacqua2026: @dellacqua2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / doshi2024: @doshi2024 is in the reference list and not cited in the final build, so it is not checked
- match_references / eubank2016: @eubank2016 is in the reference list and not cited in the final build, so it is not checked
- match_references / gartenberg2026: @gartenberg2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / he2026: @he2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / hosseini2023: @hosseini2023 is in the reference list and not cited in the final build, so it is not checked
- match_references / jcgm2012: @jcgm2012 is in the reference list and not cited in the final build, so it is not checked
- match_references / kapoor2026: @kapoor2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / kusumegi2025: @kusumegi2025 is in the reference list and not cited in the final build, so it is not checked
- match_references / lee2024: @lee2024 is in the reference list and not cited in the final build, so it is not checked
- match_references / liang2025: @liang2025 is in the reference list and not cited in the final build, so it is not checked
- match_references / linardon2026: @linardon2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / luccioni2024: @luccioni2024 is in the reference list and not cited in the final build, so it is not checked
- match_references / oxford2026: @oxford2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / resnik2025: @resnik2025 is in the reference list and not cited in the final build, so it is not checked
- match_references / rule2018: @rule2018 is in the reference list and not cited in the final build, so it is not checked
- match_references / schulz2026: @schulz2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / stodden2010: @stodden2010 is in the reference list and not cited in the final build, so it is not checked
- match_references / suchak2025: @suchak2025 is in the reference list and not cited in the final build, so it is not checked
- match_references / trisovic2022: @trisovic2022 is in the reference list and not cited in the final build, so it is not checked
- match_references / walters2023: @walters2023 is in the reference list and not cited in the final build, so it is not checked
- match_references / wiley2025: @wiley2025 is in the reference list and not cited in the final build, so it is not checked
- match_references / yuan2025: @yuan2025 is in the reference list and not cited in the final build, so it is not checked
- match_references / zhang2026: @zhang2026 is in the reference list and not cited in the final build, so it is not checked
- match_references / zheng2026: @zheng2026 is in the reference list and not cited in the final build, so it is not checked
- verify_quote / r03: the passage step found no passage in the source text of @lu2026 that bears on the sentence
