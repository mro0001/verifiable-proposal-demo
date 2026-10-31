# Data analysis report

This report shows the data analysis for the scholar to verify. The outline lists each step with a short title, and under it each title is shown again with the exact code that carries it out, copied from its script with its file and lines. A step is a section a script marks with a comment line `# step: <title>`, or, in a Python script that marks none, a function the script calls, in the order it calls them. The descriptions table lists each sentence of the final build's text that describes this phase, as one model step found them, with where the scripts carry it out or missing. A program checks that each quote is in the text and that each place is in the scripts. No model judges whether a description fits its code, and the scholar approves or holds each description.

Pipeline steps in this phase 2, outline steps 14. Descriptions found 47 (missing from the scripts 28, quotes not in the text 0, places not in the scripts 0).

## Summary

- Blocking: 0
- Warnings: 28
- Notes: 0

## Problems

| Severity | Check | Item | Problem | Evidence |
|---|---|---|---|---|
| warning | check_descriptions | d06 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d07 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d09 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d13 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d15 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d16 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d19 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d20 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d21 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d22 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d24 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d25 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d26 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d27 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d28 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d30 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d31 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d35 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d36 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d37 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d38 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d39 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d40 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d41 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d42 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d43 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d44 | The finding step gave no place in the scripts that carries out this description. |  |
| warning | check_descriptions | d47 | The finding step gave no place in the scripts that carries out this description. |  |

## Outline

- `artifact`, `s1_artifact_numbers.py`
  - Read parameters
  - Read files
  - Unpack
  - Run tests
  - A4 commands
  - Report excerpt
  - Count files
  - Write tables
- `live`, `s2_live_runs.py`
  - Read parameters
  - Read answers
  - Planted faults
  - Count runs
  - No-answer trial
  - Write table

## Code

### Read parameters

`s1_artifact_numbers.py` lines 82-104

```python
# step: Read parameters
import ast
import collections
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import xml.etree.ElementTree as ET

import yaml

import params_io
import results_io

P = params_io.Params(step="artifact", script="s1_artifact_numbers.py")
VP = "verification_procedures"
HOMES = ("HOME", "AUDIT_HOME", "CONNECTIONS_HOME", "FEATURES_HOME", "XDG_CONFIG_HOME")
VERSION_LINE = re.compile(r"^(v\S+) -> ", re.M)
Case = collections.namedtuple("Case", "suite file test outcome")
```

### Read files

`s1_artifact_numbers.py` lines 107-126

```python
# step: Read files
def pairs(text):
    """Split a parameter written as name=value words into (name, value) pairs, in order."""
    return [tuple(word.split("=", 1)) for word in text.split()]


def read_json(path):
    """Read one JSON file."""
    with open(path) as f:
        return json.load(f)


def items_of(data):
    """Return the list of items of a findings or table file, whether it is a list or holds items."""
    return data["items"] if isinstance(data, dict) else data


def severities(path):
    """Count the findings of a run's findings file by severity."""
    return collections.Counter(f["severity"] for f in items_of(read_json(path)))
```

### Unpack

`s1_artifact_numbers.py` lines 129-158

```python
# step: Unpack
def unpack(archive, base, name):
    """Unpack the archive into the folder name inside base and return its path."""
    root = os.path.join(base, name)
    with tarfile.open(archive) as tf:
        tf.extractall(root)
    return root


def child_env(base):
    """Return the environment every command in the artifact runs with (see Assumptions)."""
    env = dict(os.environ)
    for name in HOMES:
        env[name] = os.path.join(base, "homes", name.lower())
        os.makedirs(env[name], exist_ok=True)
    env["VG_OFFLINE"] = "1"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    harness = P["harness_programs"].split()
    # Drop each folder on the command path that holds a harness program.
    keep = [d for d in env.get("PATH", "").split(os.pathsep)
            if d and not any(os.path.exists(os.path.join(d, h)) for h in harness)]
    env["PATH"] = os.pathsep.join(keep)
    return env


def run(cmd, cwd, env):
    """Run one command with its output captured, not passed on, and return its standard output."""
    proc = subprocess.run(cmd, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          universal_newlines=True)
    return proc.stdout
```

### Run tests

`s1_artifact_numbers.py` lines 161-211

```python
# step: Run tests
def outcome(case):
    """Return passed, failed, or skipped for one testcase element of a JUnit report."""
    tags = {child.tag for child in case}
    if tags & {"failure", "error"}:
        return "failed"
    if "skipped" in tags:
        return "skipped"
    return "passed"


def run_suites(root, env, base):
    """Run each suite once with pytest and return one Case for every test it ran."""
    cases = []
    for name, spec in pairs(P["suites"]):
        folder, target = spec.split(":", 1)
        report = os.path.join(base, "junit_" + name + ".xml")
        run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--rootdir", root,
             "-o", "junit_family=xunit1", "--junitxml", report, target],
            os.path.join(root, folder), env)
        for case in ET.parse(report).iter("testcase"):
            cases.append(Case(name, case.get("file", ""),
                              case.get("classname", "") + "::" + case.get("name", ""), outcome(case)))
    return cases


def in_group(path, paths):
    """True when a test file is one of the group's files or lies in one of its folders."""
    return any(path == p or (p.endswith("/") and path.startswith(p)) for p in paths.split(","))


def suite_counts(cases):
    """Count passed tests by suite and by named group, plus failed and skipped by suite."""
    results = {}
    names = [name for name, _ in pairs(P["suites"])]
    for name in names:
        mine = [c for c in cases if c.suite == name]
        results["tests." + name] = sum(c.outcome == "passed" for c in mine)
        results["tests." + name + ".failed"] = sum(c.outcome == "failed" for c in mine)
        results["tests." + name + ".skipped"] = sum(c.outcome == "skipped" for c in mine)
    passed = [c for c in cases if c.outcome == "passed"]
    results["tests.suites"] = len(names)
    results["tests.total"] = len(passed)
    groups = dict(pairs(P["test_groups"]))
    for group, paths in groups.items():
        results["tests." + group] = sum(in_group(c.file, paths) for c in passed)
    terms = P["slides_terms"].lower().split()
    slide_paths = groups[P["slides_group"]]
    results["tests.slides"] = sum(in_group(c.file, slide_paths) and any(t in c.test.lower() for t in terms)
                                  for c in passed)
    return results
```

### A4 commands

`s1_artifact_numbers.py` lines 214-324

```python
# step: A4 commands
def a4_runs():
    """Return each A4 run on seeded test files as label: (graph, folder under fixtures/), in order."""
    return {label: tuple(spec.split(":", 1)) for label, spec in pairs(P["a4_runs"])}


def demo(name):
    """Return the README's run folder runs/demo_<name>, relative to the procedures' folder."""
    return os.path.join("runs", "demo_" + name)


def judged_items(records):
    """Add up the items the judgment steps of a run put to a model or a recorded answer."""
    total = 0
    for name in sorted(os.listdir(records)):
        execution = read_json(os.path.join(records, name)).get("execution") or {}
        if execution.get("type") == "judgment":
            total += execution.get("items", 0)
    return total


def sample_block(root, env, results):
    """Run the A4 second block: the sample project's two builds, the data handoff and data run,
    and the phase handoff and the data analysis run with the sample's recorded answers."""
    sample = os.path.join(root, P["sample_project"])
    vp = os.path.join(root, VP)
    # The README's relative paths, from the sample project's folder and from the procedures' folder.
    project = os.path.relpath(sample, vp)
    handoffs = os.path.relpath(os.path.join(root, "handoffs"), vp)
    build = [sys.executable, "-m", "ospipe", "build"]
    build_env = dict(env, PYTHONPATH=os.path.relpath(os.path.join(root, "ospipe"), sample))
    run([sys.executable, "s1_results.py"], sample, env)
    out_m = run(build + ["--manuscript", "manuscript.md", "--manifest", "numbers.yml", "--tables-dir", ".",
                         "--bib", "refs.bib", "--builds-dir", "builds/manuscript", "--purpose", "sample manuscript"],
                sample, build_env)
    out_s = run(build + ["--manuscript", "slides.md", "--manifest", "numbers.yml", "--tables-dir", ".",
                         "--to", "revealjs", "--builds-dir", "builds/slides", "--purpose", "sample slides"],
                sample, build_env)
    versions = []
    for out in (out_m, out_s):
        found = VERSION_LINE.search(out)
        versions.append(found.group(1) if found else "none")
    results["sample.manuscript_version"], results["sample.slides_version"] = versions
    # One version when every build wrote the same one, otherwise each build's own.
    results["sample.version"] = "/".join(sorted(set(versions)))
    slides = os.path.join(sample, "builds", "slides", versions[-1] + ".html")
    with open(slides) as f:
        results["sample.slides"] = f.read().count("<section")
    run([sys.executable, os.path.join(handoffs, "project_to_data.py"), "--project", project,
         "--to", demo("sample_inputs")], vp, env)
    run([sys.executable, "vg.py", "run", os.path.join("graphs", "data.yaml"), "--run", demo("sample"),
         "--inputs", demo("sample_inputs")], vp, env)
    run([sys.executable, os.path.join(handoffs, "project_to_data_phases.py"), "--project", project,
         "--to", demo("sample_phases")], vp, env)
    run([sys.executable, "vg.py", "run", os.path.join("graphs", "data_analysis.yaml"), "--run",
         demo("sample_analysis"), "--inputs", demo("sample_phases"),
         "--judge", "recorded:" + os.path.join(project, "recorded_phases.json")], vp, env)
    files = os.path.join(vp, demo("sample"), "files")
    counts = severities(os.path.join(files, "findings.json"))
    results["sample.blocking"] = counts["blocking"]
    results["sample.warnings"] = counts["warning"]
    results["sample.notes"] = counts["info"]
    checked = items_of(read_json(os.path.join(files, "numbers_check.json")))
    results["sample.numbers"] = sum(bool(row.get("ok")) for row in checked)
    results["sample.numbers_listed"] = len(checked)
    fields = read_json(os.path.join(vp, demo("sample_analysis"), "files", "fields.json"))
    described = [it for it in fields["items"] if it.get("kind") == "description"]
    results["sample.analysis_steps"] = fields["run"]["n_steps"]
    results["sample.analysis_descriptions"] = len(described)
    results["sample.analysis_confirmed"] = sum(it.get("quote_found") is True and
                                               it.get("location_status") == "confirmed" for it in described)


def run_seeded(vp, env, label, graph, folder, results):
    """Run one procedure or phase report on its seeded test files as the README gives it, replay or
    score the run when params.yaml names it, and keep what it reports under the run's label."""
    inputs = os.path.join("fixtures", folder, "seeded")
    graph_file = os.path.join("graphs", graph + ".yaml")
    cmd = [sys.executable, "vg.py", "run", graph_file, "--run", demo(graph), "--inputs", inputs]
    if label in P["judged_runs"].split():
        cmd += ["--judge", "recorded:" + os.path.join(inputs, "recorded_judge.json")]
    run(cmd, vp, env)
    with open(os.path.join(vp, graph_file)) as f:
        results[label + ".steps"] = len(yaml.safe_load(f)["nodes"])
    records = os.path.join(vp, demo(graph), "records")
    results[label + ".steps_run"] = len([n for n in os.listdir(records) if n.endswith(".json")])
    if label in P["judged_runs"].split():
        results[label + ".judged"] = judged_items(records)
    if label in P["replayed_runs"].split():
        verify = run([sys.executable, "vg.py", "verify", "--run", demo(graph)], vp, env)
        results[label + ".replays"] = verify.count("replay matches")
    if label in P["scored_runs"].split():
        run([sys.executable, "vg.py", "score", "--run", demo(graph), "--truth", os.path.join(inputs, "truth.yaml")],
            vp, env)
        score = read_json(os.path.join(vp, demo(graph), "score.json"))
        results[label + ".faults"] = score["faults"]
        results[label + ".caught"] = len(score["caught"])
        results[label + ".missed"] = len(score["missed"])
        results[label + ".recall"] = score["recall"]
        results[label + ".extras"] = len(score["extra_findings"])


def a4_blocks(root, env):
    """Run the A4 second, third, and fourth blocks and return what they report, with the A2.5 excerpt."""
    results = {}
    vp = os.path.join(root, VP)
    sample_block(root, env, results)
    for label, (graph, folder) in a4_runs().items():
        run_seeded(vp, env, label, graph, folder, results)
    excerpt(vp, results)
    return results
```

### Report excerpt

`s1_artifact_numbers.py` lines 327-387

```python
# step: Report excerpt
def counts_table(report):
    """Return the numbers of a report's counts table, the one headed Count and Number, in its order."""
    numbers, inside = [], False
    for line in report.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not inside:
            inside = cells == ["Count", "Number"]
        elif not line.startswith("|"):
            break
        elif set(cells[-1]) - set("-"):
            # Every row but the line of dashes under the heading.
            numbers.append(int(cells[-1]))
    return numbers


def section_bullets(report, heading):
    """Return the bullet lines of one ## section of a report."""
    bullets, inside = [], False
    for line in report.splitlines():
        if line.startswith("## "):
            inside = line[len("## "):].strip() == heading
        elif inside and line.startswith("- "):
            bullets.append(line)
    return bullets


def located(quote):
    """True when the passage step located a quote, not a section pointer, that a program found in the source."""
    return quote.get("from") == "located" and quote.get("kind") == "quote" and quote.get("in_source") == "yes"


def excerpt(vp, results):
    """Keep the figures the A2.5 excerpt prints from the references run's own report.md and fields.json."""
    files = os.path.join(vp, demo(a4_runs()[P["excerpt_stream"]][0]), "files")
    fields = read_json(os.path.join(files, "fields.json"))
    with open(os.path.join(files, "report.md")) as f:
        report = f.read()
    head, digits = fields["run"], P["hash_digits"]
    named = pairs(P["excerpt_counts"])
    ai = [it for it in fields["items"] if it.get("origin") == "ai"]
    # The entry shown in full is excerpt_row when it is an AI citation with a located quote, else the first such.
    entries = [it for it in ai if any(located(q) for q in it.get("quotes") or [])]
    entry = ([it for it in entries if it["id"] == P["excerpt_row"]] or entries)[0]
    # The report is written from its fields, so the two must agree on what the excerpt shows.
    if (counts_table(report) != [head[field] for _, field in named] or head["draft_sha256"] not in report
            or "### " + entry["heading"] not in report):
        raise ValueError("report.md and fields.json of the excerpt's run disagree")
    results["excerpt.doc_sha"] = head["draft_sha256"].split(":")[-1][:digits]
    for key, field in named:
        results["excerpt." + key] = head[field]
    results["excerpt.row"] = entry["id"]
    results["excerpt.row_source_sha"] = entry["source_sha256"].split(":")[-1][:digits]
    results["excerpt.row_location"] = [q for q in entry["quotes"] if located(q)][0]["location"]
    # The AI entries the excerpt omits before and after the one shown, in the report's order of headings.
    ai_ids = {it["id"] for it in ai}
    order = [h for h in re.findall(r"^### (\S+):", report, re.M) if h in ai_ids]
    at = order.index(entry["id"])
    results["excerpt.ai_before"] = at
    results["excerpt.ai_after"] = len(order) - at - 1
    results["excerpt.notes_omitted"] = len(section_bullets(report, "Notes"))
```

### Count files

`s1_artifact_numbers.py` lines 390-449

```python
# step: Count files
def front_matter(text):
    """Return the name: value lines of a markdown file's opening block between --- lines."""
    lines = text.splitlines()
    out = {}
    if lines[:1] == ["---"]:
        for line in lines[1:]:
            if line.strip() == "---":
                break
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip()
    return out


def count_calls(source, name):
    """Count the calls in Python source whose function is name, alone or as an attribute."""
    total = 0
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call):
            f = node.func
            if (isinstance(f, ast.Name) and f.id == name) or (isinstance(f, ast.Attribute) and f.attr == name):
                total += 1
    return total


def archive_counts(archive):
    """Count what the appendix counts in the archive's files, without running anything."""
    results = {}
    with tarfile.open(archive) as tf:
        members = [m for m in tf.getmembers() if m.isfile()]
        names = {m.name for m in members}

        def text(name):
            """Return one archived file's text."""
            return tf.extractfile(name).read().decode("utf-8")

        results["repo.files"] = len(members)
        size = sum(m.size for m in members) / P["bytes_per_mb"]
        results["repo.mb"] = "{0:.{1}f}".format(size, P["mb_digits"])
        corpus = P["kb_corpus"].rstrip("/") + "/"
        entries = sorted(n for n in names
                         if n.startswith(corpus) and n.endswith(".md") and n[len(corpus):].count("/") == 1)
        results["kb.entries"] = len(entries)
        outside = 0
        for name in entries:
            source = front_matter(text(name)).get("source", "")
            # Outside when no file of the artifact is the source the entry names.
            if not any(n == source or n.endswith("/" + source) for n in names):
                outside += 1
        results["kb.outside"] = outside
        results["kb.tools"] = count_calls(text(P["kb_server"]), P["kb_tool_call"])
        results["runtime.commands"] = count_calls(text(P["runtime_file"]), P["command_call"])
        sizes = []
        for stream in P["seeded_streams"].split():
            for kind in P["fixture_kinds"].split():
                prefix = "/".join((VP, "fixtures", stream, kind)) + "/"
                sizes.append(sum(n.startswith(prefix) for n in names))
        results["fixtures.min_files"] = min(sizes)
        results["fixtures.max_files"] = max(sizes)
    return results
```

### Write tables

`s1_artifact_numbers.py` lines 452-476

```python
# step: Write tables
def main():
    """Compute every number, add the word forms, and write the three tables and the parameter record."""
    archive = P["artifact_archive"]
    counts = archive_counts(archive)
    # The real path, since pytest names a test's file relative to its root folder only when
    # both are spelled the same way, and macOS reaches the temporary folder through a link.
    base = os.path.realpath(tempfile.mkdtemp(prefix="artifact_numbers_"))
    try:
        env = child_env(base)
        suites = suite_counts(run_suites(unpack(archive, base, "suites"), env, base))
        a4 = a4_blocks(unpack(archive, base, "commands"), env)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    words, caps = P["word_keys"].split(), P["word_cap_keys"].split()
    for results in (suites, a4, counts):
        results_io.add_words(results, [k for k in words if k in results], [k for k in caps if k in results])
    results_io.write_rows("suite_counts.csv", suites)
    results_io.write_rows("a4_results.csv", a4)
    results_io.write_rows("artifact_counts.csv", counts)
    P.write_record()


if __name__ == "__main__":
    main()
```

### Read parameters

`s2_live_runs.py` lines 58-74

```python
# step: Read parameters
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile

import yaml

import params_io
import results_io

P = params_io.Params(step="live", script="s2_live_runs.py")
FLAGGING = ("blocking", "warning")
HOMES = ("HOME", "AUDIT_HOME", "CONNECTIONS_HOME", "FEATURES_HOME", "XDG_CONFIG_HOME")
```

### Read answers

`s2_live_runs.py` lines 77-136

```python
# step: Read answers
def pairs(text):
    """Split a parameter written as name=value words into (name, value) pairs, in order."""
    return [tuple(word.split("=", 1)) for word in text.split()]


def read_json(path):
    """Read one JSON file."""
    with open(path) as f:
        return json.load(f)


def parse_answer(text):
    """Return the answer object in a saved answer's text, or None when it does not parse."""
    try:
        return json.loads(text[text.index("{"):text.rindex("}") + 1])
    except ValueError:
        return None


def flags(answer):
    """True when a saved answer finds a problem with its item (see Assumptions)."""
    if not isinstance(answer, dict):
        return False
    if "verdict" in answer:
        return answer["verdict"] != "supports"
    if "matches" in answer:
        return answer["matches"] is False
    return answer.get("honest") is False or answer.get("meaning_changed") is True


def step_folder(run, step):
    """Return the run's responses folder for one judgment step, or None when the run has none."""
    folder = os.path.join(run, "responses")
    for name in sorted(os.listdir(folder)):
        if name.split("_", 1)[-1] == step:
            return os.path.join(folder, name)
    return None


def answer_of(run, step, item):
    """Return the parsed saved answer of one step for one item, its retry when there is one."""
    folder = step_folder(run, step)
    if folder is None:
        return None
    for name in (item + P["retry_suffix"], item + ".txt"):
        path = os.path.join(folder, name)
        if os.path.exists(path):
            with open(path) as f:
                return parse_answer(f.read())
    return None


def answered_items(run, step):
    """Return the items a step has a first saved answer for, retries left out."""
    folder = step_folder(run, step)
    if folder is None:
        return []
    return sorted(n[:-len(".txt")] for n in os.listdir(folder)
                  if n.endswith(".txt") and not n.endswith(P["retry_suffix"]))
```

### Planted faults

`s2_live_runs.py` lines 139-145

```python
# step: Planted faults
def judgment_faults(tf, stream):
    """Return the planted faults of a procedure's seeded test files whose check is a judgment step."""
    graph = yaml.safe_load(tf.extractfile("verification_procedures/graphs/" + stream + ".yaml"))
    judged = {n["id"] for n in graph["nodes"] if n.get("kind") == "judgment"}
    truth = yaml.safe_load(tf.extractfile("verification_procedures/fixtures/" + stream + "/seeded/truth.yaml"))
    return [f for f in truth["faults"] if f["check"] in judged]
```

### Count runs

`s2_live_runs.py` lines 148-171

```python
# step: Count runs
def one_run(run, results, prefix):
    """Count one run's saved answers, judged items, and findings, and its score when it has one."""
    files = []
    for _, _, names in os.walk(os.path.join(run, "responses")):
        files.extend(names)
    results[prefix + "responses"] = len(files)
    results[prefix + "retries"] = sum(n.endswith(P["retry_suffix"]) for n in files)
    items = 0
    for name in sorted(os.listdir(os.path.join(run, "records"))):
        execution = read_json(os.path.join(run, "records", name)).get("execution") or {}
        if execution.get("type") == "judgment":
            items += execution.get("items", 0)
    results[prefix + "items"] = items
    findings = read_json(os.path.join(run, "files", "findings.json"))
    findings = findings["items"] if isinstance(findings, dict) else findings
    results[prefix + "findings"] = sum(f["severity"] in FLAGGING for f in findings)
    results[prefix + "graph_version"] = read_json(os.path.join(run, "manifest.json"))["graph"]["version"]
    score_file = os.path.join(run, "score.json")
    if os.path.exists(score_file):
        score = read_json(score_file)
        results[prefix + "faults"] = score["faults"]
        results[prefix + "caught"] = len(score["caught"])
        results[prefix + "extras"] = len(score["extra_findings"])
```

### No-answer trial

`s2_live_runs.py` lines 174-210

```python
# step: No-answer trial
def child_env(base):
    """Return the environment the trial runs with (see Assumptions)."""
    env = dict(os.environ)
    for name in HOMES:
        env[name] = os.path.join(base, "homes", name.lower())
        os.makedirs(env[name], exist_ok=True)
    env["VG_OFFLINE"] = "1"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    harness = P["harness_programs"].split()
    # Drop each folder on the command path that holds a harness program.
    keep = [d for d in env.get("PATH", "").split(os.pathsep)
            if d and not any(os.path.exists(os.path.join(d, h)) for h in harness)]
    env["PATH"] = os.pathsep.join(keep)
    return env


def no_answer_trial(art, base, results):
    """Run the earlier copy's procedure on its seeded test files with no model answers, score it, and keep the score."""
    art.extractall(os.path.join(base, "earlier"))
    vp = os.path.join(base, "earlier", "verification_procedures")
    empty = os.path.join(base, "no_answers.json")
    with open(empty, "w") as f:
        f.write("{}\n")
    stream = P["nojudge_stream"]
    fx = os.path.join("fixtures", stream, "seeded")
    rundir = os.path.join("runs", "nojudge_" + stream)
    env = child_env(base)
    cmd = [sys.executable, "vg.py", "run", os.path.join("graphs", stream + ".yaml"), "--run", rundir, "--inputs", fx]
    for flag, name in (("--judge", "recorded_judge.json"), ("--second", "recorded_second.json")):
        if os.path.exists(os.path.join(vp, fx, name)):
            cmd += [flag, "recorded:" + empty]
    for args in (cmd, [sys.executable, "vg.py", "score", "--run", rundir, "--truth", os.path.join(fx, "truth.yaml")]):
        subprocess.run(args, cwd=vp, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    score = read_json(os.path.join(vp, rundir, "score.json"))
    results[stream + "_nojudge.faults"] = score["faults"]
    results[stream + "_nojudge.caught"] = len(score["caught"])
```

### Write table

`s2_live_runs.py` lines 213-269

```python
# step: Write table
def main():
    """Count every run, then the totals and comparisons, and write the table and the parameter record."""
    base = tempfile.mkdtemp(prefix="live_runs_")
    results = {}
    try:
        with tarfile.open(P["live_archive"]) as tf:
            tf.extractall(base)
            results["live.runs"] = len({m.name.split("/", 1)[0] for m in tf.getmembers()})
        runs = dict(pairs(P["live_runs"]))
        for label, folder in runs.items():
            one_run(os.path.join(base, folder), results, "live." + label + ".")
        for key in ("responses", "retries", "items"):
            results["live." + key] = sum(results["live." + label + "." + key] for label in runs)
        with tarfile.open(P["procedures_archive"]) as art:
            caught_all = faults_all = 0
            for label in P["judgment_runs"].split():
                run = os.path.join(base, runs[label])
                stream = read_json(os.path.join(run, "manifest.json"))["stream"]
                faults = judgment_faults(art, stream)
                caught = sum(flags(answer_of(run, f["check"], f["item"])) for f in faults)
                results["live." + label + ".judgment_faults"] = len(faults)
                results["live." + label + ".judgment_caught"] = caught
                faults_all += len(faults)
                caught_all += caught
            results["live.judgment_faults"] = faults_all
            results["live.judgment_caught"] = caught_all
            # Support verdicts of the live run against the recorded answers that come with the artifact.
            run = os.path.join(base, runs[P["differ_run"]])
            stream = read_json(os.path.join(run, "manifest.json"))["stream"]
            kind = P["differ_run"].rsplit(".", 1)[-1]
            recorded = json.load(art.extractfile(
                "verification_procedures/fixtures/" + stream + "/" + kind + "/recorded_judge.json"))
            no_answer_trial(art, base, results)
        step = P["support_step"]
        rows = answered_items(run, step)
        differ = 0
        for row in rows:
            live = answer_of(run, step, row) or {}
            if live.get("verdict") != (recorded.get(step + ":" + row) or {}).get("verdict"):
                differ += 1
        results["live.verdict_rows"] = len(rows)
        results["live.verdicts_differ"] = differ
        rechecks = answered_items(run, P["recheck_step"])
        results["live.rechecks"] = len(rechecks)
        results["live.rechecks_agree"] = sum((answer_of(run, P["recheck_step"], r) or {}).get("agree") is True
                                             for r in rechecks)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    results_io.add_words(results, [k for k in P["word_keys"].split() if k in results],
                         [k for k in P["word_cap_keys"].split() if k in results])
    results_io.write_rows("live_runs.csv", results)
    P.write_record()


if __name__ == "__main__":
    main()
```

## Descriptions

Each row is a sentence of the final build's text that the finding step gave as describing this phase, with the places in the scripts it gave. The last two columns are the program's checks. A place is confirmed when it is lines of a script the pipeline declares, and the steps it falls in are named beside it.

| Id | Description in the final build's text | Where the scripts carry it out | Quote in the text | Location check |
|---|---|---|---|---|
| d01 | The first suite reports `443 passed` in about a minute and the second `872 passed` in about 10 minutes. | `s1_artifact_numbers.py` lines 172-211 (analysis, Run tests) | yes | confirmed |
| d02 | The other six report `1333 passed`, `39 passed`, `148 passed`, `338 passed`, `559 passed`, and `644 passed`, in the order run, 4376 tests in all, and the whole block takes about 20 minutes. | `s1_artifact_numbers.py` lines 172-211 (analysis, Run tests) | yes | confirmed |
| d03 | Its analysis script computes the results the two products cite from one data file, the build fills them in from the project's numbers file, and the data procedure then checks each value in that file against a rerun of the analysis, on the project's files that a handoff gathers. | `s1_artifact_numbers.py` lines 235-284 (analysis, A4 commands) | yes | confirmed |
| d04 | A second handoff gathers the pipeline, its script, and the text of the latest manuscript build for the data analysis report, whose one model step is answered from recorded answers. | `s1_artifact_numbers.py` lines 266-270 (analysis, A4 commands) | yes | confirmed |
| d05 | Each build takes under a second and writes version `v001`, the manuscript as `builds/manuscript/v001.docx` and the slides as `builds/slides/v001.html`, each with a copy of its filled-in text and a row in its ledger. | `s1_artifact_numbers.py` lines 246-258 (analysis, A4 commands) | yes | confirmed |
| d06 | A placeholder with no value stops the build, which lists every missing key. | missing | yes | missing |
| d07 | Opening the slides in a browser loads the reveal.js library from the web. | missing | yes | missing |
| d08 | The data procedure's run takes under 3 seconds and reports 0 blocking findings and 0 warnings, with all 10 cited numbers matching the rerun. | `s1_artifact_numbers.py` lines 264-278 (analysis, A4 commands) | yes | confirmed |
| d09 | In a trial with one number changed by hand in the numbers file, the run reported it as blocking. | missing | yes | missing |
| d10 | The data analysis report's outline lists 5 steps of the script, and a program confirms each description the model step found, 1 in all, in the text and the script. | `s1_artifact_numbers.py` lines 279-284 (analysis, A4 commands) | yes | confirmed |
| d11 | The run takes about 3 seconds and completes 11 of the graph's 11 steps, including its one judgment step, which locates passages and gives no verdict. | `s1_artifact_numbers.py` lines 287-301 (analysis, A4 commands) | yes | confirmed |
| d12 | The `verify` command reports `replay matches` for each of the 9 tool steps it reruns (A2.4), and the `score` command prints `{"faults": 13, "recall": 1.0, "missed": []} extras=0`. | `s1_artifact_numbers.py` lines 302-313 (analysis, A4 commands) | yes | confirmed |
| d13 | Every finding in this report is a note, and only blocking findings and warnings count as extras. | missing | yes | missing |
| d14 | The `score` command reports every planted fault caught, 7 of 7 for prose, 9 of 9 for data, 2 of 2 for the data cleaning report, and 7 of 7 for build, with 0, 2, 0, and 0 extra findings. | `s1_artifact_numbers.py` lines 305-313 (analysis, A4 commands) | yes | confirmed |
| d15 | The two for data fall on items that planted faults touch. | missing | yes | missing |
| d16 | Each run takes under 3 seconds. | missing | yes | missing |
| d17 | Offline runs take under 4 seconds per procedure on test sets of 4 to 25 files. | `s1_artifact_numbers.py` lines 442-448 (analysis, Count files) | yes | confirmed |
| d18 | A live run sends a model one request for each judged item, and the seeded references files have 6 judged items, each a passage to locate. | `s1_artifact_numbers.py` lines 225-232 (analysis, A4 commands) | yes | confirmed |
| d19 | The data procedure asks no model, and each data phase report sends one request holding the final build's text and the pipeline's scripts. | missing | yes | missing |
| d20 | Nothing has been measured on a full manuscript. | missing | yes | missing |
| d21 | The tests use recorded answers so that they give the same result on every run, while a live run saves every prompt and answer per item with a checksum of the prompt. | missing | yes | missing |
| d22 | A reader can therefore review the answers a run used even if a model answers differently on another run. | missing | yes | missing |
| d23 | On October 8, 2026, seven development runs had AI models answer every judgment step in earlier versions of the references, data, and prose procedures, on the clean and seeded test files of that time. | `s2_live_runs.py` lines 219-221 (analysis, Write table) | yes | confirmed |
| d24 | Those steps judged whether a source supports its sentence, with a second model's recheck and a proposed fix, whether each method's documentation describes its code, and whether each AI rationale describes its change. | missing | yes | missing |
| d25 | Of the steps these runs answered, the current procedures keep only the one that locates a passage. | missing | yes | missing |
| d26 | Table A10 gives the models and settings, and Table A11 the results. | missing | yes | missing |
| d27 | Both models are open-weight models reached through a university-hosted inference service, whose address the runtime reads from the provider setting (A2.2). | missing | yes | missing |
| d28 | Recorded answers let any reader run the references procedure and the three data phase reports without a model key (A4), and the other procedures ask no model, while rerunning live judgment needs a key to that service. | missing | yes | missing |
| d29 | In the live runs, every planted fault was caught in all three procedures, and the six that depend on judgment were caught by the models' own verdicts, read from the saved answers rather than from the score. | `s2_live_runs.py` lines 227-239 (analysis, Write table) | yes | confirmed |
| d30 | The `score` command then counted a fault as caught when any blocking finding or warning named the same check and item, so a "not judged" warning also counted. | missing | yes | missing |
| d31 | It now counts a finding of any severity that names the fault's check and an item holding the fault's item. | missing | yes | missing |
| d32 | In a trial run with no model answers, the earlier prose procedure still scored 10 of 10, and the current one has no model step. | `s2_live_runs.py` lines 191-210 (analysis, No-answer trial) | yes | confirmed |
| d33 | The clean files gave no warning or blocking finding for references and data, and one warning for prose (Table A11). | `s2_live_runs.py` lines 149-164 (analysis, Count runs) | yes | confirmed |
| d34 | In the live seeded references run, four of the five extra findings follow from planted faults. | `s2_live_runs.py` lines 166-171 (analysis, Count runs) | yes | confirmed |
| d35 | The fifth is a partly verdict on row r06, a sentence with no planted support fault whose recorded answer at the time was supports, and the second model agreed with the partly verdict. | missing | yes | missing |
| d36 | Row r06's reference then carried a planted wrong year, which was caught separately. | missing | yes | missing |
| d37 | Of note, the prose procedure's pitfalls and prompt wording were revised after its first live run, which made two errors, and the same seeded test file was then run again. | missing | yes | missing |
| d38 | The clean prose warning came after that revision. | missing | yes | missing |
| d39 | For all seven live runs, the saved code of most tool steps differs from the committed code, since the references, data, and prose procedures were rebuilt after October 8. | missing | yes | missing |
| d40 | No saved prompt can be rendered from the committed templates, which were removed or rewritten. | missing | yes | missing |
| d41 | All seven runs used contract files that differ from the committed ones, and each also used an earlier graph than the committed one. | missing | yes | missing |
| d42 | The runtime file is not recorded in run folders and changed on October 8. | missing | yes | missing |
| d43 | Every run folder from October 8 passed the `verify` command (A2.4) on October 23, 2026. | missing | yes | missing |
| d44 | Each test file was run once per model configuration, except the seeded prose file, which was run again after the revision, so run-to-run variation has not been measured. | missing | yes | missing |
| d45 | Within these runs, live support verdicts differed from the recorded answers of that time on 3 of 12 references rows, and one data answer was cut off and parsed only on retry, with its finish reason not saved. | `s2_live_runs.py` lines 240-255 (analysis, Write table) | yes | confirmed |
| d46 | The second model agreed with the first on all five rechecks, and the recorded second answers of that time also agreed, so a disagreement between the two checkers did not occur in either mode before the second check was removed. | `s2_live_runs.py` lines 256-259 (analysis, Write table) | yes | confirmed |
| d47 | The run records are \[LIVE RECORDS LOCATION\]. | missing | yes | missing |

## Files read

- `final_text.md`, the final build's text, sha256:6cfef15424907eb740a62a668ab9aaf9cecadbe47765b67dce2e205bcd4fb076
- `pipeline.yaml`, the pipeline, sha256:5d2b08aebbf298038c44b8ae6e0d7e23f33a141ef3c285882a85436572d31c3c
- `s1_artifact_numbers.py`, the script of step artifact, sha256:c0d7c3fbf27aa4c612ca7db1da28dc4720df03271a727d126b28220a4d01da27
- `s2_live_runs.py`, the script of step live, sha256:7f78483fe3e311f914f4c2353090b9bcd97232c49e0fa6fcc0343e7b3301fe17

## Notes

None.
