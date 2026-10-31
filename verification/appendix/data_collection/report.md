# Data collection report

This report shows the data collection for the scholar to verify. The outline lists each step with a short title, and under it each title is shown again with the exact code that carries it out, copied from its script with its file and lines. A step is a section a script marks with a comment line `# step: <title>`, or, in a Python script that marks none, a function the script calls, in the order it calls them. The descriptions table lists each sentence of the final build's text that describes this phase, as one model step found them, with where the scripts carry it out or missing. A program checks that each quote is in the text and that each place is in the scripts. No model judges whether a description fits its code, and the scholar approves or holds each description.

Pipeline steps in this phase 0, outline steps 0. Descriptions found 0 (missing from the scripts 0, quotes not in the text 0, places not in the scripts 0).

## Summary

- Blocking: 0
- Warnings: 0
- Notes: 1

## Problems

None.

## Outline

No step of the pipeline declares the phase collection (`phase: collection` in `pipeline.yaml`).

## Code

None.

## Descriptions

Each row is a sentence of the final build's text that the finding step gave as describing this phase, with the places in the scripts it gave. The last two columns are the program's checks. A place is confirmed when it is lines of a script the pipeline declares, and the steps it falls in are named beside it.

None.

## Files read

- `final_text.md`, the final build's text, sha256:6cfef15424907eb740a62a668ab9aaf9cecadbe47765b67dce2e205bcd4fb076
- `pipeline.yaml`, the pipeline, sha256:5d2b08aebbf298038c44b8ae6e0d7e23f33a141ef3c285882a85436572d31c3c
- `s1_artifact_numbers.py`, the script of step artifact, sha256:c0d7c3fbf27aa4c612ca7db1da28dc4720df03271a727d126b28220a4d01da27
- `s2_live_runs.py`, the script of step live, sha256:7f78483fe3e311f914f4c2353090b9bcd97232c49e0fa6fcc0343e7b3301fe17

## Notes

- outline_steps / collection: No step of the pipeline declares the phase collection.
